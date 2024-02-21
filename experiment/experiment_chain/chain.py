from langchain.chains import LLMChain
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

# from output_parsers import summary_parser, ice_breaker_parser, topics_of_interest_parser

llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
# llm_creative = ChatOpenAI(temperature=1, model_name="gpt-3.5-turbo")

def get_summary_chain() -> LLMChain:
    summary_template = """
         You are given a math question {information}, think through it step by step and provide me 
         
         1. step by step reasoning
         2. Answer
         \n
     """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"],
        template=summary_template
    )

    return LLMChain(llm=llm, prompt=summary_prompt_template)
