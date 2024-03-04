TESTINGAMOUNT = 100
UPPERAINT = 65
MAXINT = 9999999
INCORRECTSAMPLEKEY = "Incorrect Samples"
ANSWERKEY = "answer"
QUESTIONKEY = "question"
VERBOSE = False
BASEEXP = "Base Experiment"
COTEXP = "Chain Of Thought Prompting"
FSEXP = "Few Shot Prompting"
BASEOPCATEXP = "Base Prompting Operation Categorization Augmented"
BASEOPCATEXP_TESTSET = "Base Prompting Operation Categorization Augmented on Test Set"
RESULTOGPATH = "Results/DEFAULT_METHOD/OgData/"
RESULTAUGOGPATH = "Results/AUGMENTED_METHOD/OgData/"
GSM8KOGDATA = "Dataset/GSM8K/OgData/"
GSM8KCATDATA = "Dataset/GSM8K/CategorizedData/"

DEFAULTCOTPROMPT = """
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
