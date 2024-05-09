from flask import Flask, request, jsonify
from bs4 import BeautifulSoup
import requests
import nltk
from nltk.tokenize import sent_tokenize

app = Flask(__name__)

@app.route('/get_answer', methods=['POST'])
def get_answer():
    data = request.get_json()
    url = data['url']
    question = data['question']

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    text = soup.get_text()
    sentences = sent_tokenize(text)

    for sentence in sentences:
        if question in sentence:
            return jsonify({'answer': sentence})

    return jsonify({'answer': "I don't know the answer"})

if __name__ == '__main__':
    app.run(debug=True)
