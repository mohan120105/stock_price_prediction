# Real-Time Stock Price Prediction App

## Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Technologies Used](#technologies-used)
6. [Contributing](#contributing)


## Introduction
This project is a real-time stock price prediction app built with Streamlit. 
The app allows users to select or input a stock ticker symbol and predict the closing price using 
a pre-trained machine learning model. The app also fetches and displays real-time stock data.

## Features
- Predicts the closing price of selected stocks
- Fetches and displays real-time stock data
- Supports a predefined list of stock tickers and custom ticker input
- User-friendly interface with Streamlit

## Installation
Follow these steps to get the project up and running on your local machine:

1. **Clone the repository:**
    ```bash
    git clone https://github.com/79mohan7981/stock_price_prediction.git
    cd stock_price_prediction
    ```

2. **Create and activate a virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages:**
    ```bash
    pip install streamlit yfinance numpy scikit-learn pandas
    ```

4. **Download or create the trained model:**
    - Ensure you have a `stock_price_model.pkl` file in the project directory.
    - If you don't have one, train a model and save it as `stock_price_model.pkl`.

## Usage
1. **Run the Streamlit app:**
    ```bash
    streamlit run app.py
    ```

2. **Access the app:**
    Open your web browser and go to `http://localhost:8501`.

3. **Use the interface to select or enter a stock ticker symbol, select the history period, and get predictions:**

## Technologies Used
- **Programming Language:** Python
- **Web Framework:** Streamlit
- **Data Fetching:** yfinance
- **Machine Learning Libraries:** scikit-learn, numpy, pandas
- **Model Persistence:** pickle

## Contributing
Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature-branch`)
5. Create a new Pull Request

