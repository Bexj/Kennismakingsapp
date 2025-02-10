from langchain_openai import AzureChatOpenAI
from langchain.schema import HumanMessage, SystemMessage
from src.kennismakingsapp.config import (
    AZURE_OPENAI_API_KEY,
    AZURE_OPENAI_ENDPOINT,
    AZURE_OPENAI_DEPLOYMENT,
    AZURE_OPENAI_API_VERSION,
)

# Initialize LangChain Azure OpenAI model
llm = AzureChatOpenAI(
    azure_endpoint=AZURE_OPENAI_ENDPOINT,
    api_key=AZURE_OPENAI_API_KEY,
    deployment_name=AZURE_OPENAI_DEPLOYMENT,
    api_version=AZURE_OPENAI_API_VERSION,
)

def chat_with_gpt(user_input: str) -> str:
    """Sends a user message to Azure OpenAI and returns the response."""
    messages = [
        SystemMessage(content="You are a helpful AI assistant."),
        HumanMessage(content=user_input)
    ]
    response = llm.invoke(messages)
    return response.content
