import streamlit as st
import openai

# Set up your OpenAI API key
openai.api_key = 'YOUR_API_KEY_HEREsk-Or5TMLjEynTNP931vBy9T3BlbkFJnBHKqVEaEzxhwvJ7Yn3q'  

# Streamlit app title and header
st.title("Simple Chatbot")

# Function to interact with the chatbot
def chat_with_bot(messages):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    return response.choices[0].message['content']

# Main Streamlit app
user_input = st.text_input("You:", "")

if user_input:
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": user_input}
    ]
    bot_response = chat_with_bot(messages)
    st.text_area("Bot:", bot_response, readonly=True)
