from dotenv import load_dotenv
load_dotenv()
from experiment.chain_experiment import main_run_experiments
from chain import chain
import os
from config import *
from experiment.prompt_improved_experiment import *
from util import util, dataset

def storeGSM8KData(split,filename):
    path = os.path.join(GSM8KOGDATA, f"{split}.jsonl")
    output_path = os.path.join(GSM8KCATDATA, f"{filename}.jsonl")
    data = util.categorize_dataset(path)
    util.store_category(output_path,data)

if __name__ == '__main__':
    augmentPromptExperiment()
    

    
    
