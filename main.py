from dotenv import load_dotenv
load_dotenv()
from experiment.experiment import main_run_experiments
from chain import chain
import os
from config import *
from experiment.prompt_improved_experiment import *


def prompt_experiment():
    test1 = "The cost of the house and repairs came out to 80,000+50,000=$<<80000+50000=130000>>130,000\nHe increased the value of the house by 80,000*1.5=<<80000*1.5=120000>>120,000\nSo the new value of the house is 120,000+80,000=$<<120000+80000=200000>>200,000\nSo he made a profit of 200,000-130,000=$<<200000-130000=70000>>70,000\n#### 70000<|endoftext|>"
    categorizer(test1)

if __name__ == '__main__':
    # print(os.getenv("OPENAI_API_KEY"))  # Temporarily added for debugging
    # main_run_experiments([BASEEXP,FSEXP, COTEXP])
    prompt_experiment()
    
    
