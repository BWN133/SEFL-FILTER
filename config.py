TESTINGAMOUNT = 500
UPPERAINT = 65
SOLUTIONCANDIDATE = 3
MAXINT = 9999999
INCORRECTSAMPLEKEY = "Incorrect Samples"
INCORRECTANSWERKEY = "Incorrect Answer"
ANSWERKEY = "answer"
QUESTIONKEY = "question"
SOLUTIONKEY = "solution"
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


DEFAULTCOTPROMPTARRAY = [{"question": "At 30, Anika is 4/3 the age of Maddie. What would be their average age in 15 years?", "answer": "#### 50"},
                         {"question": "Janet, a third grade teacher, is picking up the sack lunch order from a local deli for the field trip she is taking her class on. There are 35 children in her class, 5 volunteer chaperones, and herself. She she also ordered three additional sack lunches, just in case there was a problem. Each sack lunch costs $7. How much do all the lunches cost in total?", "answer": "#### 308"},
                         {"question": "Colin can skip at six times the speed that Brandon can.  Brandon can skip at one-third the speed that Tony can.  And Tony can skip at twice the speed that Bruce can.  At what speed, in miles per hour, can Colin skip if Bruce skips at 1 mile per hour?", "answer": "#### 4"},
                         {"question": "Josh is saving up for a box of cookies. To raise the money, he is going to make bracelets and sell them. It costs $1 for supplies for each bracelet and he sells each one for $1.5. If he makes 12 bracelets and after buying the cookies still has $3, how much did the box of cookies cost?", "answer": "#### 3"},
                         {"question": "Very early this morning, Elise left home in a cab headed for the hospital. Fortunately, the roads were clear, and the cab company only charged her a base price of $3, and $4 for every mile she traveled. If Elise paid a total of $23, how far is the hospital from her house?", "answer": "#### 5"},
                         {"question": "Roy owns a refrigerated warehouse where he stores produce before selling it at the farmer\u2019s market.  The fruits and vegetables he stores are very sensitive to temperature, and he must keep them all cold or they will spoil.  One day, the power went out and the air conditioner was turned off for three hours, during which time the temperature rose by 8 degrees per hour.  If Roy gets the power back on, it will activate the air conditioner to lower the temperature at the rate of 4 degrees F per hour.  What is the amount of time, in hours, it will take for the air conditioner to restore the warehouse to 43 degrees F?", "answer": "#### 6"},
                         {"question": "Janet pays $40/hour for 3 hours per week of clarinet lessons and $28/hour for 5 hours a week of piano lessons. How much more does she spend on piano lessons than clarinet lessons in a year?", "answer": "#### 1040"}]


DEFAULTAUGDATAPROMPTARRAY = [
{"input": '''"question": "Dana can run at a rate of speed four times faster than she can walk, but she can skip at a rate of speed that is half as fast as she can run. If she can skip at 3 miles per hour, how many miles can she travel in six hours if she spends one-third of the time running and two-thirds of the time walking?", "answer": "If Dana can skip at half the speed she can run, then she can run at 3*2=<<3*2=6>>6 miles per hour.\nAnd since she can run at a speed that is 4 times faster than she can walk, this means she can walk at 6/4=1.5 miles per hour.\nIf two-thirds of the time is spent walking, then she walks for 6*(2/3)=<<6*(2/3)=4>>4 hours.\nIf one-third of the time is spent running, then she runs for 6-4=<<6-4=2>>2 hours.\nThus, she runs for 2 hours at 6 miles per hour, or 2*6=<<2*6=12>>12 miles.\nShe walks for 4 hours at 1.5 miles per hour, or 4*1.5=<<4*1.5=6>>6 miles.\nThus, altogether, she travels 12+6=<<12+6=18>>18 miles.\n#### 18"''', "output": "<<A*B=C, A-C=D, D*E=F, C*G=H, F+H=Z>>"},
{"input": '''"question": "Brandon's iPhone is four times as old as Ben's iPhone. Ben's iPhone is two times older than Suzy's iPhone. If Suzy\u2019s iPhone is 1 year old, how old is Brandon\u2019s iPhone?", "answer": "Ben\u2019s iPhone is 1*2 = <<1*2=2>>2 years old.\nBrandon\u2019s iPhone is 4*2 = <<4*2=8>>8 years old.\n#### 8"''', "output": "<<A*B=C, C*B=Z>>"},
{"input":'''"question": "The great dragon, Perg, sat high atop mount Farbo, breathing fire upon anything within a distance of 1000 feet.  Polly could throw the gold javelin, the only known weapon that could sleigh the dragon, for a distance of 400 feet, well within the reach of the dragon's flames.  But when Polly held the sapphire gemstone, she could throw the javelin three times farther than when not holding the gemstone. If holding the gemstone, how far outside of the reach of the dragon's flames could Polly stand and still hit the dragon with the gold javelin?", "answer": "With the gemstone, Polly could throw the javelin 3 times farther than 400 feet, for a distance of 3*400=<<3*400=1200>>1200 feet.\n1200 feet is beyond the 1000-foot reach of the dragon's flames by a distance of 1200-1000=<<1200-1000=200>>200 feet.\n#### 200"''',"<<output":"A*B=C, C-D=Z>>"},
{"input": '''"question": "Grandma Jones baked 5 apple pies for the fireman's luncheon.  She cut each pie into 8 pieces and set the five pies out on the buffet table for the guests to serve themselves.  At the end of the evening, after the guests had taken and eaten their pieces of pie, there were 14 pieces of pie remaining.  How many pieces were taken by the guests?", "answer": "To start the evening, there were 5 pies, each with 8 pieces, which is 5*8=<<5*8=40>>40 pieces of pie.\nIf only 14 remained, then 40-14=<<40-14=26>>26 pieces of pie had been taken by guests.\n#### 26"''', "output": "<<A*B=C, C-D=Z>>"},
{"input":'''"question": "According to its nutritional info, a bag of chips has 250 calories per serving. If a 300g bag has 5 servings, how many grams can you eat if your daily calorie target is 2000 and you have already consumed 1800 calories?", "answer": "If the total calorie target is 2000 and I have consumed 1800 calories then I have 2000-1800 = <<2000-1800=200>>200 calories left to eat\nIf each serving of chips has 250 calories and I only have 200 calories left to eat, then I can only eat 200/250 of a serving = 4/5 of a serving\nWe also know that a 300g bag of chips has 5 servings, hence each serving has 300g/5 = <<300/5=60>>60 grams\nIf I can only eat 4/5 of a serving, then I can eat only 60g * 4/5 = 240g/5 = 48 grams\n#### 48"''',"output":"<<A-B=C,C/D=E, F/G=H, H*E=Z>>"},
]

a = "A + B = C, c_1 * A = E, E + B = F ,F + C = G, G/c_2 = Z"