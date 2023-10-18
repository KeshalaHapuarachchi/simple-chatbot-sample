# simple-chatbot-using the OpenAI API and Streamlit

Streamlit Documentation: https://docs.streamlit.io/ 


**Setting Up OpenAI API Key**: This code uses the OpenAI API to interact with their language models. It requires an API key for authentication. You should replace 'YOUR_API_KEY_HEREsk-Or5TMLjEynTNP931vBy9T3BlbkFJnBHKqVEaEzxhwvJ7Yn3q' with your actual OpenAI API key.
**Streamlit App Setup**: The Streamlit app is initiated with the title "Simple Chatbot".
**Chat with Bot Function (chat_with_bot())**: This function is responsible for interacting with the chatbot. It sends a series of messages (in this case, a system message and a user message) to the OpenAI API and retrieves the response from the chatbot.

**Main Streamlit App**: user_input is a text input field where the user can type their messages.
When the user inputs a message (if user_input:), it triggers the chatbot interaction.
The messages variable is a list containing two dictionaries:
The first dictionary sets the role as "system" and provides a content message to indicate that the user is interacting with a helpful assistant.
The second dictionary sets the role as "user" and takes the user's input.
The chat_with_bot() function is called with these messages.
The bot's response is displayed in a text area labeled "Bot".

![image](https://github.com/KeshalaHapuarachchi/simple-chatbot-sample/assets/105196447/5a3227cd-e1e0-41e2-b12b-9193ac86e162)


Thank You...
