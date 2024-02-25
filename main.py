from dotenv import load_dotenv
load_dotenv()
from experiment.experiment import main_run_experiments
import os
from config import *


if __name__ == '__main__':
    print(os.getenv("OPENAI_API_KEY"))  # Temporarily added for debugging
    main_run_experiments([BASEEXP,FSEXP, COTEXP])
    
