# Import necessary libraries for the chatbot
import streamlit as st
import chatbot_backend as test  # Import your custom chatbot backend as 'test'

# Set the title for the chatbot in the Streamlit UI
st.title("Hi, This is Chatbot Akshay's Sevak 😎")  # Modify the title as per your preference

# Initialize LangChain memory for the chatbot and store it in Streamlit's session state
if 'memory' not in st.session_state:  # Check if 'memory' isn't already in session state
    st.session_state.memory = test.test_memory()  # Initialize and store memory using the backend function

# Initialize chat history in session state to store conversation logs
if 'chat_history' not in st.session_state:  # Check if 'chat_history' isn't already in session state
    st.session_state.chat_history = []  # Initialize chat history as an empty list

# Display previous chat history in the chat window
for message in st.session_state.chat_history:  # Loop through the chat history
    with st.chat_message(message["role"]):  # Identify whether it's the user's or assistant's message
        st.markdown(message["text"])  # Render each chat message

# Display an input box for the user to type their message
input_text = st.chat_input("Powered by Bedrock and Claude")  # Chat input placeholder text
if input_text:  # If the user has entered a message

    # Display user's input message in the chat window
    with st.chat_message("user"):  # Mark it as a user message
        st.markdown(input_text)  # Display the user's message

    # Add user's message to the chat history
    st.session_state.chat_history.append({"role": "user", "text": input_text})

    # Generate chatbot response using backend function (ConversationChain)
    chat_response = test.test_conversation(input_text=input_text, memory=st.session_state.memory)

    # Display chatbot's response in the chat window
    with st.chat_message("assistant"):  # Mark it as an assistant message
        st.markdown(chat_response)  # Display the assistant's response

    # Add the chatbot's response to the chat history
    st.session_state.chat_history.append({"role": "assistant", "text": chat_response})
