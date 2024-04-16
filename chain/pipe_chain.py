from langchain_openai import ChatOpenAI
from config import *
from langchain.output_parsers import PydanticOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from Schema import schema

llm = ChatOpenAI(temperature=0.7, model_name="gpt-3.5-turbo")

def build_recheck_example(question:str, potential_solution:str, potential_solution_result: str, final_answer:str, final_result:str):
    result =  "For the content below, all content inside **** **** are what system provided you. The AI output content are those inside #### #### not including ####"
    result += "**** question: " + question + "\n\n Potential Solution: " + potential_solution + "\n Answer of potential solution: " + potential_solution_result
    result += "####"
    d = {"answer":final_answer, "result":final_result}
    return result + str(d) + "####"
    

def recheck_chain(question:str, potentialSolution: schema.Math_Output):
    parser = PydanticOutputParser(pydantic_object=schema.Math_Output)
    prompt = ChatPromptTemplate.from_messages([
        "You are an expert in validating and correcting math solutions."
        "You will be provided with a math world problem and a solution that could be incorrect"
        "Your job is to conduct following stepsL:"
        "1. Recheck the quantitities mentioned in the problem description and exam the answer"
        "2. Redo each step of the question and produce a result"
        "You will output a dictionary with following fields:"
        "answer: The step by step description of how to solve the question"
        "result: Single number only result"
        "Here are few shot examples:"
        "{examples}"
        "Here the question:"
        "{question}"
        "And here are the potential solution"
        "{potential_solution_description}"
        "The final answer of the potential solution"
        "{potential_solution_answer}"
    ]).partial(format_instructions=parser.get_format_instructions())
    example = build_recheck_example(
        "Jose threatened to withhold 20 percent of Amanda's pay if she does not finish her sales report by midnight. If Amanda makes $50.00 an hour and works for 10 hours a day, how much money will she receive if she does not finish the sales report by midnight?",
        "If she works for 10 hours a day she will get 50 * 10 = 500$. However, if she didn't make the deadline, she will get 20% withhold which end up with 500 * 0.2 = 100 USD. She will only get 100 USD if she didn't meet the deadline.",
        "100",
        "If she works for 10 hours a day at an hourly pay of $50, then her total income in a day is $<<10*50=500>>500.\nIf she doesn't meet the deadline Jose gave her, she'll lose 20/100*$500 = $<<20/100*500=100>>100\nShe'll receive $500-$100= $<<500-100=400>>400 if Jose cuts out 20 percent of her pay.",
        '400'
    )
    examples = str([example])
    enhance_checker = (
        prompt | llm | parser
    )
    return enhance_checker.invoke({"question":question, "examples":examples,"potential_solution_description": potentialSolution.answer, "potential_solution_answer":potentialSolution.result})


def question_answering_chain(question, examples):
    # print("!!!!!!!!!!!!!!!!!!Question is right here" + question)
    parser = PydanticOutputParser(pydantic_object=schema.Math_Output)
    prompt = ChatPromptTemplate.from_messages([
        "You are an expert math solver. Your job is to firstly read the question and solve it step by step"
        "You will be provided with the question along with couple examples"
        "You will be responsible for out a dictionary with following feild"
        "answer: The step by step description of how to solve the question"
        "result: Single number only result"
        "Here are list of few shot examples"
        "{examples}"
        "Here are the question you need to solve: {question}"
    ]
    ).partial(format_instructions=parser.get_format_instructions())

    
    answer_proposer = (
        prompt | llm | parser
    )
    
    return answer_proposer.invoke({"question": question, "examples":examples})
