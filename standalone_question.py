import getpass
import os
from dotenv import load_dotenv, dotenv_values
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

from pprint import pprint
load_dotenv()

try:
    if not os.getenv("OPENAI_API_KEY"):
        os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter API key for OpenAI: ")

    llm = ChatOpenAI(api_key=os.environ["OPENAI_API_KEY"])

    tweetTemplate = 'Generate a promotional tweet for a product, from this product description: {productDesc}'

    tweetPrompt = PromptTemplate.from_template(tweetTemplate)

    tweetChain = tweetPrompt.pipe(llm)

    rsp = tweetChain.invoke(input='Electric bike')

    pprint(rsp.content)

except Exception as e:
    print(e)


