from dotenv import load_dotenv
load_dotenv()
from experiment.Midterm_Experiments.chain_experiment import *
from chain import chain
import os
from config import *
from experiment.Midterm_Experiments.prompt_improved_experiment import *
from util import util, dataset, discard_functions
from Pipe import pipe
from Pipe import tester
from experiment.Final_Experiments import experiment
def storeGSM8KData(split,filename):
    path = os.path.join(GSM8KOGDATA, f"{split}.jsonl")
    output_path = os.path.join(GSM8KCATDATA, f"{filename}.jsonl")
    data = util.categorize_dataset(path)
    util.store_category(output_path,data)

def storeGSM8KData_EXACT(split, filename):
    path = os.path.join(GSM8KOGDATA, f"{split}.jsonl")
    output_path = os.path.join(GSM8KCATDATA, f"{filename}.jsonl")
    data = discard_functions.categorize_dataset_exact(path)
    util.store_category(output_path,data)
    
def count_single(path):
    data = dataset.read_jsonl(path,100)
    total = 0
    category_with_one_data = 0
    total_category = 0
    for d in data[0]:
        curL = len(data[0][d])
        total += curL
        total_category += 1
        if curL == 1:
            category_with_one_data += 1
    print(total, category_with_one_data, total_category)

def count_different(path1, path2):
    data = dataset.read_jsonl(path1,MAXINT)
    bank = set()
    for d in data:
        bank.add(d[QUESTIONKEY]) if QUESTIONKEY in d else None
    data2 = dataset.read_jsonl(path2,MAXINT)
    count = 0
    for d in data2:
        if QUESTIONKEY in d and d[QUESTIONKEY] in bank:
            count += 1
    return count

def print_correct_solution_generate_rate():
    main_rate = experiment.correct_solution_generate_rate("Results\STUDIABILITY_PIPE_METHOD\Studiability_Result_Total1_100.jsonl")
    varience_main_2 = experiment.correct_solution_generate_rate("Results\STUDIABILITY_PIPE_METHOD\Studiability_Result_Total_2_1_100.jsonl")
    varience_no_random = experiment.correct_solution_generate_rate("Results\STUDIABILITY_PIPE_METHOD\Studiability_Result_Total_no_random_1_100.jsonl")
    varience_no_enhancement = experiment.correct_solution_generate_rate("Results\STUDIABILITY_PIPE_METHOD\Studiability_Result_Total_no_enhancement_6c_1_100.jsonl")
    print("SELF-FILTER average num of candidates: " + str(main_rate))
    print("SELF-FILTER 2 average num of candidates: " + str(varience_main_2))
    print("No Random average num of candidates: " + str(varience_no_random))
    print("No enhancement average num of candidates: " + str(varience_no_enhancement))

def print_average_num_candidate():
    varience_main = experiment.count_variation("Results\STUDIABILITY_PIPE_METHOD\Studiability_Result_Total1_100.jsonl")
    varience_main_2 = experiment.count_variation("Results\STUDIABILITY_PIPE_METHOD\Studiability_Result_Total_2_1_100.jsonl")
    varience_no_random = experiment.count_variation("Results\STUDIABILITY_PIPE_METHOD\Studiability_Result_Total_no_random_1_100.jsonl")
    varience_no_enhancement = experiment.count_variation("Results\STUDIABILITY_PIPE_METHOD\Studiability_Result_Total_no_enhancement_6c_1_100.jsonl")
    print("SELF-FILTER average num of candidates: " + str(varience_main))
    print("SELF-FILTER average num of candidates: " + str(varience_main_2))
    print("No Random average num of candidates: " + str(varience_no_random))
    print("No enhancement average num of candidates: " + str(varience_no_enhancement))

def print_correctlyPickRate():
    varience_main = experiment.correctly_pick_generate_rate("Results\STUDIABILITY_PIPE_METHOD\Studiability_Result_Total1_100.jsonl")
    varience_main_2 = experiment.correctly_pick_generate_rate("Results\STUDIABILITY_PIPE_METHOD\Studiability_Result_Total_2_1_100.jsonl")
    varience_no_random = experiment.correctly_pick_generate_rate("Results\STUDIABILITY_PIPE_METHOD\Studiability_Result_Total_no_random_1_100.jsonl")
    varience_no_enhancement = experiment.correctly_pick_generate_rate("Results\STUDIABILITY_PIPE_METHOD\Studiability_Result_Total_no_enhancement_6c_1_100.jsonl")
    print("SELF-FILTER average num of candidates: " + str(varience_main))
    print("SELF-FILTER average num of candidates: " + str(varience_main_2))
    print("No Random average num of candidates: " + str(varience_no_random))
    print("No enhancement average num of candidates: " + str(varience_no_enhancement))
if __name__ == '__main__':
    # print_correct_solution_generate_rate()
    print_correctlyPickRate()
    # experiment.abalation_no_enhancement_experiment(1,100)
    # experiment.studiability_result(1,100)
    # print_average_num_candidate()
    #tester.test_system3()
    # question = "Tony can run a mile twice as fast as Tina, who with a time of 6 minutes is one-third as fast a runner as Tom.  What are all three of their mile times when added together?"
    # pipe.main_pipe(question=question)
    
    
