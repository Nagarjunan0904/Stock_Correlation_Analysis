import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import yfinance as yf
import matplotlib.pyplot as plt

# fetching the Historical Data
def fetch_stock_data(tickers, start_date, end_date, interval='1d'):
    data = {}
    for ticker in tickers:
        stock = yf.Ticker(ticker)
        hist = stock.history(start=start_date, end=end_date, interval=interval)
        data[ticker] = hist['Close']
    return pd.DataFrame(data)

# Visualizing using Streamlit app
st.title("Stock Correlation Analysis")
uploaded_file = st.file_uploader("Upload Stock Tickers CSV", type="csv")

if uploaded_file is not None:
    tickers = pd.read_csv(uploaded_file).columns[1:].tolist()
    stock_data = fetch_stock_data(tickers, "2020-01-01", "2023-01-01")

    # Display Correlation Heatmap
    st.write("Correlation Heatmap:")
    fig, ax = plt.subplots(figsize=(10, 8))  # Create a figure for the heatmap
    sns.heatmap(stock_data.corr(), annot=True, ax=ax, cmap="coolwarm")
    st.pyplot(fig)  # Render the Matplotlib figure in Streamlit

