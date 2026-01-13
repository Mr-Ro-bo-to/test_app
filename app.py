import streamlit as st
from myproject import greet

st.title("Have a wonderful day 😘")

name = st.text_input("Enter your name:", "Marie")

if st.button("Greet"):
    message = greet(name)
    st.success(message)
    st.balloons()