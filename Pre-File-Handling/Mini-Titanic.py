pythonCopyEditdata = [
    {"sex": "female", "age": 25, "pclass": 1, "survived": 1},
    {"sex": "male",   "age": 35, "pclass": 1, "survived": 0},
    {"sex": "female", "age": 17, "pclass": 3, "survived": 1},
    {"sex": "male",   "age": 8,  "pclass": 3, "survived": 1},
    {"sex": "male",   "age": 28, "pclass": 3, "survived": 0},
    {"sex": "female", "age": 40, "pclass": 2, "survived": 1},
    {"sex": "male",   "age": 52, "pclass": 2, "survived": 0},
    {"sex": "female", "age": 5,  "pclass": 3, "survived": 1},
    {"sex": "male",   "age": 19, "pclass": 1, "survived": 1},
    {"sex": "male",   "age": 44, "pclass": 3, "survived": 0},
    {"sex": "female", "age": 32, "pclass": 1, "survived": 1},
    {"sex": "male",   "age": 10, "pclass": 2, "survived": 0},
]

total = len(pythonCopyEditdata)

# Actual Survival/ Not Survival counts
actual_survival_count = 0
for x in pythonCopyEditdata:
    if x['survived'] == 1:
        actual_survival_count += 1

actual_not_survival_count = total - actual_survival_count

play = True

while play == True:
    def predict_survival(sex, age, pclass):
        if sex == 'female':
            return 1

        elif int(age) < 25 :
            return 1

        elif pclass == '1' or pclass == '3':
            return 1
        
        else:
            return 0


    survived_message = ['DID NOT', 'DID']

    print("\n1 = Single prediction (user types one passenger's features)\n2 = Evaluate on sample dataset (program runs through records and prints accuracy)\nMODE: (1/2)")
    mode = input('-')

    if mode == '1':

        print('Sex: (MALE/FEMALE)')
        sex = input('-').lower()
        if sex == 'male' or sex == 'female':
            print('Age: (0-100)')
            age = input('-')
            if 0 < int(age) < 100:

                print('Pclass: (1/2/3)')
                check = False
                while not check:
                    pclass = input('-')
                    if 1<= int(pclass) <= 3:
                        check = True
                
                    
                    survived = predict_survival(sex, age, pclass)
                    print(survived_message[survived], 'SURVIVE')

    # Mode 2

    elif mode == '2':
        
        correct_predictions = 0
        predicted_survive = 0
        predicted_not_survive = 0

        for item in pythonCopyEditdata:
            actual_survival = item['survived']
            
            predicted = predict_survival(item['sex'], item['age'], item['pclass'])
            if actual_survival == predicted:
                correct_predictions += 1
            if predicted == 1:
                predicted_survive += 1
                


        Accuracy_percentage = (correct_predictions / total) * 100
        print('Accuracy percentage: ', Accuracy_percentage, '%')

        


        predicted_not_survive = total - predicted_survive
        
        

        print('Predicted SURVIVE: ', predicted_survive, ', Predicted NOT SURVIVE: ', predicted_not_survive)
        print('Actual SURVIVE: ', actual_survival_count, ', Actual NOT SURVIVE: ', actual_not_survival_count)

    print('Run again? (y/n):')
    ask = input('').lower()
    if ask == 'y':
        play = True
    elif ask == 'n':
        break



      ########## Alternate to predict_survival function ##########

# print("\n1 = Single prediction (user types one passenger's features)\n2 = Evaluate on sample dataset (program runs through records and prints accuracy)\nMODE: (1/2)")
# check = False
# while not check:
#     mode = input('-')
#     if mode == '1' or mode == '2':
#             check1 = True
#             if mode == '1':

#                 print('Sex: (MALE/FEMALE)')
#                 check1 = False
#                 while not check1:
#                     sex = input('-').lower()
#                     if sex == 'male' or sex == 'female':
#                         check1 = True

#                 check2 = False
#                 print('Age: (0-100)')
#                 while not check2:                       
#                     age = input('-')
#                     if age.isdigit() and 0 <= int(age) <= 100:
#                             check2 = True
                        
#                     else:
#                         check2 = False

#                 check3 = False
#                 print('Pclass: (1/2/3)')
#                 while not check3:
#                     pclass = input('-')
                    
#                     if pclass.isdigit () and 1<= int(pclass) <= 3:
#                         check3 = True
#                         break
#                     else:
#                         check3 = False