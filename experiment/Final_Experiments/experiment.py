from chain import chain
from util import dataset
from langchain.chains import LLMChain
from config import *
from util import util
import os
from Pipe import pipe
from tqdm import tqdm

def abalation_no_enhancement_experiment(start:int, end:int):
    test_data = dataset.get_examples(GSM8KOGDATA + "test.jsonl",MAXINT)[start-1: end]
    output = []
    total_output = []
    output.append({"correct":0})
    correct = 0
    amount_ran = 0
    with tqdm(total=(end - start + 1)) as pbar:
        for i,data in enumerate(test_data):
            answer = dataset.extract_answer(data[ANSWERKEY])
            try: 
                std_result = pipe.ablation_no_enhance_pipe(data[QUESTIONKEY])
            except:
                print("execution error at" + str(i) + "data")
                amount_ran = i
                break

            if std_result[-1][ANSWERKEY] != answer:
                curWrong = {QUESTIONKEY:data[QUESTIONKEY],ANSWERKEY:data[ANSWERKEY], INCORRECTANSWERKEY:std_result}
                output.append(curWrong)
                print(curWrong)
            else:
                correct += 1
            total_output.append({QUESTIONKEY:data[QUESTIONKEY],ANSWERKEY:data[ANSWERKEY], "System_Answer":std_result})
            pbar.update(1)
            amount_ran += 1
    output[0]["correct"] = correct
    output.append({"Amount Ran": amount_ran})
    util.store_category("Results\STUDIABILITY_PIPE_METHOD\Studiability_Result_ablation_no_enhancement_6c_3_"+str(start) + "_" + str(end) + ".jsonl", output)
    util.store_category("Results\STUDIABILITY_PIPE_METHOD\Studiability_Result_Total_no_enhancement_6c_3_"+str(start) + "_" + str(end) + ".jsonl", total_output)
    


def abalation_no_random_experiment(start:int, end:int):
    test_data = dataset.get_examples(GSM8KOGDATA + "test.jsonl",MAXINT)[start-1: end]
    output = []
    total_output = []
    output.append({"correct":0})
    correct = 0
    amount_ran = 0
    with tqdm(total=(end - start + 1)) as pbar:
        for i,data in enumerate(test_data):
            answer = dataset.extract_answer(data[ANSWERKEY])
            try: 
                std_result = pipe.ablation_no_random_pipe(data[QUESTIONKEY])
            except:
                print("execution error at" + str(i) + "data")
                amount_ran = i
                break

            if std_result[-1][ANSWERKEY] != answer:
                curWrong = {QUESTIONKEY:data[QUESTIONKEY],ANSWERKEY:data[ANSWERKEY], INCORRECTANSWERKEY:std_result}
                output.append(curWrong)
                print(curWrong)
            else:
                correct += 1
            total_output.append({QUESTIONKEY:data[QUESTIONKEY],ANSWERKEY:data[ANSWERKEY], "System_Answer":std_result})
            pbar.update(1)
            amount_ran += 1
    output[0]["correct"] = correct
    output.append({"Amount Ran": amount_ran})
    util.store_category("Results\STUDIABILITY_PIPE_METHOD\Studiability_Result_ablation_no_random_3_"+str(start) + "_" + str(end) + ".jsonl", output)
    util.store_category("Results\STUDIABILITY_PIPE_METHOD\Studiability_Result_Total_no_random_3_"+str(start) + "_" + str(end) + ".jsonl", total_output)
    



# Comparing performance of COT agent versus our Studiability agent with both GPT 3.5
def studiability_result(start:int, end:int):
    test_data = dataset.get_examples(GSM8KOGDATA + "test.jsonl",MAXINT)[start-1: end]
    output = []
    total_output = []
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
                curWrong = {QUESTIONKEY:data[QUESTIONKEY],ANSWERKEY:data[ANSWERKEY], INCORRECTANSWERKEY:std_result}
                output.append(curWrong)
                print(curWrong)
            else:
                correct += 1
            total_output.append({QUESTIONKEY:data[QUESTIONKEY],ANSWERKEY:data[ANSWERKEY], "System_Answer":std_result})
            pbar.update(1)
            amount_ran += 1
    output[0]["correct"] = correct
    output.append({"Amount Ran": amount_ran})
    util.store_category("Results\STUDIABILITY_PIPE_METHOD\Studiability_Result_3_"+str(start) + "_" + str(end) + ".jsonl", output)
    util.store_category("Results\STUDIABILITY_PIPE_METHOD\Studiability_Result_Total_3_"+str(start) + "_" + str(end) + ".jsonl", total_output)
    


