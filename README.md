# Stock and Investment Chatbot
## Overview and Use Cases
The Stock and Investment Chatbot is designed to assist users in obtaining information about stock prices and financial data. It also provides investment recommendations and analysis based on user queries. The chatbot can answer questions, fetch real-time stock prices, and compare multiple stock symbols.

### Use Cases
- **Query Stock Information**: Users can request current stock prices for individual symbols.
- **Compare Stock Prices**: Users can compare prices of multiple stock symbols.
- **Answer Financial Questions**: Users can ask general financial or stock-related questions to receive contextual answers.
## Technologies and Tools
- **Hugging Face Transformers**: Used to create the question-answering model and generate contextual answers.
- **SpaCy**: Utilized for natural language processing tasks (if applicable).
- **Alpha Vantage API**: Provides real-time stock prices and financial data.
- **Generative AI**: Used to create sample data and train models (if applicable).

## Embedding Techniques

Embedding is a technique to convert textual data into numerical vectors that represent the semantic meaning of words or phrases. For this project, BERT (Bidirectional Encoder Representations from Transformers) is used to create embeddings. BERT transforms text into vectors that capture contextual relationships between words.


## Hugging Face Components Used
Question Answering Pipeline: Utilizes the distilbert-base-cased-distilled-squad model to answer user questions based on provided context.

## API Usage
Alpha Vantage API
The Alpha Vantage API is used to fetch real-time stock price data. To use the API, you need an API key which can be obtained by signing up on the Alpha Vantage website.

## Future Enhancements
Enhanced UI: Improve the user interface for better user experience.
Additional APIs: Integrate more APIs for broader financial data coverage.
Advanced Analytics: Implement advanced data analytics features for deeper market insights.
