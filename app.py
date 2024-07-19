from flask import Flask, request, jsonify, render_template
from transformers import pipeline
import requests
import os
from dotenv import load_dotenv

app = Flask(__name__)

# Load environment variables from .env file
load_dotenv()
ALPHA_VANTAGE_API_KEY = os.getenv('ALPHA_VANTAGE_API_KEY')

# Question Answering Pipeline
question_answerer = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")

# Function to fetch stock price
def get_stock_price(symbol, api_key):
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=1min&apikey={api_key}'
    response = requests.get(url)
    data = response.json()
    return data

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask_question():
    data = request.get_json()
    question = data.get('question')
    context = data.get('context', "This is a sample context about stock prices and financial information.")
    answer = question_answerer(question=question, context=context)['answer']
    return jsonify({'answer': answer})

@app.route('/stock', methods=['POST'])
def get_stock():
    data = request.get_json()
    symbol = data.get('symbol')
    stock_data = get_stock_price(symbol, ALPHA_VANTAGE_API_KEY)
    return jsonify(stock_data)

@app.route('/compare', methods=['POST'])
def compare_stocks():
    data = request.get_json()
    symbols = data.get('symbols', [])
    stock_data = {}
    for symbol in symbols:
        stock_data[symbol] = get_stock_price(symbol, ALPHA_VANTAGE_API_KEY)
    return jsonify(stock_data)

if __name__ == '__main__':
    app.run(debug=True)
