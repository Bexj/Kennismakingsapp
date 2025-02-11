from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate
from langchain_openai import AzureChatOpenAI
from src.kennismakingsapp.document_loader import load_joren_documents
from src.kennismakingsapp.config import (
    AZURE_OPENAI_API_KEY,
    AZURE_OPENAI_ENDPOINT,
    AZURE_OPENAI_DEPLOYMENT,
    AZURE_OPENAI_API_VERSION,
)

llm = AzureChatOpenAI(
    azure_endpoint=AZURE_OPENAI_ENDPOINT,
    api_key=AZURE_OPENAI_API_KEY,
    deployment_name=AZURE_OPENAI_DEPLOYMENT,
    api_version=AZURE_OPENAI_API_VERSION,
)

JOREN_DOCUMENT_KNOWLEDGE = load_joren_documents()

prompt_template = """
You are a chatbot trained to help users get to know Joren.
Joren is a student in Applied Computer Science specializing in AI & Data at UCLL Leuven.
They have a passion for data engineering, AI integration in business, and building intelligent applications.
He works in the warehouse of Aldi at night on weekends, and it is very intensive labor.

Here is additional information:
{knowledge}

{chat_history}

User: {input}
AI:"""

conversation_memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

conversation = ConversationChain(
    llm=llm,
    memory=conversation_memory,
    prompt=PromptTemplate(input_variables=["input"], template=prompt_template.format(knowledge=JOREN_DOCUMENT_KNOWLEDGE, chat_history="{chat_history}", input="{input}")),
    verbose=False,
)

def chat_with_gpt(user_input: str) -> str:
    """Sends user input to Azure OpenAI while maintaining conversation history."""
    response = conversation.predict(input=user_input)
    return response
