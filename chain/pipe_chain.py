from langchain_openai import ChatOpenAI
from config import *
import re
import json
from langchain.output_parsers import PydanticOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from Schema import schema
from langchain_core.runnables import Runnable, RunnableConfig
from langchain_core.messages import AIMessage, HumanMessage, ToolMessage
from langchain_core.runnables import RunnablePassthrough


Math_Output_parser = PydanticOutputParser(pydantic_object=schema.Math_Output)
Compare_Output_parser = PydanticOutputParser(pydantic_object=schema.Compare_Output)
llm = ChatOpenAI(temperature=0.7, model_name="gpt-3.5-turbo")
# llm = ChatOpenAI(temperature=0.7, model_name="gpt-4")

    

def error_resistance_Math_Output_parser(msg: AIMessage, config: RunnableConfig):
    try:
        return Math_Output_parser.invoke(msg, config=config)
    except Exception as e:
        try:
            pattern = r"\{[^{}]*\}"
            # Find all matches
            matches = re.findall(pattern, msg.content)
            r = json.loads(matches[0])
            return_r =  schema.Math_Output(answer=r["answer"], result=r["result"])
            return return_r
        except:
            raise e
        


def error_resistance_Compare_Output_parser(msg: AIMessage,config: RunnableConfig):
    try:
        return Compare_Output_parser.invoke(msg, config=config)
    except Exception as e:
        try:
            pattern = r"\{[^{}]*\}"

            # Find all matches
            matches = re.findall(pattern, msg.content)
            r = json.loads(matches[0])
            return_r = schema.Compare_Output(reasoning=r["reasoning"],choice=r["choice"])
            return return_r
        except:
            raise e

def exception_to_messages(inputs: dict) -> dict:
    if VERBOSE: print("\nReach exception_to_messages +++++++++++++++++++++++++")
    exception = str(inputs['exception'])
    if VERBOSE: print("Here are the exception object *****&&&&&&&&&&&&&&&*******" + exception + "*****&&&&&&&&&&&&&&&*******")
    # Add historical messages to the original input, so the model knows that it made a mistake with the last tool call.
    messages = ChatPromptTemplate.from_messages ([
        "The last call raised an exception:",
        exception,
        "Do not repeat mistakes and try again."
    ])
    inputs["last_output"] = messages
    return inputs



def build_recheck_example(question:str, potential_solution:str, final_answer:str, final_result:str):
    result =  "For the content below, all content inside **** **** are what system provided you. The AI output content are those inside #### #### not including ####"
    result += "**** question: " + question + "\n\n Potential Solution: " + potential_solution
    result += "####"
    d = {"answer":final_answer, "result":final_result}
    return result + str(d) + "####"
def build_pick_correct_example(question:str, s1:str,s2:str, reasoning:str, choice:str):
    result = "For the content below, all content inside **** **** are what system provided you. The AI output content are everything not encapsulated in ****"
    result += "**** question: " + question + "\n\n Solution 1: " + s1 + " \n Solution 2: " + s2 + "****"
    result += """{"reasoning":""" + reasoning + """, "choice":""" + choice + """}""" 
    return result

def pick_correct_chain(question: str, potential_solution1:schema.Math_Output, potential_solution2:schema.Math_Output):
    prompt = ChatPromptTemplate.from_messages([
        "You are an expert in finding the correct solution from two purposed solution"
        "You will be provided with a format example that you need to learn the output format encapsulated in ~~~~~"
        "Few shot examples encapsulated in -----"
        "A math word question encapsulated with *****"
        "Solution 1 that may be incorrect encapsulated in ^^^^^"
        "Solution 2 that may be incorrect encapsulated in &&&&&"
        "Your job is to conduct following steps:"
        "1. Read the question and provided solutions"
        "2. Explain your reasoning and pick one solution from provided solution"
        "You will output a dictionary with following fields:"
        "1.reasoning: The step by step description of why you pick the answer"
        "2.choice: 1 or 2 based on your choices"
        "Remenber to use double quote \" for key values and result"
        "~~~~~{formatExample}~~~~~"
        "-----{examples}-----"
        "*****{question}*****"
        "^^^^^{potential_solution_description1}^^^^^"
        "&&&&&{potential_solution_description2}&&&&&"
    ]).partial(format_instructions=Compare_Output_parser.get_format_instructions())
    
    formatExample = """{"reasoning":"The second solution is correct because the first solution picked wrong solution","choice":"2"}"""
    examples = build_pick_correct_example("Yella's computer usage last week was 91 hours. If she plans to use the computer 8 hours a day for this week, how much less \u200bis her computer usage for this week?",
                               "Yella can use the computer 8 x 7 = 56 hours for this week.\nTherefore, Yella's computer usage for this week is 91 - 56 = 35 hours less than her computer usage last week",
                               "Yella can use the computer 8 x 7 = 56 hours for this week.\nTherefore, Yella's computer usage for this week is 91 - 56 = 30 hours less than her computer usage last week",
                               "The first solution is correct because there is a calculation error in the second solution",
                               "1")
    correct_solution_picker = (
        prompt | llm | error_resistance_Compare_Output_parser
    )
    self_correct_enhance_chain = correct_solution_picker.with_fallbacks([exception_to_messages | correct_solution_picker], exception_key="exception")
    return self_correct_enhance_chain.invoke({"question":question, "formatExample":formatExample,"examples":examples,"potential_solution_description1": potential_solution1.answer,"potential_solution_description2": potential_solution2.answer})
    

