from dotenv import load_dotenv
from .experiment_chain.chain import get_summary_chain

def run_experiment(input_question):
    mainChain = get_summary_chain()
    return mainChain.run(information=input_question)

