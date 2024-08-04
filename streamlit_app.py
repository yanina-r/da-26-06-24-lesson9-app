import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt 
from datetime import datetime

st.title('Lesson 9 app')
st.sidebar.header('Enter your stock symbol')

stock_symbol1 = st.sidebar.text_input('Enter the stock symbol (for example, AAPL for Apple)')
stock_symbol2 = st.sidebar.text_input('Enter the stock symbol of another promotion (for example, AMZN for Amazon)')

start_year, end_year = st.sidebar.slider(
    'Select the range of years:',
    min_value=2000, max_value=datetime.now().year, value=(2015, 2020)
)

if stock_symbol1 and stock_symbol2:
    start_date = f"{start_year}-01-01"
    end_date = f"{end_year}-12-31"
    stock_data1 = yf.download(stock_symbol1, start=start_date, end=end_date)
    stock_data2 = yf.download(stock_symbol2, start=start_date, end=end_date)
    
    if not stock_data1.empty and not stock_data2.empty:
        st.write('Finance data for the first share:', stock_data1.head())
        st.write('Finance data for another promotion:', stock_data2.head())
        
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(stock_data1.index, stock_data1['Close'], label=f'Share price {stock_symbol1}')
        ax.plot(stock_data2.index, stock_data2['Close'], label=f'Share price {stock_symbol2}')
        ax.set_title('Share price chart')
        ax.set_xlabel('Date')
        ax.set_ylabel('Share price (USD)')
        ax.grid(True)
        ax.legend()

        st.pyplot(fig)
    else:
        st.error('Data not found. Enter the correct symbol.')
