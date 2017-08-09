# Faulknerbot

![William Faulkner](faulknerbot.jpg)


Overview
============
In this demo code, I've implemented Tensorflow's [Sequence to Sequence](https://www.tensorflow.org/versions/r0.12/tutorials/seq2seq/index.html) model to train a chatbot on the [Faulkner at Virginia: An Audio Archive](https://http://faulkner.lib.virginia.edu/).

Dependencies
============
* numpy
* scipy
* six
* tensorflow (https://www.tensorflow.org/versions/r0.12/get_started/os_setup.html)

Use [pip](https://pypi.python.org/pypi/pip) to install any missing dependencies


Usage
===========

To train the bot, edit the `seq2seq.ini` file so that mode is set to train like so

`mode = train`

then run the code like so

``python execute.py``

To test the bot during or after training, edit the `seq2seq.ini` file so that mode is set to test like so

`mode = test`

then run the code like so

``python execute.py``


Credits
===========
Credit for the vast majority of code here goes to the [TensorFlow authors](https://research.google.com/pubs/pub45166.html). I've preprocessed the dataset and trained the system. I've also included a quick search function to retrieve results from The University of Virginia Libraries Faulkner at [Virginia Audio Archive site](http://faulkner.lib.virginia.edu/). I've also added a objectionable language editing system to avoid [the fate of Tay](http://arstechnica.com/information-technology/2016/03/tay-the-neo-nazi-millennial-chatbot-gets-autopsied/).

