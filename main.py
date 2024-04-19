from dotenv import load_dotenv
load_dotenv()
from experiment.chain_experiment import *
from chain import chain
import os
from config import *
from experiment.prompt_improved_experiment import *
from util import util, dataset, discard_functions
from Pipe import pipe
from Pipe import tester
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

if __name__ == '__main__':
    # ehanceData_run_experiments(RESULTAUGOGPATH +"BaseModel_noAug.jsonl")
    # main_run_experiments([COTEXP], GSM8KOGDATA+"train.jsonl", data_length=1500)
    question = "Two trains leave San Rafael at the same time. They begin traveling westward, both traveling for 80 miles. The next day, they travel northwards, covering 150 miles. What's the distance covered by each train in the two days?\n"
    pipe.main_pipe(question=question)
    # tester.test_recheck_chain()
    
    
    
