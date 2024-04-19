from chain import chain
from util import dataset
from langchain.chains import LLMChain
from config import *
from util import util
import os
from Pipe import pipe


# Comparing performance of COT agent versus our Studiability agent with both GPT 3.5
def studiability_result(amount:int):
    test_data = dataset.get_examples(GSM8KOGDATA + "test.jsonl",amount)
    output = []
    correct = 0
    for data in test_data:
        answer = dataset.extract_answer(data[ANSWERKEY])
        std_result = pipe.main_pipe(data[QUESTIONKEY])
        if std_result[-1][ANSWERKEY] != answer:
            output.append({QUESTIONKEY:data[QUESTIONKEY],ANSWERKEY:data[ANSWERKEY], INCORRECTANSWERKEY:std_result[-1][SOLUTIONKEY]})
            print(output)
            
        
    