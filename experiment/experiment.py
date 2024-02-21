from dotenv import load_dotenv
from .experiment_chain.chain import get_summary_chain

def run_experiment():
    input = "If you have 1 cat, your grandpa gave you another cat, how many cats do you have?"
    
    mainChain = get_summary_chain()
    print(mainChain.run(information=input))

