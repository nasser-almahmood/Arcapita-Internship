mylist = []
budgets = {"food":0.0,"rent":0.0,"transport":0.0,"other":0.0}
allowed = {"salary","food","rent","transport","other"}
budgetsum = budgets['food'] + budgets['rent'] + budgets['transport'] + budgets['other']
def add_transaction(mylist):
# Date
    day = ''
    month = ''
    year = ''
    valid = True
    while valid == True:
        try:
            print('\nEnter Date: (day/month/year)')
            date = input('~ ').split('/')
        
            day = str(date[0])
            month = str(date[1])
            year = str(date[2])
            if int(day) <= 30 and int(month) <= 12 and len(str(year)) == 4:
                
                valid = False
            else:
                print('\n- Invalid -')
                valid = True
        except:
            print('\n- Invalid -')
            valid = True
        date = day+'/'+month+'/'+year
# Type
    valid = True
    while valid == True:
        print('\nEnter Type: (I = Income, E = Expense)')
        type = input('~ ').lower()
        try:
            if type == 'i':
                type = 'income'
                valid = False
            elif type == 'e':
                type = 'expense'
                valid = False
            else:
                print('\n- Invalid -')
                valid = True
        except:
            print('\n- Invalid -')
            valid = True
# Category
    valid = True
    while valid == True:
        try:
            if type == 'expense':
                print('\n Enter (EXPENSE) Category: (Food/Rent/Transport/Other)')
                category = input('~ ').lower()
                if  category == 'food' or category == 'rent' or category == 'transport' or category == 'other':
                    valid = False
                else:
                    print('\n- Invalid Category-')
                    valid = True
            elif type == 'income':
                category = 'salary'
                valid = False
        except:
            print('\n- Invalid Category-')
            valid = True
# Amount
    valid = True
    num = 0
    amount = 0
    while valid == True:
        try:
            
            if category == 'food'or category == 'rent' or category == 'transport' or category == 'other':
                print('\nEnter Amount:')
                amount = float(input('~ '))
                if budgetsum >= 0 and amount <= budgetsum:
                    num = float(budgets[category]) - float(amount)
                    budgets[category] = num
                    print('Budget for', category+':', num)
                    print('\nEnter note:')
                    note = input('~ ')
                    valid = False
                    break
                else:
                    print('\n- Insufficient funds -')
                    valid = True
            elif category == 'salary':
                print('\nEnter Income:')
                amount = float(input('~ '))
                budgets['food'] = amount * 0.2
                budgets['rent'] = amount * 0.5
                budgets['transport'] = amount * 0.2
                budgets['other'] = amount * 0.1

                if amount > 0:
                    print('\nEnter Note:')
                    note = input('~ ')
                    valid = False
                else:
                    print('\n- Invalid -')
                    valid = True
            else:
                print('\n- Invalid -')
                valid == True
        except:
            print('\n- Invalid -')
            valid = True
    
# ADD
    mylist.append({"date": date, "type": type, "category": category, "amount": amount, "note": note})

def view_transactions(mylist):
    count = 1
    print('\n---------------------------------------------------------------------')
    print('Num | Date        | Type     | Category   | Amount   | Note\n----|-------------|----------|------------|----------|---------------')
    space0 = 0
    space = 0
    space1 = 0
    space2 = 0
    
    for transaction in mylist:
        space0 = 10 - len(str(transaction["date"]))
        spaces0 = ' ' * space0
        space = 9 - len(transaction["category"])
        spaces = ' ' * space
        space1 = 8 - len(transaction["type"])
        spaces1 = ' ' * space1
        space2 = 7 - len(str(transaction["amount"]))
        spaces2 = ' ' * space2
        print('['+str(count)+']'+' |', transaction["date"], spaces0, '|', transaction["type"], spaces1+ '|', transaction["category"], spaces, '|', transaction["amount"], spaces2, '|', transaction["note"])
        count += 1
    print('---------------------------------------------------------------------\n')

