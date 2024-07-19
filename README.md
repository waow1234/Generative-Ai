# Stock and Investment Chatbot
## Overview and Use Cases
The Stock and Investment Chatbot is designed to assist users in obtaining information about stock prices and financial data. It also provides investment recommendations and analysis based on user queries. The chatbot can answer questions, fetch real-time stock prices, and compare multiple stock symbols.

### Use Cases
- **Query Stock Information**: Users can request current stock prices for individual symbols.
- **Compare Stock Prices**: Users can compare prices of multiple stock symbols.
- **Answer Financial Questions**: Users can ask general financial or stock-related questions to receive contextual answers.
## Technologies and Tools
## AI Techniques and Tools
-Transformers: Utilizes the pipeline function from the Hugging Face Transformers library for question answering.
-Pre-trained Model: distilbert-base-cased-distilled-squad model from Hugging Face for efficient question answering.
## Stock Price Retrieval
-Alpha Vantage API: Fetches real-time stock data.
##Flask
-Flask Framework: Handles routing and server-side logic.
-Jinja2: Renders HTML templates.
## Environment Management
-python-dotenv: Loads environment variables from a .env file for secure API key management.
## Embedding Explanation
## Question Answering Pipeline
The question answering functionality uses the Hugging Face Transformers library, specifically the pipeline method with the question-answering task. The model used is distilbert-base-cased-distilled-squad, which is a distilled version of BERT for question answering tasks, providing a balance between performance and speed.
## Stock Price Retrieval Function
The function get_stock_price fetches stock prices using the Alpha Vantage API. It constructs a URL with the provided stock symbol and API key, makes a GET request, and returns the JSON response.

## Hugging Face Components Used
Question Answering Pipeline: Utilizes the distilbert-base-cased-distilled-squad model to answer user questions based on provided context.

## API Usage
Alpha Vantage API
The Alpha Vantage API is used to fetch real-time stock price data. To use the API, you need an API key which can be obtained by signing up on the Alpha Vantage website.
