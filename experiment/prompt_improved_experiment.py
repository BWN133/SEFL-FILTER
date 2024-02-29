from config import *
import os
from util import dataset, util
from chain.chain import *
from experiment.experiment_main import *
from experiment.chain_experiment import *
def augmentPromptExperiment():
    # storeGSM8KData("train", "train_opc")
    path = os.path.join(GSM8KCATDATA,"train_opc.jsonl")
    bank = dataset.read_jsonl(path, MAXINT)[0]
    # path = os.path.join(GSM8KOGDATA + "test.jsonl")
    # main_run_experiments([BASEEXP],path)
    experiment_result = dataset.read_jsonl(RESULTOGPATH + "BaseResult.jsonl", MAXINT)
    curChain = get_default_aug_chain()
    noAugChain = get_default_chain()
    # correct, model_completion, incorrectAnswer = run_experiment(curChain,experiment_result,bank)
    # util.store_result(BASEOPCATEXP, correct, incorrectAnswer, RESULTAUGOGPATH + "BaseModel.jsonl")
    correct_noAug, model_completion_noAug, incorrectAnswer_noAug = run_experiment(noAugChain,experiment_result)
    util.store_result(BASEOPCATEXP, correct_noAug, incorrectAnswer_noAug, RESULTAUGOGPATH + "BaseModel_noAug.jsonl")
            
            
    