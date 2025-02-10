from langchain_openai import AzureChatOpenAI
from langchain.schema import HumanMessage, SystemMessage
from src.kennismakingsapp.document_loader import load_joren_documents
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

JOREN_DOCUMENT_KNOWLEDGE = load_joren_documents()

def chat_with_gpt(user_input: str) -> str:
    """Sends a user message to Azure OpenAI and returns the response."""
    messages = [
        SystemMessage(content="You are a chatbot trained to help users get to know Joren. Here is some information about Joren: "
                              "Joren is a student in Applied Computer Science specializing in AI & Data at UCLL Leuven. "
                              "They have a passion for data engineering, AI integration in business, and building intelligent applications. "
                              "He works in the warehouse of Aldi at night in the weekends, it is very intensive labor"
                              f"here is information about Joren: {JOREN_DOCUMENT_KNOWLEDGE}"
                            ),
        HumanMessage(content=user_input)
    ]
    response = llm.invoke(messages)
    return response.content
