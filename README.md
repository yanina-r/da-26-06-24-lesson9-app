# 🎈 Lesson 9 app

I created a simple Streamlit app!

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://da-26-06-24-9-app.streamlit.app/)

### Web Application for Stock Analysis
Built with Streamlit, this web application allows users to download stock data, view it as tables and graphs, and interact with various visualizations for analysis

## Application interface
The main page of the application with text boxes for entering stock symbols, sliders for selecting a date range, a button for uploading data and other controls.
![Screenshot](img/Знімок%20екрана%202024-08-04%20о%2018.35.14.png)

## Description of the Streamlit methods
1.st.text_input
  - Used to enter stock symbols (eg AAPL for Apple). The user can enter up to two stock symbols for further analysis.
2.st.slider
 - Allows users to select a range of years to analyze stock data. The selected years are used for data loading.
3.st.button
 - A button that starts the data download process for the selected stock symbols.
4. st.spinner
 - Shows a spinner (loading indicator) when retrieving stock data. Helps the user understand that data is being loaded.
5. st.dataframe
 - Displays stock data in the form of tables. Allows users to view stock data in a tabular format.
6.st.selectbox
  - Allows you to select a stock to view the chart. The selection affects what data is shown in the graph.
7. st.line_chart
 - Displays a line graph of closing prices for selected stocks. Helps to visualize changes in stock price over time.
8.st.image
 - Displays an image. Can be used to add illustrations or additional content.
9. st.balloons
   - Shows a balloon animation after the data download is complete. Adds an effect to a web application.
10.st.components.v1.html
 - Displays HTML code with a link to Nasdaq for additional resources. Can be used to embed external content.
