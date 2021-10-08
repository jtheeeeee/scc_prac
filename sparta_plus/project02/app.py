from flask import Flask, render_template, request, jsonify, redirect, url_for
from pymongo import MongoClient
import requests

app = Flask(__name__)

client = MongoClient('54.180.122.204', 27017, username="test", password="test")
db = client.dbsparta_plus_week2


@app.route('/')
def main() :
    msg=request.args.get('msg')
    words = list(db.words.find({}, {"_id" : False}))
    return render_template("index.html", words=words, msg=msg)


@app.route('/detail/<keyword>')
def detail(keyword) :
    status_receive = request.args.get("status_give")
    r = requests.get(f"https://owlbot.info/api/v4/dictionary/{keyword}",
                     headers={"Authorization" : "Token 8e2f99bd6d20e9eabbbb6d4a5026da855b0d5a53"})
    if r.status_code !=200:
        return redirect(url_for("main", msg="없는 단어입니다."))
    result = r.json()
    print(result)
    return render_template("detail.html", word=keyword, result=result, status=status_receive)


@app.route('/api/save_word', methods=['POST'])
def save_word() :
    word_receive = request.form['word_give']
    definition_receive = request.form['definition_give']
    doc = {"word" : word_receive, "definition" : definition_receive}
    db.words.insert_one(doc)
    return jsonify({'result' : 'success', 'msg' : f'단어 {word_receive} 저장'})


@app.route('/api/delete_word', methods=['POST'])
def delete_word() :
    word_receive = request.form["word_give"]
    db.words.delete_one({"word" : word_receive})
    return jsonify({'result' : 'success', 'msg' : f'단어 {word_receive} 삭제'})


@app.route('/api/get_exs', methods=['GET'])
def get_exs():
    word_receive = request.args.get("word_give")
    examples = list(db.example.find({"word":word_receive}, {"_id" : False}))
    return jsonify({'result': 'success', "examples":examples})

@app.route('/api/save_ex', methods=['POST'])
def save_ex():
    new_ex=request.form["example_give"]
    word_receive = request.form["word_give"]
    db.example.insert_one({"word":word_receive, "example": new_ex})
    return jsonify({'result' : 'success', 'msg' : f'example "{new_ex}" saved'})


@app.route('/api/delete_ex', methods=['POST'])
def delete_ex():
    word_receive= request.form['word_give']
    number_receive = request.form['number_give']
    example = list(db.example.find({"word" : word_receive}))[int(number_receive)]["example"]
    print(word_receive, example)
    db.example.delete_one({"word" : word_receive, "example" : example})
    return jsonify({'result' : 'success', 'msg' : f'example #{number_receive} of "{word_receive}" deleted'})


if __name__ == '__main__' :
    app.run('0.0.0.0', port=5000, debug=True)
