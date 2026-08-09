mylist =[] 

run = True




while run == True:
    print("\n(1) Add a new task\n(2) View all tasks\n(3) Mark a task as done\n(4) Delete a task\n(5) SEARCH a task\n(6) Exit\n ")
    menu = input('-')

    if menu == '1':
        print("\nEnter task:\n")
        added = input('')
        mylist.append({"Task": added, "Done": False})



    if menu == '2':
        num = 1
        for item in mylist:
            check = item["Done"]
            checkmark = ''
            if check == True:
                checkmark = 'x'
            elif check == False:
                checkmark = ' '
            print(str(num)+'. ['+checkmark+']'+item["Task"])
            num += 1 



    if menu == '3':
        num = 1
        print('')
        for item in mylist:
            check = item["Done"]

            if check == True:
                
                checkmark = 'x'

                
            elif check == False:
                checkmark = ' '

            print(str(num)+'. ['+checkmark+']'+item["Task"])
            num += 1
                
        
        print('\nNumber of DONE task:')  
        numdone = int(input('')) - 1
        mylist[numdone]["Done"] = True

         

    if menu == '4':
        
        num = 1
        for item in mylist:
            check = item["Done"]
            checkmark = ''
            if check == True:
                checkmark = 'x'
            elif check == False:
                checkmark = ' '
            print(str(num)+'. ['+checkmark+']'+item["Task"])
            num += 1 



        print('Pick task you want deleted\n')
        remove = int(input('-'))
        numremove = remove - 1
        mylist.pop(numremove)



    if menu == '5':
        print('\nPlease enter what you are searching for.\n')
        search = input('')
        num = 1
        for item in mylist:
            
            if search in item['Task']:
                check = item["Done"]
                checkmark = ''
                if check == True:
                    checkmark = 'x'
                elif check == False:
                    checkmark = ' '
                print(str(num)+'. ['+checkmark+']'+item["Task"])
                num += 1 
        
        
    if menu == '6':
        run = False


   