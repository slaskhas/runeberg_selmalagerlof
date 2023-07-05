#!/bin/bash


# echo Your args are: "$@"

params=$(echo "$@" | tr " " "\n")

if  [ -z "$params" ]
then
    echo ""
    echo "usage: docker run -v \`pwd\`:/wrk  -it --rm selma  <params1 params2 ..>"
    echo ""
    echo "where (optional) params are: nanogpt_install nanogpt_prepare  nanogpt_train  nanogpt_train_resume nanogpt_eval"
    echo "If no parameter is given (as in now) data will be downloaded only, to /wrk"
    echo "If /wrk is not mounted ( -v \`pwd\`:/wrk ), downloaded data may be lost."
    echo ""
    echo "To run commands from shell: docker run -v \`pwd\`:/wrk  -it --rm selma bash"
    echo "/handle.sh <params1 params2 ..>"
    echo ""
    params="download"
fi

python3 /runeberg_selmalagerlof/runeberg_selmalagerlof.py


for param in $params
do
    if [ "$param" = "nanogpt_install" ]
    then
	cd /wrk
	git clone https://github.com/karpathy/nanoGPT.git
	python3 -m venv /wrk/nanoGPT/venv
        . /wrk/nanoGPT/venv/bin/activate
	python3 -m pip install torch numpy transformers datasets tiktoken wandb tqdm
	mkdir /wrk/nanoGPT/data/runeberg_selmalagerlof
	python3 /runeberg_selmalagerlof/joiner.py
	cp /runeberg_selmalagerlof/fancy_prepare.py /wrk/nanoGPT/data/runeberg_selmalagerlof
	cp /runeberg_selmalagerlof/train_selmalagerlof.py /wrk/nanoGPT/config/
	deactivate
    fi
    if [ "$param" = "bash" ]
    then
        echo ""
        echo "Available parameters are: nanogpt_install nanogpt_prepare  nanogpt_train  nanogpt_train_resume nanogpt_eval"
        echo ""
	echo ". /wrk/nanoGPT/venv/bin/activate"
        echo "/handle.sh <params1 params2 ..>"
        echo ""
	bash
    fi
    if [ "$param" = "nanogpt_prepare" ]
    then
	echo "nanogpt_prepare"
	. /wrk/nanoGPT/venv/bin/activate
	cp /runeberg_selmalagerlof/fancy_prepare.py /wrk/nanoGPT/data/runeberg_selmalagerlof
        cd  /wrk/nanoGPT
        python3 ./data/runeberg_selmalagerlof/fancy_prepare.py
	deactivate
    fi
    if [ "$param" = "nanogpt_train" ]
    then
	echo "nanogpt_train"
	. /wrk/nanoGPT/venv/bin/activate
        cd /wrk/nanoGPT
	python3 train.py config/train_selmalagerlof.py --compile=False --eval_iters=20 --log_interval=1 --batch_size=12  --max_iters=1000 --lr_decay_iters=1000 --dropout=0.0
	deactivate
    fi
    if [ "$param" = "nanogpt_train_resume" ]
    then
	echo "nanogpt_train_resume"
	. /wrk/nanoGPT/venv/bin/activate
        cd /wrk/nanoGPT
	python3 train.py config/train_selmalagerlof.py --init_from=resume --compile=False --eval_iters=20 --log_interval=1  --batch_size=12  --max_iters=10000 --lr_decay_iters=10000 --learning_rate=1e-4
	deactivate
    fi
    if [ "$param" = "nanogpt_eval" ]
    then
	echo "nanogpt_eval"
	. /wrk/nanoGPT/venv/bin/activate
        cd /wrk/nanoGPT
        python3 sample.py    --out_dir=out-selmalagerlof --device=cpu --seed=`python3 -c "import random;print(random.randint(1, 25000))"`
	deactivate
    fi
done
