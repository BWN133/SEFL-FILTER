from chain.chain import *
from util import dataset
from langchain.chains import LLMChain
from config import *
from util import util
import os

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
            supData = augSamples[curK][0:10] if curK in augSamples else DEFAULTCOTPROMPT
            model_completion.append(chain.run(information=cur_question, relatedProblems=supData))
        else:
            model_completion.append(chain.run(information=cur_question))
        if dataset.is_correct(model_completion[-1], data[i]):
            correct += 1
        else:
            incorrectAnswer.append((data[i], model_completion[-1]))
    return correct, model_completion, incorrectAnswer