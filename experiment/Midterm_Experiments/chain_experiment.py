from chain.chain import *
from util import dataset
from langchain.chains import LLMChain
from experiment.Midterm_Experiments.experiment_main import *
from config import *
from util import util
import os
def main_run_experiments(experiment:list, path, data_length=TESTINGAMOUNT):
    test_data = dataset.get_examples(path,data_length)
    if(BASEEXP in experiment):
        # Base Experiment
        base_chain = get_default_chain()
        correct, model_completion, incorrectAnswer = run_experiment(base_chain, test_data)
        print_result(BASEEXP, correct, incorrectAnswer,data_length)
        util.store_result(BASEEXP, correct, incorrectAnswer, RESULTOGPATH + "BaseResult.jsonl")
    if(COTEXP in experiment):
        cot_chain = get_chain_of_thought_chain()
        correct_cot, model_completion_cot, incorrectAnswer_cot = run_experiment(cot_chain, test_data)
        print_result(COTEXP, correct_cot, incorrectAnswer_cot, data_length)
        util.store_result(COTEXP, correct_cot, incorrectAnswer_cot, RESULTOGPATH + "COTResult.jsonl")
    if(FSEXP in experiment):
        fs_chain = get_few_shot_prompting()
        correct_fs, model_completion_fs, incorrectAnswer_fs = run_experiment(fs_chain, test_data)
        print_result(FSEXP, correct_fs, incorrectAnswer_fs,data_length)
        util.store_result(FSEXP, correct_fs, incorrectAnswer_fs,RESULTOGPATH + "FSResult.jsonl")

def ehanceData_run_experiments(path):
    test_data = dataset.read_jsonl(path,MAXINT)
    chain = get_data_enhancement_chain()
    correct, model_completion, incorrectAnswer = data_enhencement_experiment(chain, test_data)
    print("Model's answer",model_completion)

def run_mistakes_review_experiment(path, data_length=MAXINT):
    test_data = dataset.read_jsonl(path, data_length)
    chain = get_review_mistake_chain()
    correct, model_completion, incorrectAnswer = mistakes_review_experiment(chain, test_data)
    print("Model's answer",model_completion)


# Param 'Experiment Name', correct_amount, [model_output], [{"question": ... , "answer": ...}, "model_answer"]
def print_result(exp_name, correct_amount, incorrectSamples, totalAmount=TESTINGAMOUNT):
    print("Experiment: ", exp_name)
    print("Total Correct Rate ", correct_amount/ totalAmount)
    if VERBOSE:
        for t in incorrectSamples:
            print("Question: ", t[0]["question"])
            print("Correct Answer: ", t[0]['answer'])
            print("Model's Prediction: ", t[1])

    

    
        
