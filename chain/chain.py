from langchain.chains import LLMChain
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

# from output_parsers import summary_parser, ice_breaker_parser, topics_of_interest_parser

# llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
# llm = ChatOpenAI(temperature=0.7, model_name="gpt-4")
llm = ChatOpenAI(temperature=0.7, model_name="gpt-3.5-turbo")

def get_default_chain() -> LLMChain:
    summary_template = """
         You are given a math question {information}, think through it step by step and provide me 
         
         1. step by step reasoning
         2. Provide the answer as a integer at the end with four '#' and one space character before it. Don't put unit or '%' sign in the final answer. one number only 
         For example:
         ```It takes 2/2=<<2/2=1>>1 bolt of white fiber\nSo the total amount of fabric is 2+1=<<2+1=3>>3 bolts of fabric\n#### 3```
         \n
     """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"],
        template=summary_template
    )

    return LLMChain(llm=llm, prompt=summary_prompt_template)

def get_chain_of_thought_chain() -> LLMChain:
    summary_template = """
         You are given a math question {information}, think through it step by step and provide me 
         
         1. step by step reasoning
         2. Provide the answer as a integer at the end with four '#' and one space character before it. Don't put unit or '%' sign in the final answer. one number only 
        For example:
         ```It takes 2/2=<<2/2=1>>1 bolt of white fiber\nSo the total amount of fabric is 2+1=<<2+1=3>>3 bolts of fabric\n#### 3```
         \n
         Here are few shot example:
         "question": "At 30, Anika is 4/3 the age of Maddie. What would be their average age in 15 years?", "answer": "If Anika is 30 now, in 15 years, she'll be 30+15=<<30+15=45>>45 years old.\nAt 30, Anika is 4/3 the age of Maddie, meaning Maddie is 4/3*30=<<4/3*30=40>>40 years.\nIn 15 years, Maddie will be 40+15=<<40+15=55>>55 years old.\nTheir total age in 15 years will be 55+45=<<55+45=100>>100\nTheir average age in 15 years will be 100/2=<<100/2=50>>50\n#### 50"
         \n
         "question": "Janet, a third grade teacher, is picking up the sack lunch order from a local deli for the field trip she is taking her class on. There are 35 children in her class, 5 volunteer chaperones, and herself. She she also ordered three additional sack lunches, just in case there was a problem. Each sack lunch costs $7. How much do all the lunches cost in total?", "answer": "Janet needs 35 lunches for the kids + 5 for the chaperones + 1 for herself + 3 extras = <<35+5+1+3=44>>44 lunches.\nEach lunch is $7, so lunch for the field trip costs $7 per lunch * 44 lunches = $<<7*44=308>>308 total\n#### 308"
         \n
         "question": "Colin can skip at six times the speed that Brandon can.  Brandon can skip at one-third the speed that Tony can.  And Tony can skip at twice the speed that Bruce can.  At what speed, in miles per hour, can Colin skip if Bruce skips at 1 mile per hour?", "answer": "Tony can skip at twice the speed that Bruce can, for a speed of 1*2=<<1*2=2>>2 miles per hour.\nBrandon can skip at one-third the speed that Tony can, for a speed of 2*(1/3) = 2/3 miles per hour.\nColin can skip at six times the speed that Brandon can, for a speed of (2/3*6=4 miles per hour).\n#### 4"
         \n
         "question": "Josh is saving up for a box of cookies. To raise the money, he is going to make bracelets and sell them. It costs $1 for supplies for each bracelet and he sells each one for $1.5. If he makes 12 bracelets and after buying the cookies still has $3, how much did the box of cookies cost?", "answer": "He makes $.5 profit on each bracelet because 1.5 - 1 = <<1.5-1=.5>>.5\nHe earns $6 because 12 x .5 = <<12*.5=6>>6\nThe cookies cost $3 because 6 - 3 = <<6-3=3>>3\n#### 3"
         \n
         "question": "Very early this morning, Elise left home in a cab headed for the hospital. Fortunately, the roads were clear, and the cab company only charged her a base price of $3, and $4 for every mile she traveled. If Elise paid a total of $23, how far is the hospital from her house?", "answer": "For the distance she traveled, Elise paid 23 - 3 = <<23-3=20>>20 dollars\nSince the cost per mile is $4, the distance from Elise\u2019s house to the hospital is 20/4 = <<20/4=5>>5 miles.\n#### 5"
         \n
         "question": "Roy owns a refrigerated warehouse where he stores produce before selling it at the farmer\u2019s market.  The fruits and vegetables he stores are very sensitive to temperature, and he must keep them all cold or they will spoil.  One day, the power went out and the air conditioner was turned off for three hours, during which time the temperature rose by 8 degrees per hour.  If Roy gets the power back on, it will activate the air conditioner to lower the temperature at the rate of 4 degrees F per hour.  What is the amount of time, in hours, it will take for the air conditioner to restore the warehouse to 43 degrees F?", "answer": "At a rate of 8 degrees per hour, in three hours the temperature rose by 3*8=<<3*8=24>>24 degrees.\nAt a rate of 4 degrees per hour, the air conditioner can reduce the temperature 24 degrees in 24/4=6 hours.\n#### 6"
         \n
         "question": "Janet pays $40/hour for 3 hours per week of clarinet lessons and $28/hour for 5 hours a week of piano lessons. How much more does she spend on piano lessons than clarinet lessons in a year?", "answer": "First find the total Janet spends on clarinet lessons per week: $40/hour * 3 hours/week = $<<40*3=120>>120/week\nThen find the total Janet spends on piano lessons per week: $28/hour * 5 hours/week = $<<28*5=140>>140/week\nThen subtract her weekly clarinet spending from her weekly piano spending to find the weekly difference: $140/week - $120/week = $<<140-120=20>>20/week\nThen multiply the weekly difference by the number of weeks in a year to find the annual difference: $20/week * 52 weeks/year = $<<20*52=1040>>1040/year\n#### 1040"
     """
    summary_prompt_template = PromptTemplate(
        input_variables=["information"],
        template=summary_template
    )
    return LLMChain(llm=llm, prompt=summary_prompt_template)


