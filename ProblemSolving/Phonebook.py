dict = {
     "Ali": "1234",   
     "Sara": "5678"
         }

valid = True
while valid == True:
    count = 0 
    print('\nEnter Name:')
    names = input('~ ')
    for item in dict:
        if item == names:
            print('\nName:', names, '\nNumber:', dict[item])

    else:
        print('\n- Not found -')