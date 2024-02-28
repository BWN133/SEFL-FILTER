from config import *
import os
from util import dataset, util
from chain.chain import *
def augmentPromptExperiment():
    # storeGSM8KData("train", "train_opc")
    path = os.path.join(GSM8KCATDATA,"train_opc.jsonl")
    data = dataset.read_jsonl(path, MAXINT)[0]
    # path = os.path.join(GSM8KOGDATA + "test.jsonl")
    # main_run_experiments([BASEEXP, COTEXP,FSEXP],path)
    experiment_result = dataset.read_jsonl(RESULTOGPATH + "BaseResult.jsonl", MAXINT)
    
    for t in experiment_result:
        if ANSWERKEY in t:
            curK = util.operation_categorizer(t[ANSWERKEY])
            supData = data[curK]
            curChain = get_default_aug_chain()
            print(curChain.run(information=t[QUESTIONKEY], relatedProblems=supData))
            
            
    