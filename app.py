import streamlit as st
from myproject import greet

st.title("Hello World Streamlit App")

name = st.text_input("Enter your name:", "World")

if st.button("Greet"):
    message = greet(name)
    st.success(message)
    st.balloons()