# Step 1: Import required modules from LangChain for conversation handling and AWS Bedrock
from langchain.chains import ConversationChain  # Handles conversation flow
from langchain.memory import ConversationSummaryBufferMemory  # Provides memory management for conversations
from langchain_aws import ChatBedrock  # AWS Bedrock integration for large language models (LLMs)

# Step 2a: Define a function to set up the connection with the Amazon Bedrock model
def demo_chatbot():
    demo_llm = ChatBedrock(
       credentials_profile_name='default',  # AWS credentials profile to use
       model_id='anthropic.claude-3-haiku-20240307-v1:0',  # The specific Bedrock model to use
       model_kwargs={
           "max_tokens": 300,  # Limit the response to 300 tokens
           "temperature": 0.1,  # Control randomness in the output (lower value = more focused response)
           "top_p": 0.9,  # Sampling method parameter (higher values allow for more varied responses)
           "stop_sequences": ["\n\nHuman:"]  # Define stopping conditions in the conversation
       }
    )
    return demo_llm  # Return the LLM instance

# Step 2b: Optionally, test the LLM with a sample input using the invoke method
    # To test, you can use this line instead of running the conversation chain:
    # response = demo_llm.invoke(input_text="Hi, what is the temperature in New York in January?")
    # print(response)

# Step 3: Define a function to initialize memory with a token limit using the Bedrock LLM
def demo_memory():
    llm_data = demo_chatbot()  # Fetch the LLM model from the function
    memory = ConversationSummaryBufferMemory(llm=llm_data, max_token_limit=300)  # Create memory buffer with a max token limit
    return memory  # Return the memory instance

# Step 4: Define a function to manage the conversation chain using input text and memory
def demo_conversation(input_text, memory):
    llm_chain_data = demo_chatbot()  # Get the Bedrock LLM instance
    llm_conversation = ConversationChain(llm=llm_chain_data, memory=memory, verbose=True)  # Create a conversation chain with memory

    # Step 5: Invoke the conversation chain and return the chatbot's response
    chat_reply = llm_conversation.invoke(input_text)  # Use invoke to process the input text
    return chat_reply['response']  # Return the generated response from the conversation

# References:
# - For more information on LangChain and AWS Bedrock, visit: 
#   https://python.langchain.com/v0.1/docs/integrations/llms/bedrock/

# Required installations:
# pip install -U langchain-aws  # Install LangChain AWS integration
# pip install anthropic  # Install the Anthropic API for using Claude models
