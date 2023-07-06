
### Project Runeberg - Selma Lagerlöf downloader

# with bonus nanoGPT usecase

This repo contains a simple python downloader script made
to download a set of texts/books by the famous author [Selma Lagerlöf](https://sv.wikipedia.org/wiki/Selma_Lagerl%C3%B6f).
The texts are part of the awesome [Project Runeberg](http://runeberg.org/).

Project Runeberg (runeberg.org) is a volunteer effort to create free electronic editions of classic Nordic (Scandinavian) literature and make them openly available over the Internet.

### Built With
* Python
* Docker  (optional)
* nanoGPT (optional)

### Usage

<pre>git clone https://github.com/slaskhas/runeberg_selmalagerlof.git
cd runeberg_selmalagerlof</pre>

alt 1:

To simply use the download script:
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

alt 3:

Use the pre-built container allwidgets/runeberg_selmalagerlof on dockerhub.

<pre>
docker run  -v `pwd`:/wrk -it  --rm  allwidgets/runeberg_selmalagerlof
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
* nanogpt\_train\_resume
* nanogpt_eval

Optionally the parameter `bash`  may be used to drop into the container and run the script `/handle.sh` manually.

Steps to build and use:

<pre>
docker build -t selma .
docker run  -v `pwd`:/wrk -it  --rm  selma nanogpt_install
docker run  -v `pwd`:/wrk -it  --rm  selma nanogpt_prepare  nanogpt_train
docker run  -v `pwd`:/wrk -it  --rm  selma nanogpt_eval
</pre>

After 500 iterations, expect something like:
<pre>
Det var bra lär den för och de var Oljänniskor bli bli
mycket ända fram och tillbaka. Hon skulle då så lås aldrig rörde, att hennes bli många i upphärkarna, att lättre föjde
frun
</pre>
Somewhat jibberish, but still readable.
Use parameter `nanogpt_train_resume` to improve the result.
<pre>
docker run  -v `pwd`:/wrk -it  --rm  selma nanogpt_train_resume
docker run  -v `pwd`:/wrk -it  --rm  selma nanogpt_eval
</pre>
After 10000 iterations you may get
<pre>
Men så tänkte jag: "Gå och dricker in på nytt och se!"

Jag tänkte, att jag skulle bli övergiven, att detta var
för jag hade alltid kommit i natt, så att jag kunde komma hit i
tiden. Såg jag väl hur jag skulle ha kommit och att han
därmed hade blivit sjuk, kunde jag inte finna sådant, som inte
hade varit något hjärt än att få tala med mig om.
</pre>

Somewhat jibberish, but on a much higher level :-) .

### License

This code is licensed under the [MIT License](https://en.wikipedia.org/wiki/MIT_License). nanoGPT code is not part of this repository but I want to mention that it is also using MIT license. 

Regarding the actual material by Selma lagerlöf, this is from Project Runeberg: <pre>
Project Runeberg is very careful to respect copyright
held by authors, illustrators, and translators. 
But when they have been dead for more than 70 years, 
the copyright expires, 
and we are free to publish their works.
</pre>

### Todo

This was a quick hack to download and cleanup some data from Project Runeberg. A future task may be to add download script for Stridberg and many other authors from the same site.

### acknowledgements
[Project Runeberg](http://runeberg.org/) of course, and [Andrej
karpathy](https://github.com/karpathy) for [nanoGPT](https://github.com/karpathy/nanoGPT) .

## Claes Nygren 
