from classes import *
from semantic_analysis import word_dict,amount_dict
from flask import Flask, url_for, render_template, redirect, request, json,jsonify

app = Flask(__name__)

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
    app.run(debug=True,port=8000)
