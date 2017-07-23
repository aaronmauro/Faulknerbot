from flask import Flask, render_template, request, url_for, redirect
from flask import jsonify
from search import search, link

app = Flask(__name__, static_url_path="/static")

#############
## Routing ##
#############

@app.route('/message', methods=['POST'])
def reply():
    return jsonify( { 'text': execute.decode_line(sess, model, enc_vocab, rev_dec_vocab, request.form['msg'] ) } )

@app.route("/")
def index():
    return render_template("index.html", search = search)

'''
@app.route("/")
def hello():
    return "Hello, I will be a William Faulkner chatbot soon."
'''
# fire up Tensor Flow

import tensorflow as tf
import execute

sess = tf.Session()
sess, model, enc_vocab, rev_dec_vocab = execute.init_session(sess, conf='seq2seq_serve.ini')

# start app
if (__name__ == "__main__"):
    app.run('104.236.248.34')
