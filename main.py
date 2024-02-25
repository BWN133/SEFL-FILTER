from dotenv import load_dotenv
load_dotenv()
from experiment.experiment import run_experiment
from Dataset import dataset

import os

TESTINGAMOUNT = 5


if __name__ == '__main__':
    print(os.getenv("OPENAI_API_KEY"))  # Temporarily added for debugging
    # run_experiment()
    test_data = dataset.get_examples("test",TESTINGAMOUNT)
    model_completion = []
    incorrectAnswer = []
    correct = 0
    for i in range(TESTINGAMOUNT):
        cur_question = test_data[i]['question']
        model_completion.append(run_experiment(test_data[i]["question"]))
        if dataset.is_correct(model_completion[-1],test_data[i]):
            correct += 1
        else:
            incorrectAnswer.append((test_data[i]['answer'], model_completion[-1]))
    print("Total Correct Rate ", correct/ TESTINGAMOUNT)
    for t in incorrectAnswer:
        print("Correct Answer: ", t[0])
        print("Model's Prediction: ", t[1])
    
