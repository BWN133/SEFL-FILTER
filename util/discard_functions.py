import json 
from util import dataset
from config import *
import os

# equation is equation, bank: {"curLetter": int, "num_string":"num"}
def equation_to_variables(equation:str, bank:dict):
    # Split the equation into parts
    assert isinstance(bank["curLetter"], int)
    signs = "+-*/="
    startDigit = 0
    result = []
    for i,c in enumerate(equation):
        if c in signs:
            num = equation[startDigit: i]
            result.append(findSubVariable(bank,num))
            result.append(c)
            startDigit = i + 1
    if startDigit < len(equation):
        result.append(findSubVariable(bank,equation[startDigit:]))
    return ''.join(result)




def findSubVariable(bank, num):
    if num in bank:
        return bank[num]
    else:
        curLetter = chr(bank["curLetter"])
        bank["curLetter"] += 1
        bank[num] = curLetter
        return curLetter



# Not Working, simply capture data based on equations are not legit. For example
# If I have A + B and C + F both equal to 15, this two 15 may point to completely different things thus
# can not use two simple D to represent them
# also repetitive number may also mean two of same thing or two different thing 
# for example
# 6*6 = 36
def exact_categorizer(answer: str):
    equations = dataset.extract_equation(answer)
    result = []
    bank = {"curLetter": UPPERAINT}
    for e in equations:
        result.append(equation_to_variables(e, bank))
        
    return '###'.join(result)


# Load in some dataset and then store them in category
# result = true: load from result folder
# result = false: load from dataset
def categorize_dataset_exact(path):
    categorized_data = {}
    target_samples = dataset.get_examples(path)

    for sample in target_samples:
        if sample[ANSWERKEY] is None:
            continue
        key = exact_categorizer(sample[ANSWERKEY])
        if key not in categorized_data:
            categorized_data[key] = []
        categorized_data[key].append(sample)
    return categorized_data