def max_(mylist, category):
    maximum = 0
    for transaction in mylist:
          if category == transaction["category"]:
            if int(transaction["amount"]) > maximum:
                maximum = int(transaction["amount"])
                max = str(transaction["amount"])
    return max
def min_(mylist, category):
    minimum = 9999999999999999999
    for transaction in mylist:
          if category == transaction["category"]:
            if int(transaction["amount"]) < minimum:
                minimum = int(transaction["amount"])
                min = str(transaction["amount"])
    return min
def category_transactions(mylist):
    print('\nEnter Category: (Food/Rent/Transport/Other|Salary)\n')
    category = input('~ ').lower()
    total = 0
    count = 0
    average = 0 
    if category == 'food'or category == 'rent' or category == 'transport' or category == 'other' or category == 'salary':
        for transaction in mylist:
            if category == transaction["category"]:
                total += transaction["amount"]
                count += 1
        max = max_(mylist, category)
        min = min_(mylist, category)
        average = total / count
           

        print('\n-----------------------------')
        print('Category:', category)

        print('Total:   ', total)

        print('Average: ', average)

        print('Min:     ', min)

        print('Max:     ', max)

        print('Count:   ', count)
        print('-----------------------------\n')

def summary_(mylist):
    expenses = 0
    income = 0
    for transaction in mylist:
        if transaction["category"] == 'food'or transaction["category"] == 'rent' or transaction["category"] == 'transport' or transaction["category"] == 'other':
            expenses += transaction["amount"]

        else:
            income += transaction["amount"] 
    net = income - expenses



    print('\n-----------------------------')
    print('Income:   ', income)
    print('Expenses: ', expenses)
    print('Net:      ', net)
    print('-----------------------------\n')
    
def budget_check(mylist):
    food = 0
    rent = 0
    transport = 0
    other = 0

    space0 = 0
    space = 0
    space1 = 0
    space2 = 0
    spacea = 0
    spaceb = 0
    spacec = 0
    spaced = 0

    foods = ''
    rents = ''
    transports = ''
    others = ''
        
    for transaction in mylist:
        if transaction["category"] == 'food':
            food += transaction["amount"]
        elif transaction["category"] == 'rent':
            rent += transaction["amount"]
        elif transaction["category"] == 'transport':
            transport += transaction["amount"]
        elif transaction["category"] == 'other':
            other += transaction["amount"]
        #budget
        spacea = 7 - len(str(budgets["food"]))
        spacesa = ' ' * spacea
        spaceb = 7 - len(str(budgets["rent"]))
        spacesb = ' ' * spaceb
        spacec = 7 - len(str(budgets["transport"]))
        spacesc = ' ' * spacec
        spaced = 7 - len(str(budgets["other"]))
        spacesd = ' ' * spaced
        #spent
        space0 = 8 - len(str(food))
        spaces0 = ' ' * space0
        space = 8 - len(str(rent))
        spaces = ' ' * space
        space1 = 8 - len(str(transport))
        spaces1 = ' ' * space1
        space2 = 8 - len(str(other))
        spaces2 = ' ' * space2
        
    if food < budgets["food"]:
        foods = 'Under Budget :) '
    elif food == budgets["food"]:
        foods = 'On Budget'
    else:
        foods = 'Over Budget :( '

    if rent < budgets["rent"]:
        rents = 'Under Budget :) '
    elif rent == budgets["rent"]:
        rents = 'On Budget'
    else:
        rents = 'Over Budget :( '

    if transport < budgets["transport"]:
        transports = 'Under Budget :) '
    elif transport == budgets["transport"]:
        transports = 'On Budget'
    else:
        transports = 'Over Budget :( '

    if other < budgets["other"]:
        others = 'Under Budget :) '
    elif other == budgets["other"]:
        others = 'On Budget'
    else:
        others = 'Over Budget :( '
    
    print('\n---------------------------------------------------\nCategory   | Budget   | Spent    | Status\n-----------|----------|----------|-----------------')
    print('Food       |',budgets["food"],spacesa, '|', food, spaces0+'|', foods)
    print('Rent       |',budgets["rent"],spacesb, '|', rent, spaces+'|', rents)
    print('Transport  |',budgets["transport"],spacesc, '|', transport, spaces1+'|', transports)
    print('Other      |',budgets["other"],spacesd, '|',  other, spaces2+'|', others)
    print('---------------------------------------------------\n')

