from langchain.prompts import (
    ChatPromptTemplate,
    PromptTemplate,
    SystemMessagePromptTemplate,
    AIMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)
from langchain.llms import OpenAI
import os
from langchain.chains import LLMChain
os.environ["http_proxy"] = "http://127.0.0.1:1080"
os.environ["https_proxy"] = "http://127.0.0.1:1080"
os.environ["OPENAI_API_KEY"] = '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'
#第一种构建方法
template="You are a helpful assistant that translates {input_language} to {output_language}."
system_message_prompt = SystemMessagePromptTemplate.from_template(template)
human_template = "{text}"
human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)
#第二种，在外部创建一个PromptTemplate，然后将其传递进去
prompt = PromptTemplate(
    template="You are a helpful assistant that translates {input_language} to {output_language}.",
    input_variables=["input_language", "output_language"],
)
system_message_prompt_2 = SystemMessagePromptTemplate(prompt=prompt)

assert system_message_prompt == system_message_prompt_2
#从一个或多个MessagePromptTemplates构建一个ChatPromptTemplate。
chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])

# get a chat completion from the formatted messages
chat_prompt.format_prompt(input_language="English", output_language="French", text="I love programming.").to_messages()

chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])

# get a chat completion from the formatted messages
chat_prompt.format_prompt(input_language="English", output_language="French", text="I love programming.").to_messages()

llm = OpenAI(temperature=0.9)
chain=LLMChain(llm=llm, prompt=chat_prompt)
print(chain.run(input_language="English", output_language="French", text="I love programming."))
