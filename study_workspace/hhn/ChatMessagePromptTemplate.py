from langchain.prompts import ChatMessagePromptTemplate
import os
os.environ["http_proxy"] = "http://127.0.0.1:1080"
os.environ["https_proxy"] = "http://127.0.0.1:1080"
os.environ["OPENAI_API_KEY"] = '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'

prompt = "May the {subject} be with you"

chat_message_prompt = ChatMessagePromptTemplate.from_template(role="Jedi", template=prompt)
print(chat_message_prompt.format(subject="force"))

