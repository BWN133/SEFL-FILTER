from dotenv import load_dotenv
from chain.chain import *
from Dataset import dataset
import os
from langchain.chains import LLMChain
from config import *
import json 
def main_run_experiments(experiment:list):
    test_data = dataset.get_examples("test",TESTINGAMOUNT)
    if(BASEEXP in experiment):
        # Base Experiment
        base_chain = get_default_chain()
        correct, model_completion, incorrectAnswer = run_experiment(base_chain, test_data)
        print_result(BASEEXP, correct, incorrectAnswer)
        store_result(BASEEXP, correct, incorrectAnswer,"BaseResult.json")
    if(COTEXP in experiment):
        cot_chain = get_chain_of_thought_chain()
        correct_cot, model_completion_cot, incorrectAnswer_cot = run_experiment(cot_chain, test_data)
        print_result(COTEXP, correct_cot, incorrectAnswer_cot)
        store_result(COTEXP, correct_cot, incorrectAnswer_cot,"COTResult.json")
    if(FSEXP in experiment):
        fs_chain = get_few_shot_prompting()
        correct_fs, model_completion_fs, incorrectAnswer_fs = run_experiment(fs_chain, test_data)
        print_result(FSEXP, correct_fs, incorrectAnswer_fs)
        store_result(FSEXP, correct_fs, incorrectAnswer_fs,"FSResult.json")


# Param data: list[dict{"question":...,"answer": ...}]
# Return 'Experiment Name', correct_amount, [model_output], [{"question": ... , "answer": ...}, "model_answer"]
def run_experiment(chain: LLMChain ,data:list):
    model_completion = []
    incorrectAnswer = []
    correct = 0
    for i in range(TESTINGAMOUNT):
        cur_question = data[i]['question']
        model_completion.append(chain.run(information=cur_question))
        if dataset.is_correct(model_completion[-1], data[i]):
            correct += 1
        else:
            incorrectAnswer.append((data[i], model_completion[-1]))
    return correct, model_completion, incorrectAnswer

# Param 'Experiment Name', correct_amount, [model_output], [{"question": ... , "answer": ...}, "model_answer"]
def print_result(exp_name, correct_amount, incorrectSamples):
    print("Experiment: ", exp_name)
    print("Total Correct Rate ", correct_amount/ TESTINGAMOUNT)
    if VERBOSE:
        for t in incorrectSamples:
            print("Question: ", t[0]["question"])
            print("Correct Answer: ", t[0]['answer'])
            print("Model's Prediction: ", t[1])

# Param 'Experiment Name', correct_amount, [model_output], [{"question": ... , "answer": ...}, "model_answer"], 
def store_result(exp_name:str, correct_amount:int, incorrectSamples:list, fileName:str):
    output = []
    output.append({"Experiment Name": exp_name})
    output.append({"Correct Amount" : correct_amount})
    output.append({"Incorrect Samples":[]})
    for t in incorrectSamples:
        t[0]["Incorrect Answer"] = t[1]
        output[2]["Incorrect Samples"].append(t[0])
    path = os.path.join('experiment/result/', fileName)
    # Writing to a file
    with open(path, 'w') as f:
        json.dump(output, f, indent=4)
    

    
        
