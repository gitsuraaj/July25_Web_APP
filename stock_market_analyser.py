import yfinance as yf
import streamlit as st

#https://ranaroussi.github.io/yfinance/





st.header("Stock market Analyser")

#text input

ticker_symbol = st.text_input("Enter Stock Ticker (e.g. AAPL, GOOGL, TSLA)", "AAPL")

ticker_data = yf.Ticker(ticker_symbol)



import datetime

col1, col2= st.columns(2)

with col1:
    start_date = st.date_input("Enter Start Date", datetime.date(2019, 1, 1))

with col2:
    end_date = st.date_input("Enter End Date", datetime.date(2022, 12, 31))

ticker_df= ticker_data.history(start= start_date,end=end_date)


st.write("SHOWING DETAILS FOR:")
st.write(ticker_symbol)
st.dataframe(ticker_df)


st.write("Closing Price Chart")
st.line_chart(ticker_df['Close'])

st.write("Volume Chart")
st.line_chart(ticker_df['Volume'])