from flask import Flask, render_template, request
from flask import jsonify
from search import search, link
app = Flask(__name__,static_url_path="/static")

#############

@app.route('/message', methods=['POST'])
def reply():
    return jsonify( { 'text': execute.decode_line(sess, model, enc_vocab, rev_dec_vocab, request.form['msg'] ) } )

@app.route('/_searcher', methods=['POST'])
def searcher():
    return jsonify( { 'text': search(request.form['msg'] ) + link(request.form['msg']) } )

@app.route("/")
def index():
    return render_template("index.html")

#############


'''
Init seq2seq model

    1. Call main from execute.py
    2. Create decode_line function that takes message as input
'''

import tensorflow as tf
import execute

sess = tf.Session()
sess, model, enc_vocab, rev_dec_vocab = execute.init_session(sess, conf='seq2seq_serve.ini')

# start app
if (__name__ == "__main__"):
    app.run(port="5000")