def count_variation(path):
    data = util.dataset.read_jsonl(path, MAXINT)
    current_total = 0
    total_data = 0
    for d in data:
        curset = set()
        # print(d)
        if 'System_Answer' not in d.keys():
            continue
        for system_step in d['System_Answer']:
            if system_step['Step'] != 'First_Solve':
                continue
            curset.add(system_step['answer'])
        current_total += len(curset)
        total_data += 1
    return current_total / total_data

        
def correct_solution_generate_rate(path):
    data = util.dataset.read_jsonl(path, MAXINT)
    current_total = 0
    total_data = 0
    for d in data:
        curset = set()
        if 'System_Answer' not in d.keys():
            continue
        for system_step in d['System_Answer']:
            curset.add(system_step['answer'])
        if dataset.extract_answer(d['answer']) in curset:
            current_total += 1
        total_data += 1
    return current_total/ total_data


def correctly_pick_generate_rate(path):
    data = util.dataset.read_jsonl(path, MAXINT)
    current_total = 0
    total_data = 0
    for d in data:
        curset = set()
        final_result = ""
        if 'System_Answer' not in d.keys():
            continue
        for system_step in d['System_Answer']:
            curset.add(system_step['answer'])
            if system_step['Step'] == 'pickCorrect':
                final_result = system_step['answer']
        if len(curset) > 1:
            total_data += 1
            if dataset.extract_answer(d['answer']) == final_result:
                current_total += 1
        
    return current_total/ total_data


def majority_vote_accuracy(path):
    data = util.dataset.read_jsonl(path, MAXINT)
    current_total = 0
    total_data = 0
    for d in data:
        total_data += 1
        curset = {}
        final_result = ""
        if 'System_Answer' not in d.keys():
            continue
        for system_step in d['System_Answer']:
            if system_step['Step'] != 'pickCorrect':
                cura = system_step['answer'] 
                # print(cura,curset)
                if cura not in curset.keys():
                    curset[cura] = 1
                else:
                    curset[cura] += 1
            else:
                print("find pick correct")
        curCount = 0
        for k in curset.keys():
            if curset[k] > curCount:
                curCount = curset[k]
                final_result = k
        if dataset.extract_answer(d['answer']) == final_result:
                current_total += 1
        
    return current_total/ total_data



def majority_vote_incorrect_SELF_FILTER_COrrect(path):
    data = util.dataset.read_jsonl(path, MAXINT)
    current_total = 0
    total_data = 0
    output = []
    for d in data:
        total_data += 1
        curset = {}
        final_result = ""
        pick_correct_answer = ""
        if 'System_Answer' not in d.keys():
            continue
        for system_step in d['System_Answer']:
            if system_step['Step'] != 'pickCorrect':
                cura = system_step['answer'] 
                # print(cura,curset)
                if cura not in curset.keys():
                    curset[cura] = 1
                else:
                    curset[cura] += 1
            else:
                pick_correct_answer = system_step['answer']
        curCount = 0
        for k in curset.keys():
            if curset[k] > curCount:
                curCount = curset[k]
                final_result = k
        
        if pick_correct_answer != final_result and dataset.extract_answer(d['answer']) == pick_correct_answer:
                output.append(d)
        
    return output




def majority_vote_correct_SELF_FILTER_incorrect(path):
    data = util.dataset.read_jsonl(path, MAXINT)
    current_total = 0
    total_data = 0
    output = []
    for d in data:
        total_data += 1
        curset = {}
        final_result = ""
        pick_correct_answer = ""
        if 'System_Answer' not in d.keys():
            continue
        for system_step in d['System_Answer']:
            if system_step['Step'] != 'pickCorrect':
                cura = system_step['answer'] 
                # print(cura,curset)
                if cura not in curset.keys():
                    curset[cura] = 1
                else:
                    curset[cura] += 1
            else:
                pick_correct_answer = system_step['answer']
        curCount = 0
        for k in curset.keys():
            if curset[k] > curCount:
                curCount = curset[k]
                final_result = k
        
        if pick_correct_answer != final_result and dataset.extract_answer(d['answer']) == final_result:
                output.append(d)
        
    return output