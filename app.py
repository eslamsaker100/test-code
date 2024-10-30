import streamlit as st

# Title for the app
st.title("Hello, Streamlit!")

# Input section
name = st.text_input("What's your name?")

# Button to submit
if st.button("Submit"):
    st.write(f"Hello, {name}!")

# Add a slider
age = st.slider("How old are you?", 0, 100, 25)
st.write(f"You are {age} years old.")
