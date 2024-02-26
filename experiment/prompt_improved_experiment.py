from Dataset import dataset
from config import *
# have some answer data, we see how we categorize it based on it's equations
# 
def categorizer(answer: str):
    equations = dataset.extract_equation(answer)
    result = []
    bank = {"curLetter": UPPERAINT}
    for e in equations:
        result.append(equation_to_variables(e, bank))
    print(result)

def findSubVariable(bank, num):
    print("find a num is: ", num)
    if num in bank:
        return bank[num]
    else:
        curLetter = chr(bank["curLetter"])
        bank["curLetter"] += 1
        bank[num] = curLetter
        return curLetter

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
            print("find a num is: ", num)
            result.append(findSubVariable(bank,num))
            result.append(c)
            startDigit = i + 1
    if startDigit < len(equation):
        result.append(findSubVariable(bank,equation[startDigit:]))
    return result
        
                
                
                
                
    return equation
# Load in some dataset and then store them in category
def categorize_data():
    pass

