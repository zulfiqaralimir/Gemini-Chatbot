# Using Streamlit
import streamlit as st
import google.generativeai as genai

# Configure the Google Generative AI API

API_KEY = "AIzaSyALQx-26oVWs-Yng9FJ1E3awuTOXVUKOOg"
genai.configure(api_key=API_KEY)

# Initialize the model

model = genai.GenerativeModel('gemini-1.5-flash')

def getResponseFromModel(user_input):
    response = model.generate_content(user_input)
    return response.text

# Streamlit UI
st.title("Gemini Chatbot")

# Get user input through a text input box
user_input = st.text_input("Enter your Prompt:")

# Create a button that when clicked, will generate the response
if st.button("Get Response"):
    if user_input:
        output = getResponseFromModel(user_input)
        st.write(f"Chatbot Response: {output}")
    else:
        st.write("Please enter a prompt.")

# user_input = input("Enter your Prompt = ")
# output = getResponseFromModel(user_input)
# print(output)

