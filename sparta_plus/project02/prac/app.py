

import requests
from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/')
def main():
    myname = "Sparta"
    #name이란 이름으로 myname을 넘겨줘라
    return render_template("index.html", name =myname)


@app.route('/detail/<keyword>')
def detail(keyword):
    # r = requests.get('http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99')
    # response = r.json()
    # rows = response['RealtimeCityAir']['row']
    r = requests.get(f"https://owlbot.info/api/v4/dictionary/{keyword}", headers={"Authorization" : "Token 8e2f99bd6d20e9eabbbb6d4a5026da855b0d5a53"})
    result = r.json()
    print(result)
    word_receive = request.args.get("word_give")
    return render_template("detail.html",  word=keyword)
    # return render_template("detail.html", rows=rows, word=word_receive)


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)