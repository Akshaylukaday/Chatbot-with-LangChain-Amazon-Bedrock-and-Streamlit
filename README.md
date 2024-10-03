# Chatbot with LangChain Amazon Bedrock and Streamlit

This repository contains code to build a conversational chatbot using LangChain, Amazon Bedrock, and Streamlit. The chatbot leverages AWS Bedrock for advanced language models and LangChain for memory management, allowing the bot to maintain context throughout the conversation.

Prerequisites

Before getting started, ensure that the following tools and libraries are installed on your local machine:
1. Visual Studio Code (VS Code)

    Download and install VS Code as your code editor.

2. AWS CLI (Command Line Interface)

    Install AWS CLI by following the official AWS documentation.
    Run the following command to verify the installation:

    bash

aws --version

Configure your AWS CLI with the required IAM role:

bash

    aws configure

3. Anaconda or Python Environment

    Use Anaconda or a Python virtual environment to manage dependencies. Install Anaconda from the official site or set up a virtual environment:

    bash

    python -m venv env
    source env/bin/activate  # On macOS/Linux
    .\env\Scripts\activate   # On Windows

4. Install Python Dependencies

    Use the following command to install the required libraries:

    bash

    pip install streamlit langchain boto3 langchain-aws anthropic

5. Set Up AWS Profile

    Ensure you have an AWS profile configured with necessary permissions to access Bedrock. If not, configure it:

    bash

    aws configure --profile your_profile_name

Project Setup Instructions
Step 1: Clone the Repository

    Clone the GitHub repository to your local machine:

    bash

  gh repo clone Akshaylukaday/Chatbot-with-LangChain-Amazon-Bedrock-and-Streamlit
  cd Chatbot-with-LangChain-Amazon-Bedrock-and-Streamlit

Step 2: Run Streamlit Application

    Run the Streamlit app to start the chatbot interface:

    bash

    streamlit run app.py

Step 3: Modify Configuration

    If needed, modify the chatbot model or memory configurations inside chatbot_backend.py as per your use case:

    python

    model_id = 'anthropic.claude-3-haiku-20240307-v1:0'
    credentials_profile_name = 'your_aws_profile'

File Structure

bash

├── app.py                     # Main Streamlit application
├── backend.py          # Backend functions for LLM and memory management
├── requirements.txt            # Python dependencies
└── README.md                   # This documentation

Usage Example

Once the chatbot is running, you can interact with it via the Streamlit UI. It will preserve the conversation context using LangChain's memory and generate responses via AWS Bedrock’s Claude model.
Key Files and Code Explanation

    app.py:
        The main entry point for the Streamlit application. It handles the user interface (UI) and interaction with the chatbot.
    chatbot_backend.py:
        Contains functions to initialize the Bedrock model and manage conversation memory using LangChain.

Dependencies

    LangChain: A framework for building applications with LLMs. It provides memory support for managing conversation history.
    Amazon Bedrock: AWS’s service for accessing large language models like Claude from Anthropic.
    Streamlit: A Python framework for building web applications easily. It is used here for building the chatbot UI.

Installation Commands

To quickly set up the environment, you can install the dependencies by running:

bash

pip install -r requirements.txt


Here’s how it works:

    LangChain: This framework makes it easy to use powerful language models in a flexible way. One of its best features is the ability to remember past interactions, so the chatbot can keep track of conversations.

    💡 For example: If a customer asks for recommendations based on what they bought before, the chatbot can recall that information to provide tailored suggestions.

    Amazon Bedrock: This service gives you easy access to advanced language models like Claude from Anthropic. Developers can adjust the model’s settings to control how responses come across.

    💡 For example: By setting the response temperature low, the chatbot can ensure it gives consistent and factual answers, which is essential for handling FAQs.

    Streamlit: This tool makes it simple to create interactive web applications. It provides a user-friendly interface for customers to chat with the bot directly.

    💡 For example: Customers can type in questions like “What’s the status of my order?” and get quick, relevant answers based on previous interactions.

Why This Matters:

By combining these technologies, businesses can create chatbots that offer personalized and engaging experiences for their customers.

License

This project is licensed under the MIT License.

This documentation covers everything needed to set up and run the chatbot. It provides an overview of the required tools, installation steps, and project structure, making it easy for users to get started.
