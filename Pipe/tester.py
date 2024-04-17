from config import *
from chain import pipe_chain
from util import dataset
from Schema import schema

def test_recheck_chain():
    potential_answer = schema.Math_Output(answer="The difference in age between Teresa and Morio is 71 - 59 = 12 years.\nWhen their daughter is born, Teresa is 38 - 12 =26 years old.",
                           result="26")
    question = "Teresa is 59 and her husband Morio is 71 years old. Their daughter, Michiko was born when Morio was 38.  How old was Teresa when she gave birth to Michiko?"
    print(pipe_chain.recheck_chain(question, potential_answer))
    