def edit_del(mylist):
    
    count = 1
    
    print('\n---------------------------------------------------------------------')
    print('Num | Date        | Type     | Category   | Amount   | Note\n----|-------------|----------|------------|----------|---------------')
    space0 = 0
    space = 0
    space1 = 0
    space2 = 0
    
    for transaction in mylist:
        space0 = 10 - len(str(transaction["date"]))
        spaces0 = ' ' * space0
        space = 9 - len(transaction["category"])
        spaces = ' ' * space
        space1 = 8 - len(transaction["type"])
        spaces1 = ' ' * space1
        space2 = 7 - len(str(transaction["amount"]))
        spaces2 = ' ' * space2
        print('['+str(count)+']'+' |', transaction["date"], spaces0, '|', transaction["type"], spaces1+ '|', transaction["category"], spaces, '|', transaction["amount"], spaces2, '|', transaction["note"])
        count += 1
    print('---------------------------------------------------------------------\n')
    if mylist == []:
        print('- No Data Available -')
    else:
        valid = True
        while valid == True:
            try:
                
                index = 1
                print('Enter transaction number to Edit/Delete:\n')
                num = int(input('~ '))
                
            except:
                valid = True
            for transaction in mylist:
                if num == index:
                
                    print('\nNum | Date        | Type     | Category   | Amount   | Note\n----|-------------|----------|------------|----------|---------------')
                    print('['+str(index)+']'+' |', transaction["date"], spaces0, '|', transaction["type"], spaces1+ '|', transaction["category"], spaces, '|', transaction["amount"], spaces2, '|', transaction["note"])
                    print('---------------------------------------------------------------------\n')
                    if num <= (index - 1):
                        valid = False
                    else:
                        valid = True
                index += 1
        valid = True
        while valid == True:  
            try:
                print('[1] Edit | [2] Delete')
                edelete = int(input('~ '))
                ind = num - 1
                if edelete == 1:
                    add_transaction(mylist)
                    mylist.pop(ind)
                    print('/n- Edit Successful -')
                    valid = False

                elif edelete == 2:
                    if mylist[ind]["type"] == 'expense':
                        amount = mylist[ind]["amount"]
                        budgets['food'] = amount * 0.2
                        budgets['rent'] = amount * 0.5
                        budgets['transport'] = amount * 0.2
                        budgets['other'] = amount * 0.1
                        mylist.pop(ind)
                    elif mylist[ind]["type"] == 'expense':
                        amount = mylist[ind]["amount"]
                        budgets['food'] = - amount * 0.2
                        budgets['rent'] = - amount * 0.5
                        budgets['transport'] = -amount * 0.2
                        budgets['other'] = - amount * 0.1
                        mylist.pop(ind)
                    print('\n- Delete Successful -\n')
                    valid = False
                else:
                    valid = True    
            except:
                valid = True    
     
run = True
while run == True: 
    print('\n(1) Add Transaction')
    print('(2) View transactions')
    print('(3) Category summary')
    print('(4) Overall summary')
    print('(5) Budget check')
    print('(6) Edit/Delete transaction')
    print('(7) Export/Inport - Not Ready Yet :( -')
    print('(8) Exit\n')

    menu = input('~ ')

    if menu == '1':
        day = ''
        month = ''

        add_transaction(mylist)
        

    if menu == '2':
        view_transactions(mylist)
        if mylist == []:
            print('\n- No Data Available -\n')

    if menu == '3':
        category_transactions(mylist)

    if menu == '4':
        summary_(mylist)


    if menu == '5':
        budget_check(mylist)

    if menu == '6':
        edit_del(mylist)

    # if menu == '7':

    if menu == '8':
        run = False