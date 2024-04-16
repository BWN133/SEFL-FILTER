import json 
from util import dataset
from config import *
import os
# Param 'Experiment Name', correct_amount, [model_output], [{"question": ... , "answer": ...}, "model_answer"], 
# mode: AUGMOD | DEFMOD
def store_result(exp_name:str, correct_amount:int, incorrectSamples:list, path:str):
    output = []
    output.append({"Experiment Name": exp_name})
    output.append({"Correct Amount" : correct_amount})
    # output.append({"Incorrect Samples":[]})
    for t in incorrectSamples:
        t[0]["Incorrect Answer"] = t[1]
        output.append(t[0])
    with open(path, 'w') as file:
        for item in output:
            json_str = json.dumps(item)  # Serialize the object to a JSON formatted str
            file.write(json_str + '\n')  # Write the JSON string followed by a newline character

# Param 'Experiment Name', correct_amount, [model_output], [{"question": ... , "answer": ...}, "model_answer"], 
def store_category(path, data):
    # output = []
    # for k in data:
    #     output.append({k:data[k]})
    with open(path, 'w') as file:
        json_str = json.dumps(data)  # Serialize the object to a JSON formatted str
        file.write(json_str + '\n')  # Write the JSON string followed by a newline character

def load_Categorized_dict(path):
    with open(path, 'r') as file:
        data = json.load(file)
    return data 


def operation_categorizer(answer: str):
    equations = dataset.extract_equation(answer)
    # steps, +, -, *, /
    result = [0,0,0,0,0]
    for e in equations:
        for c in e:
            if c == '+':
                result[1] += 1
            elif c == '-':
                result[2] += 1
            elif c == '*':
                result[3] += 1
            elif c == '/':
                result[4] += 1
        # result[0] += 1
    return str(result)


                
# Load in some dataset and then store them in category
# result = true: load from result folder
# result = false: load from dataset
def categorize_dataset(path):
    categorized_data = {}
    target_samples = dataset.get_examples(path)

    for sample in target_samples:
        if sample[ANSWERKEY] is None:
            continue
        key = operation_categorizer(sample[ANSWERKEY])
        if key not in categorized_data:
            categorized_data[key] = []
        categorized_data[key].append(sample)
    return categorized_data

