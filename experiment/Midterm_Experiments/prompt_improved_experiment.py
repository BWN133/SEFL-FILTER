from config import *
import os
from util import dataset, util
from chain.chain import *
from experiment.Midterm_Experiments.experiment_main import *
from experiment.Midterm_Experiments.chain_experiment import *
def augmentPromptExperiment():
    # storeGSM8KData("train", "train_opc")
    path = os.path.join(GSM8KCATDATA,"train_opc.jsonl")
    bank = dataset.read_jsonl(path, MAXINT)[0]
    # path = os.path.join(GSM8KOGDATA + "test.jsonl")
    # main_run_experiments([BASEEXP],path)
    experiment_result = dataset.read_jsonl(RESULTOGPATH + "BaseResult.jsonl", MAXINT)
    curChain = get_default_aug_chain()
    noAugChain = get_chain_of_thought_chain()
    correct, model_completion, incorrectAnswer = run_experiment(curChain,experiment_result,bank)
    util.store_result(BASEOPCATEXP, correct, incorrectAnswer, RESULTAUGOGPATH + "BaseModel.jsonl")
    correct_noAug, model_completion_noAug, incorrectAnswer_noAug = run_experiment(noAugChain,experiment_result)
    util.store_result(BASEOPCATEXP, correct_noAug, incorrectAnswer_noAug, RESULTAUGOGPATH + "BaseModel_noAug.jsonl")


# Run the augmented trainset 
def augmentExperimentOnDataset():
    curChain = get_default_aug_chain()
    no_aug_chain = get_chain_of_thought_chain()
    path = os.path.join(GSM8KCATDATA,"train_opc.jsonl")
    bank = dataset.read_jsonl(path, MAXINT)[0]
    question_path = os.path.join(GSM8KOGDATA, "test.jsonl")
    target_questions = dataset.get_examples(question_path, TESTINGAMOUNT)
    
    correct, model_completion, incorrectAnswer = run_experiment(curChain,target_questions,bank)
    util.store_result(BASEOPCATEXP_TESTSET, correct, incorrectAnswer, RESULTAUGOGPATH + "BaseModel_test_aug_exp2_500.jsonl")
    # correct_noAug, model_completion_noAug, incorrectAnswer_noAug = run_experiment(no_aug_chain,target_questions)
    # util.store_result(BASEOPCATEXP_TESTSET + "no Augment", correct_noAug, incorrectAnswer_noAug, RESULTAUGOGPATH + "BaseModel_ChainOfThought_exp1_500.jsonl")
    
    
    
    
    
    
    
            
    