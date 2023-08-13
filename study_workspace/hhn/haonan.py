from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
import os
os.environ["http_proxy"] = "http://127.0.0.1:1080"
os.environ["https_proxy"] = "http://127.0.0.1:1080"
os.environ["OPENAI_API_KEY"] = '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'
llm = OpenAI(temperature=0.9)
prompt = PromptTemplate(
    input_variables=["product"],
    template="What is a good name for a company that makes {product}?",
)
from langchain.chains import LLMChain
chain = LLMChain(llm=llm, prompt=prompt)
chain.run("colorful socks")
# -> '\n\nSocktastic!'