def get_few_shot_prompting() -> LLMChain:
    summary_template = """
         You are given a math question {information}, think through it step by step and provide me 
         
         1. step by step reasoning
         2. Provide the answer as a integer at the end with four '#' and one space character before it. Don't put unit or '%' sign in the final answer. one number only 
         For example:
         ```It takes 2/2=<<2/2=1>>1 bolt of white fiber\nSo the total amount of fabric is 2+1=<<2+1=3>>3 bolts of fabric\n#### 3```
         \n
         Here are few shot example:
         "question": "At 30, Anika is 4/3 the age of Maddie. What would be their average age in 15 years?", "answer": "#### 50"
         \n
         "question": "Janet, a third grade teacher, is picking up the sack lunch order from a local deli for the field trip she is taking her class on. There are 35 children in her class, 5 volunteer chaperones, and herself. She she also ordered three additional sack lunches, just in case there was a problem. Each sack lunch costs $7. How much do all the lunches cost in total?", "answer": "#### 308"
         \n
         "question": "Colin can skip at six times the speed that Brandon can.  Brandon can skip at one-third the speed that Tony can.  And Tony can skip at twice the speed that Bruce can.  At what speed, in miles per hour, can Colin skip if Bruce skips at 1 mile per hour?", "answer": "#### 4"
         \n
         "question": "Josh is saving up for a box of cookies. To raise the money, he is going to make bracelets and sell them. It costs $1 for supplies for each bracelet and he sells each one for $1.5. If he makes 12 bracelets and after buying the cookies still has $3, how much did the box of cookies cost?", "answer": "#### 3"
         \n
         "question": "Very early this morning, Elise left home in a cab headed for the hospital. Fortunately, the roads were clear, and the cab company only charged her a base price of $3, and $4 for every mile she traveled. If Elise paid a total of $23, how far is the hospital from her house?", "answer": "#### 5"
         \n
         "question": "Roy owns a refrigerated warehouse where he stores produce before selling it at the farmer\u2019s market.  The fruits and vegetables he stores are very sensitive to temperature, and he must keep them all cold or they will spoil.  One day, the power went out and the air conditioner was turned off for three hours, during which time the temperature rose by 8 degrees per hour.  If Roy gets the power back on, it will activate the air conditioner to lower the temperature at the rate of 4 degrees F per hour.  What is the amount of time, in hours, it will take for the air conditioner to restore the warehouse to 43 degrees F?", "answer": "#### 6"
         \n
         "question": "Janet pays $40/hour for 3 hours per week of clarinet lessons and $28/hour for 5 hours a week of piano lessons. How much more does she spend on piano lessons than clarinet lessons in a year?", "answer": "#### 1040"
     """
    summary_prompt_template = PromptTemplate(
        input_variables=["information"],
        template=summary_template
    )
    return LLMChain(llm=llm, prompt=summary_prompt_template)




