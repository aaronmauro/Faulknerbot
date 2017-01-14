# Faulknerbot

![William Faulkner](http://a2.files.biography.com/image/upload/c_fit,cs_srgb,dpr_1.0,h_1200,q_80,w_1200/MTE5NDg0MDU0OTYxNzUxNTY3.jpg)


Overview
============
In this demo code, we implement Tensorflows [Sequence to Sequence](https://www.tensorflow.org/versions/r0.12/tutorials/seq2seq/index.html) model to train a
chatbot on the [Faulkner at Virginia: An Audio Archive](https://http://faulkner.lib.virginia.edu/).

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
This chatbot is based on the Tensorflow Chatbot Demo by @Sirajology on [Youtube](https://youtu.be/SJDEOWLHYVo). Credit for the vast majority of code here goes to [suriyadeepan](https://github.com/suriyadeepan). I've preprocessed the dataset and trained the system. I've also added a objectionable language editing system to avoid [the fate of Tay](http://arstechnica.com/information-technology/2016/03/tay-the-neo-nazi-millennial-chatbot-gets-autopsied/).
