import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime

# Заголовок додатку
st.title('Lesson 9 app')

# Введення символів акцій
stock_symbol1 = st.sidebar.text_input('Enter the stock symbol (for example, AAPL for Apple)')
stock_symbol2 = st.sidebar.text_input('Enter the stock symbol of another promotion (for example, AMZN for Amazon)')

# Вибір діапазону дат
start_year, end_year = st.sidebar.slider(
    'Select the range of years:',
    min_value=2000, max_value=datetime.now().year, value=(2015, 2020)
)

start_date = f"{start_year}-01-01"
end_date = f"{end_year}-12-31"

# Кнопка для завантаження даних
if st.sidebar.button('Fetch Data'):
    if stock_symbol1 and stock_symbol2:
        with st.spinner('Fetching data...'):
            # Завантаження даних
            stock_data1 = yf.download(stock_symbol1, start=start_date, end=end_date)
            stock_data2 = yf.download(stock_symbol2, start=start_date, end=end_date)

        # Перевірка, чи не порожні дані
        if not stock_data1.empty and not stock_data2.empty:
            # Виведення таблиць даних
            st.write('### Finance Data')
            st.dataframe(stock_data1.head())
            st.dataframe(stock_data2.head())
            
            # Вибір акцій для перегляду графіків
            selected_stock = st.sidebar.selectbox(
                'Select stock to view chart:',
                options=[stock_symbol1, stock_symbol2]
            )

            # Вибір даних для графіку на основі вибраного символу
            if selected_stock == stock_symbol1:
                data_to_plot = stock_data1
            else:
                data_to_plot = stock_data2

            # Виведення графіків
            st.write(f'### Stock Price Chart for {selected_stock}')

            fig, ax = plt.subplots(figsize=(10, 6))
            ax.plot(data_to_plot.index, data_to_plot['Close'], label=f'Share price {selected_stock}')
            ax.set_title(f'Stock Price for {selected_stock}')
            ax.set_xlabel('Date')
            ax.set_ylabel('Price (USD)')
            ax.grid(True)
            ax.legend()
            
            st.pyplot(fig)
            
            # Лінійний графік для обох акцій
            st.write('### Line Chart of Closing Prices')
            df_combined = pd.DataFrame({
                'Date': stock_data1.index,
                'Stock 1 Close': stock_data1['Close'],
                'Stock 2 Close': stock_data2['Close']
            }).set_index('Date')
            
            st.line_chart(df_combined)

            # Відображення зображення
            st.image('/workspaces/da-26-06-24-lesson9-app/img/thanks.jpeg', use_column_width=True)
            
            # Виведення HTML-коду з посиланням на Nasdaq
            html_code = """
            <div style="padding: 10px; background-color: #f0f0f0;">
                <h2>Explore NASDAQ Stocks</h2>
                <p>Visit the following link to explore NASDAQ stocks:</p>
                <a href="https://www.nasdaq.com/market-activity/stocks/screener" target="_blank">NASDAQ Stock Screener</a>
            </div>
            """
            st.components.v1.html(html_code, height=150)

            # Показати анімацію з кульками
            st.balloons()
            
        else:
            st.error('Data not found for one or both of the symbols. Please enter valid symbols.')
    else:
        st.warning('Please enter both stock symbols.')
