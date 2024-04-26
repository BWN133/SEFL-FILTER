from chain.chain import *
from util import dataset
from langchain.chains import LLMChain
from config import *
from util import util
import os

import random

def select_and_combine(list1, list2):
    l = len(list1)
    new_list = []
    if l >= 7:
        new_list = random.sample(list1, 7)
    else:
        new_list.extend(list1)
        new_list.extend(random.sample(list2, 7 - l))
    
    return new_list


# Param mode: 0: normal experiment, 1 with augmented example, 2 Dataenhancement 
def run_experiment(chain: LLMChain ,data:list, augSamples=None):
    model_completion = []
    incorrectAnswer = []
    correct = 0
    for i in range(len(data)):
        if QUESTIONKEY not in data[i]:
            continue
        cur_question = data[i][QUESTIONKEY]
        if augSamples:
            curK = util.operation_categorizer(data[i][ANSWERKEY])
            sample  = augSamples[curK] if curK in augSamples else []
            supData = select_and_combine(sample, DEFAULTCOTPROMPTARRAY)
            model_completion.append(chain.run(information=cur_question, relatedProblems=supData))
        else:
            model_completion.append(chain.run(information=cur_question))
        if dataset.is_correct(model_completion[-1], data[i]):
            correct += 1
        else:
            incorrectAnswer.append((data[i], model_completion[-1]))
    return correct, model_completion, incorrectAnswer

def data_enhencement_experiment(chain: LLMChain, data: list):
    model_output = []
    for i in range(len(data)):
        if QUESTIONKEY not in data[i]:
            continue
        cur_question = data[i][QUESTIONKEY]
        cur_answer = data[i][ANSWERKEY]
        model_output.append(chain.run(question=cur_question,answer=cur_answer, relatedProblems=DEFAULTAUGDATAPROMPTARRAY))
    return None, model_output, None
    
def mistakes_review_experiment(chain: LLMChain, data:list):
    model_output = []
    for i in range(len(data)):
        if QUESTIONKEY not in data[i]:
            continue
        cur_question = data[i][QUESTIONKEY]
        cur_answer = data[i][ANSWERKEY]
        cur_incorrect_answer = data[i][INCORRECTANSWERKEY]
        model_output.append(chain.run(question=cur_question,answer=cur_answer, incorrect_answer=cur_incorrect_answer))
    return None, model_output, None
    