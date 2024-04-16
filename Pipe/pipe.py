from config import *
from chain import pipe_chain
from util import dataset
from Schema import schema

def random_prompting_enhancement_mathsolver(question) -> schema.Math_Output:
    examples = str(dataset.build_fewshot_example(dataset.get_random_examples(GSM8KOGDATA + "train.jsonl", 3)))
    # print("!!!!!!!!!!!!!!!!!examples are here: ", examples)
    result = pipe_chain.question_answering_chain(question,examples)
    print("Without enhancement result got!!!!",result)
    result = pipe_chain.recheck_chain(question, result)
    return result

def main_pipe(question):
    # generate list of solutions that GPT propsoed
    solution_candidates = []
    for _ in range(SOLUTIONCANDIDATE):
        print(random_prompting_enhancement_mathsolver(question))
    
        
        
    
    # print(answer)
    # return answer