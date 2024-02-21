from dotenv import load_dotenv
load_dotenv()
from experiment.experiment import run_experiment

import os

if __name__ == '__main__':
    print(os.getenv("OPENAI_API_KEY"))  # Temporarily added for debugging
    run_experiment()
