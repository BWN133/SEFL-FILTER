from config import *
from chain import pipe_chain
from util import dataset
from Schema import schema
from Pipe import pipe
def test_system():
    question = "Albert is wondering how much pizza he can eat in one day. He buys 2 large pizzas and 2 small pizzas. A large pizza has 16 slices and a small pizza has 8 slices. If he eats it all, how many pieces does he eat that day?"
    print(pipe.main_pipe(question=question))

def harder_question_system_test():
    question = "Sansa is a famous artist, she can draw a portrait and sell it according to its size. She sells an 8-inch portrait for $5, and a 16-inch portrait for twice the price of the 8-inch portrait. If she sells three 8-inch portraits and five 16-inch portraits per day, how many does she earns every 3 days?"
    print(pipe.main_pipe(question=question))

def test_recheck_chain():
    potential_answer = schema.Math_Output(answer="The difference in age between Teresa and Morio is 71 - 59 = 12 years.\nWhen their daughter is born, Teresa is 38 - 12 =26 years old.",
                           result="26")
    question = "Teresa is 59 and her husband Morio is 71 years old. Their daughter, Michiko was born when Morio was 38.  How old was Teresa when she gave birth to Michiko?"
    print(pipe_chain.recheck_chain(question, potential_answer))
    
def test_combine_chain():
    potential_answer1 = schema.Math_Output(answer="The difference in age between Teresa and Morio is 71 - 59 = 12 years.\nWhen their daughter is born, Teresa is 38 - 12 =26 years old.",
                        result="26")
    potential_answer2 = schema.Math_Output(answer="The difference in age between Teresa and Morio is 71 - 59 = 123 years.\nWhen their daughter is born, Teresa is 38 - 123 = -89 years old.",
                        result="-89")
    question = "Teresa is 59 and her husband Morio is 71 years old. Their daughter, Michiko was born when Morio was 38.  How old was Teresa when she gave birth to Michiko?"
    print(pipe_chain.pick_correct_chain(question=question,potential_solution1=potential_answer1,potential_solution2=potential_answer2))