def recheck_chain(question:str, potentialSolution: schema.Math_Output):
    prompt = ChatPromptTemplate.from_messages([
        "You are an expert in correcting math solutions."
        "You will be provided with a math word question encapsulated with *****"
        "A solution that is definetly incorrect encapsulated in ^^^^^"
        "A format example that you need to learn the output format encapsulated in ~~~~~"
        "Few shot examples encapsulated in -----"
        "Your job is to conduct following steps:"
        "1. Recheck the quantitities mentioned in the problem description and exam the wrong answer"
        "2. Redo the problem"
        "You will output a dictionary with following fields:"
        "answer: The step by step description of how to solve the question"
        "result: Single number only result"
        "Remenber to use double quote \" for key values and result"
        "~~~~~{formatExample}~~~~~"
        "-----{examples}-----"
        "*****{question}*****"
        "^^^^^{potential_solution_description}^^^^^"
    ]).partial(format_instructions=Math_Output_parser.get_format_instructions())
    example = build_recheck_example(
        "Jose threatened to withhold 20 percent of Amanda's pay if she does not finish her sales report by midnight. If Amanda makes $50.00 an hour and works for 10 hours a day, how much money will she receive if she does not finish the sales report by midnight?",
        "If she works for 10 hours a day she will get 50 * 10 = 500$. However, if she didn't make the deadline, she will get 20% withhold which end up with 500 * 0.2 = 100 USD. She will only get 100 USD if she didn't meet the deadline.",
        "If she works for 10 hours a day at an hourly pay of $50, then her total income in a day is $<<10*50=500>>500.\nIf she doesn't meet the deadline Jose gave her, she'll lose 20/100*$500 = $<<20/100*500=100>>100\nShe'll receive $500-$100= $<<500-100=400>>400 if Jose cuts out 20 percent of her pay.",
        "400"
        )
    formatExample = """{"answer": "Yella can use the computer 8 x 7 = 56 hours for this week. Therefore, Yella's computer usage for this week is 91 - 56 = 35 hours less than her computer usage last week.",  "result": "35"}"""
    examples = str([example])
    enhance_checker = (
        prompt | llm | error_resistance_Math_Output_parser
    )
    self_correct_enhance_chain = enhance_checker.with_fallbacks([exception_to_messages | enhance_checker], exception_key="exception")
    return self_correct_enhance_chain.invoke({"question":question, "examples":examples,"potential_solution_description": potentialSolution.answer,"formatExample":formatExample})


def question_answering_chain(question, examples):
    prompt = ChatPromptTemplate.from_messages([
        "You are an expert math solver. Your job is to firstly read the question and solve it step by step"
        "You will be provided with a math word question encapsulated with *****"
        "a format example that you need to learn the output format encapsulated in ~~~~~"
        "Few shot examples encapsulated in -----"
        "You will be responsible for out a dictionary with following feild"
        "answer: The step by step description of how to solve the question"
        "result: Single number only result"
        "Remenber to use double quote \" for key values and result"
        "Here is one formate example: ~~~~~{formatExample}~~~~~"
        "Here are list of few shot examples"
        "-----{examples}-----"
        "Here are the question you need to solve: *****{question}*****"
    ]
    ).partial(format_instructions=Math_Output_parser.get_format_instructions())

    formatExample = """{"answer": "Yella can use the computer 8 x 7 = 56 hours for this week. Therefore, Yella's computer usage for this week is 91 - 56 = 35 hours less than her computer usage last week.",  "result": "35"}"""
    answer_proposer = (
        prompt | llm | error_resistance_Math_Output_parser
    )
    
    self_correct_enhance_chain = answer_proposer.with_fallbacks([exception_to_messages | answer_proposer], exception_key="exception")
    return self_correct_enhance_chain.invoke({"question": question, "examples":examples,"formatExample": formatExample})