def get_default_aug_chain() -> LLMChain:
    summary_template = """
         You are given a math question {information}, think through it step by step and provide me 
         
         1. step by step reasoning
         2. Check your reasoning against the question sentence by sentence
         3. Provide the answer as a integer at the end with four '#' and one space character before it. Don't put unit or '%' sign in the final answer. one number only 
         For example:
         ```It takes 2/2=<<2/2=1>>1 bolt of white fiber\nSo the total amount of fabric is 2+1=<<2+1=3>>3 bolts of fabric\n#### 3```
         \n
         Here are some similar problems and answers for your reference (Could be none): 
         {relatedProblems}

         \n 
         
     """

    summary_prompt_template = PromptTemplate(
        input_variables=["information","relatedProblems"],
        template=summary_template
    )

    return LLMChain(llm=llm, prompt=summary_prompt_template)


def get_data_enhancement_chain():
    summary_template = """
         You are given a math question, with detailed answer.
         The answer will contains multiple equations for different steps
         Now do the following:
         1. Read question and understand the solution
         2. Understand how many variables there are in equations.
         3. Extract all equations in and put them in a single <<>> seperate by comma ','
         4. Replace the numbers in the euqations with different variable name starting with Captial A. The final answer should be represent with variable Z
         5. Create a mapping for from variable name to value.
         6. Re read your transfered equation. There must be no numbers in it. If yes, replace those numbers
         7. with the variable equations you conclude, map the number back and check whether the answer is the same. If not, correct your mistake
         8. Re read again your transfered equation. There must be no numbers in it. If yes, replace those numbers
         9. Return only the varible version result encapsulate with << >> 
    
         For example:
        "question": "Natalia sold clips to 48 of her friends in April, and then she sold half as many clips in May. How many clips did Natalia sell altogether in April and May?\n", 
        "answer": "Natalia sold 48/2 = <<48/2=24>>24 clips in May.\nNatalia sold 48+24 = <<48+24=72>>72 clips altogether in April and May.\n#### 72<|endoftext|>"
         You will return:
         <<A/B=C, A+C=D>>
         \n

         Remeber:
        1. Consider those numbers that are representing some constant factors as variables as well.
        2. The final answer should be represent by letter Z
        3. Represent fractions like 3/4 as a single variable
        Here are some examples:
        {relatedProblems}
         Here is the actual question and answer:
         {question}
         {answer}
     """

    summary_prompt_template = PromptTemplate(
        input_variables=["question", "answer", "relatedProblems"],
        template=summary_template
    )

    return LLMChain(llm=llm, prompt=summary_prompt_template)

def get_review_mistake_chain()->LLMChain:
    prompt = """
         You are given a math question, with detailed answer, and an incorrect answer generated by GPT3.5.
         Now do the following:
         1. Read question and understand the solution
         2. Understand how many variables there are in equations.
         3. Understand and summarize why you make mistake on these question
         4. Summarize a key takeaway from this mistake
         5. output the key takeaway in one sentence
         \n
         Here is the actual question ,answer, and incorrect answer:
         {question}
         {answer}
         {incorrect_answer}


         output the key take away in the folloing format:
         <<1. ...
           2. ...
            >>
     """
    summary_prompt_template = PromptTemplate(
        input_variables=["question", "answer", "incorrect_answer"],
        template=prompt
    )

    return LLMChain(llm=llm, prompt=summary_prompt_template)