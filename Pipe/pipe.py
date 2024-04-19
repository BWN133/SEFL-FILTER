from config import *
from chain import pipe_chain
from util import dataset
from Schema import schema
from util import util
from tqdm import tqdm

class DummyTqdm:
    """ A dummy tqdm class that mimics tqdm's interface but does nothing. """
    def __init__(self, *args, **kwargs):
        pass
    def update(self, n=1):
        pass
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

def get_progress_bar(*args, **kwargs):
    """ Returns a tqdm progress bar or a dummy progress bar based on the verbose flag. """
    if VERBOSE:
        from tqdm import tqdm
        return tqdm(*args, **kwargs)
    else:
        return DummyTqdm(*args, **kwargs)

def random_prompting_enhancement_mathsolver(question, storage:list) -> schema.Math_Output:
    examples = str(dataset.build_fewshot_example(dataset.get_random_examples(GSM8KOGDATA + "train.jsonl", 3)))
    result:schema.Math_Output = pipe_chain.question_answering_chain(question,examples)
    storage.append({"question": question, "solution":result.answer,ANSWERKEY: result.result ,"Step": "First_Solve"})
    result = pipe_chain.recheck_chain(question, result)
    storage.append({"question": question, "solution":result.answer,ANSWERKEY: result.result ,"Step": "Rechecked"})
    return result

def pick_correct_response(question,solution_candidates):
    current_correct:schema.Math_Output = None
    with get_progress_bar(total=len(solution_candidates)) as pbar:
        for c in solution_candidates:
            if not current_correct:
                current_correct = schema.Math_Output(answer=c["solution"],result=c[ANSWERKEY])
            elif(current_correct.result != c[ANSWERKEY]):
                new_candidate:schema.Math_Output = schema.Math_Output(answer=c["solution"],result=c[ANSWERKEY])
                pick = pipe_chain.pick_correct_chain(question, current_correct, new_candidate)
                if pick == "2":
                    current_correct = c
            pbar.update(1)
    return current_correct


def main_pipe(question):
    # generate list of solutions that GPT propsoed
    if VERBOSE: print("*********************************************************\n" + "Studiability agent Recieved question: " + question)
    solution_candidates = []
    if VERBOSE: print("Random Few Shot agents are trying to answer the question collborately")
    with get_progress_bar(total=SOLUTIONCANDIDATE) as pbar:
        for _ in range(SOLUTIONCANDIDATE):
            random_prompting_enhancement_mathsolver(question, solution_candidates)
            pbar.update(1)

    if VERBOSE: print("Candidate solution generated, waiting agents to find the opimtal solution")
    finished_pick = False
    while not finished_pick:
        try:
            final_answer = pick_correct_response(question, solution_candidates)
            finished_pick = True
        except:
            print("Parser error try again")
    if VERBOSE: print("Finish picking the best answer and the answer is " + final_answer.result +  "\n*********************************************************")
    solution_candidates.append({"question": question, "solution":final_answer.answer,ANSWERKEY: final_answer.result ,"Step": "pickCorrect"})
    util.direct_storage("Results\STUDIABILITY_PIPE_METHOD\Studiability_Last_Reasoning.jsonl",solution_candidates)
    return solution_candidates
    
    
    
    
        
        
    