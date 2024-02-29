from chain.chain import *
from util import dataset
from langchain.chains import LLMChain
from experiment.experiment_main import *
from config import *
from util import util
import os
def main_run_experiments(experiment:list, path):
    test_data = dataset.get_examples(path,TESTINGAMOUNT)
    if(BASEEXP in experiment):
        # Base Experiment
        base_chain = get_default_chain()
        correct, model_completion, incorrectAnswer = run_experiment(base_chain, test_data)
        print_result(BASEEXP, correct, incorrectAnswer)
        
        util.store_result(BASEEXP, correct, incorrectAnswer, RESULTOGPATH + "BaseResult.jsonl")
    if(COTEXP in experiment):
        cot_chain = get_chain_of_thought_chain()
        correct_cot, model_completion_cot, incorrectAnswer_cot = run_experiment(cot_chain, test_data)
        print_result(COTEXP, correct_cot, incorrectAnswer_cot)
        util.store_result(COTEXP, correct_cot, incorrectAnswer_cot,RESULTOGPATH + "COTResult.jsonl")
    if(FSEXP in experiment):
        fs_chain = get_few_shot_prompting()
        correct_fs, model_completion_fs, incorrectAnswer_fs = run_experiment(fs_chain, test_data)
        print_result(FSEXP, correct_fs, incorrectAnswer_fs)
        util.store_result(FSEXP, correct_fs, incorrectAnswer_fs,RESULTOGPATH + "FSResult.jsonl")


# Param data: list[dict{"question":...,"answer": ...}]
# Return 'Experiment Name', correct_amount, [model_output], [{"question": ... , "answer": ...}, "model_answer"]
# def run_experiment(chain: LLMChain ,data:list):
#     model_completion = []
#     incorrectAnswer = []
#     correct = 0
#     for i in range(TESTINGAMOUNT):
#         cur_question = data[i]['question']
#         model_completion.append(chain.run(information=cur_question))
#         if dataset.is_correct(model_completion[-1], data[i]):
#             correct += 1
#         else:
#             incorrectAnswer.append((data[i], model_completion[-1]))
#     return correct, model_completion, incorrectAnswer

# Param 'Experiment Name', correct_amount, [model_output], [{"question": ... , "answer": ...}, "model_answer"]
def print_result(exp_name, correct_amount, incorrectSamples):
    print("Experiment: ", exp_name)
    print("Total Correct Rate ", correct_amount/ TESTINGAMOUNT)
    if VERBOSE:
        for t in incorrectSamples:
            print("Question: ", t[0]["question"])
            print("Correct Answer: ", t[0]['answer'])
            print("Model's Prediction: ", t[1])

    

    
        
