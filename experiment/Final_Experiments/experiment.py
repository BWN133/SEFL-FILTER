from chain import chain
from util import dataset
from langchain.chains import LLMChain
from config import *
from util import util
import os
from Pipe import pipe
from tqdm import tqdm


# Comparing performance of COT agent versus our Studiability agent with both GPT 3.5
def studiability_result(start:int, end:int):
    test_data = dataset.get_examples(GSM8KOGDATA + "test.jsonl",MAXINT)[start-1: end]
    output = []
    output.append({"correct":0})
    correct = 0
    amount_ran = 0
    with tqdm(total=(end - start + 1)) as pbar:
        for i,data in enumerate(test_data):
            answer = dataset.extract_answer(data[ANSWERKEY])
            try: 
                std_result = pipe.main_pipe(data[QUESTIONKEY])
            except:
                print("execution error at" + str(i) + "data")
                amount_ran = i
                break
            if std_result[-1][ANSWERKEY] != answer:
                output.append({QUESTIONKEY:data[QUESTIONKEY],ANSWERKEY:data[ANSWERKEY], INCORRECTANSWERKEY:std_result})
                print(output)
            else:
                correct += 1
            pbar.update(1)
            amount_ran += 1
    output[0]["correct"] = correct
    output.append({"Amount Ran": amount_ran})
    util.store_category("Results\STUDIABILITY_PIPE_METHOD\Studiability_Result"+str(start) + "_" + str(end) + ".jsonl", output)
    
    
    