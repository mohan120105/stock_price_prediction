import streamlit as st
import yfinance as yf
import numpy as np
import pickle

# Load the trained model
with open('stock_price_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Streamlit app title
st.title('Stock Price Prediction App')

# Predefined list of stock tickers
predefined_stocks = [
    "RELIANCE.NS", "TCS.NS", "HDFCBANK.NS", "INFY.NS", "HINDUNILVR.NS", 
    "ICICIBANK.NS", "KOTAKBANK.NS", "SBIN.NS", "BAJFINANCE.NS", "HCLTECH.NS",
    "BHARTIARTL.NS", "ASIANPAINT.NS", "ITC.NS", "HDFCLIFE.NS", "AXISBANK.NS",
    "LT.NS", "HDFC.NS", "MARUTI.NS", "SUNPHARMA.NS", "ULTRACEMCO.NS",
    "WIPRO.NS", "ONGC.NS", "NESTLEIND.NS", "POWERGRID.NS", "TATAMOTORS.NS",
    "ADANIPORTS.NS", "INDUSINDBK.NS", "NTPC.NS", "JSWSTEEL.NS", "BAJAJ-AUTO.NS",
    "TITAN.NS", "BPCL.NS", "GRASIM.NS", "HEROMOTOCO.NS", "TECHM.NS",
    "DRREDDY.NS", "HINDALCO.NS", "TATASTEEL.NS", "COALINDIA.NS", "IOC.NS",
    "VEDL.NS", "BRITANNIA.NS", "EICHERMOT.NS", "UPL.NS", "GAIL.NS",
    "SHREECEM.NS", "CIPLA.NS", "M&M.NS", "DIVISLAB.NS", "SBILIFE.NS"
]

# Dropdown to select or enter the stock ticker symbol
stock_ticker = st.selectbox("Select or enter the stock ticker symbol:", predefined_stocks + ["Enter Custom Ticker"])

# User input for custom stock ticker
if stock_ticker == "Enter Custom Ticker":
    stock_ticker = st.text_input("Enter the stock ticker symbol:")

# User input for history period
history_period = st.selectbox("Select history period:", ["1d", "2d", "5d", "1mo", "3mo", "6mo", "1y"])

# Button to trigger prediction
if st.button("Predict Stock Price"):
    # Function to validate the stock ticker
    def is_valid_ticker(ticker):
        try:
            data = yf.Ticker(ticker)
            df = data.history(period='1d')
            return not df.empty
        except:
            return False

    # Ensure the user has selected or entered a stock ticker
    if stock_ticker:
        # Check if the selected stock ticker is valid
        if is_valid_ticker(stock_ticker):
            # Fetch the data for the selected stock ticker
            data = yf.Ticker(stock_ticker)
            df = data.history(period=history_period)

            # Extract the required values
            prev_close = df['Close'].iloc[-1]
            open_price = df['Open'].iloc[-1]
            high = df['High'].iloc[-1]
            low = df['Low'].iloc[-1]
            last = df['Close'].iloc[-1]
            vwap = (df['Volume'] * df['Close']).sum() / df['Volume'].sum()
            volume = df['Volume'].iloc[-1]

            # Prepare the feature array for prediction
            features = np.array([[prev_close, open_price, high, low, last, vwap, volume]])
            # Predict the closing price
            predicted_close = model.predict(features)

            # Display the fetched real-time data
            st.subheader(f'Real-time Data for {stock_ticker}:')
            st.write(f"Prev Close: {prev_close}")
            st.write(f"Open: {open_price}")
            st.write(f"High: {high}")
            st.write(f"Low: {low}")
            st.write(f"Last: {last}")
            st.write(f"VWAP: {vwap}")
            st.write(f"Volume: {volume}")

            # Display the predicted closing price
            st.subheader('Predicted Close Price:')
            st.write(f"{predicted_close[0]:.2f}")
        else:
            st.error("Invalid stock ticker symbol. Please enter a valid stock ticker symbol.")
    else:
        st.warning("Please select or enter a stock ticker symbol to get predictions.")
