
import streamlit as st
import pandas as pd

st.header("_Streamlit_ is :blue[cool] :sunglasses:")
st.write("This is the coolest webapp!")
st.badge("Web App!")

df= pd.read_csv('/Users/apple/Desktop/July25_Web_APP/cars24-car-price.csv')

st.dataframe(df)

#https://docs.streamlit.io/develop/api-reference/widgets
agree = st.checkbox("Am I Awesome?")

if agree:
    st.write("You have a good taste!")


st.button("Reset", type="primary")

if st.button("Say hello"):
    st.write("You clicked on the button")
else:
    st.write("Button is untouched")
