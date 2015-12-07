from classes import *
from flask import Flask, url_for, render_template, redirect, request, json,jsonify
import os
import cPickle as pickle
app = Flask(__name__)
with open('dictionary_data.pkl','r') as my_input:
    word_dict = pickle.load(my_input)
    amount_dict = pickle.load(my_input)


keywords = []
for word in word_dict.keys():
    keywords.append(keyword(word.upper(),amount_dict[word]))
keywords.sort(key= lambda x:x.frequency, reverse=True)
@app.route('/')
def index():
    return render_template("index.html",words = map(lambda x: x,keywords))

@app.route('/<keyword_>')
def render(keyword_):
    return render_template("keyword.html",key = keyword_.lower().capitalize(),emails=word_dict[keyword_.lower()])

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, port=port)
