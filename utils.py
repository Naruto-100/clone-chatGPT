from langchain.chains import ConversationChain
from langchain_openai import ChatOpenAI
#from langchain.memory import ConversationBufferMemory

# import os


def get_chat_response(prompt, memory, openai_api_key):
    model = ChatOpenAI(model="gpt-3.5-turbo", openai_api_key=openai_api_key, openai_api_base="https://api.aigc369.com/v1")
    chain = ConversationChain(llm=model, memory=memory)

    response = chain.invoke({"input": prompt})
    return response["response"]

# memory = ConversationBufferMemory(return_messages=True)
#
# print(get_chat_response("什么是量子云？", memory, os.getenv("OPENAI_API_KEY")))
# print(get_chat_response("我刚问的是什么学科的题？", memory, os.getenv("OPENAI_API_KEY")))
# 注释部分用于测试get_chat_response
