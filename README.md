
### Project Runeberg - Selma Lagerlöf downloader

# with bonus nanoGPT usecase

This repo contains a simple python downloader script made
to download a set of texts/books by the famous author [Selma Lagerlöf](https://sv.wikipedia.org/wiki/Selma_Lagerl%C3%B6f).
The texts are part of the awesome [Project Runeberg](http://runeberg.org/).

Project Runeberg (runeberg.org) is a volunteer effort to create free electronic editions of classic Nordic (Scandinavian) literature and make them openly available over the Internet.

###Built With
* Python
* Docker
* nanoGPT (optional)

### Usage

<pre>git clone https://github.com/slaskhas/runeberg_selmalagerlof.git
cd runeberg_selmalagerlof</pre>

alt 1:

To simply install and run the download script:
<pre>
python3 runeberg_selmalagerlof/runeberg_selmalagerlof.py
</pre>

Each asset will end up in it's own textfile in current folder.
Expect output like:
<pre>
Downloading annasvard.txt
Downloading mirakler.txt
Downloading bannlyst.txt
Downloading charlowe.txt
.
.
</pre>

alt 2:

Use the included docker container def on linux or mac to download the content:

<pre>docker build -t selma .
docker run  -v `pwd`:/wrk -it  --rm  selma 
</pre>

It's important to mount current directory as /wrk or the downloaded data will be gone once the container is deleted.

### Bonus : train nanoGPT using the downloaded data

Scripts and Dockerfile are included to clone and train a model for the famous [nanoGPT](https://github.com/karpathy/nanoGPT)  "The simplest, fastest repository for training/finetuning medium-sized GPTs" , by [Andrej
karpathy](https://github.com/karpathy)

Pass one or multiple parameters while running the docker container mentioned above.
Parameters are:

* nanogpt_install
* nanogpt_prepare
* nanogpt_train
* nanogpt_train_resume
* nanogpt_eval

Optionally the parameter `bash`  may be used to drop into the container and run the script `/handle.sh` manually.

Steps to build and use:

<pre>
docker build -t selma .
docker run  -v `pwd`:/wrk -it  --rm  selma nanogpt_install
docker run  -v `pwd`:/wrk -it  --rm  selma nanogpt_prepare  nanogpt_train
docker run  -v `pwd`:/wrk -it  --rm  selma nanogpt_eval
</pre>

After 500 itterations, expect something like:
<pre>
Det var bra lär den för och de var Oljänniskor bli bli
mycket ända fram och tillbaka. Hon skulle då så lås aldrig rörde, att hennes bli många i upphärkarna, att lättre föjde
frun
</pre>
Somewhat jibberish, but still readable.
Use parameter `nanogpt_train_resume` to improve the result.


