from config import *
from chain import pipe_chain
from util import dataset
from Schema import schema
from util import util

def random_prompting_enhancement_mathsolver(question, storage:list) -> schema.Math_Output:
    examples = str(dataset.build_fewshot_example(dataset.get_random_examples(GSM8KOGDATA + "train.jsonl", 3)))
    result:schema.Math_Output = pipe_chain.question_answering_chain(question,examples)
    storage.append({"question": question, "solution":result.answer,"result": result.result ,"Step": "First_Solve"})
    result = pipe_chain.recheck_chain(question, result)
    storage.append({"question": question, "solution":result.answer,"result": result.result ,"Step": "Rechecked"})
    return result

def pick_correct_response(question,solution_candidates):
    current_correct:schema.Math_Output = None
    for c in solution_candidates:
        # if c["Step"] == "First_Solve":
        #     continue
        if not current_correct:
            current_correct = schema.Math_Output(answer=c["solution"],result=c["result"])
        elif(current_correct.result != c["result"]):
            new_candidate:schema.Math_Output = schema.Math_Output(answer=c["solution"],result=c["result"])
            pick = pipe_chain.pick_correct_chain(question, current_correct, new_candidate)
            if pick == "2":
                current_correct = c
    return current_correct


def main_pipe(question):
    # generate list of solutions that GPT propsoed
    solution_candidates = []
    for _ in range(SOLUTIONCANDIDATE):
        random_prompting_enhancement_mathsolver(question, solution_candidates)
        
    final_answer = pick_correct_response(question, solution_candidates)
    solution_candidates.append({"question": question, "solution":final_answer.answer,"result": final_answer.result ,"Step": "pickCorrect"})
    util.direct_storage("Results\STUDIABILITY_PIPE_METHOD\Studiability_Last_Reasoning.jsonl",solution_candidates)
    return solution_candidates
    
    
    
    
        
        
    