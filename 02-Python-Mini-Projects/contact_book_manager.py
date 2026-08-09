mylist = []

#DEFS
def add_contact(mylist):
    valid = True
    print('\nAdd contact details\n')
    name = input('Name: ')
    while valid == True:
            phone = input('Phone: ')
            if phone.isnumeric() and 8 <= len(phone) <= 10:
                valid = False
            else:
                print('! Invalid !')
                valid = True
    valid = True
    while valid == True:
        email = input('Email: ')
        if email.endswith("@gmail.com"):
            valid = False
        else: 
            print('! Invalid !')
            valid = True
    mylist.append({"name": name, "number": phone, "email": email})

def view_contact(mylist):
    count = 1
    for contact in mylist:
        print('\n'+str(count)+'.', '\n Name:', contact["name"], '\n Contact:', contact["number"], '\n Email:', contact["email"], '\n' )
        count = int(count)
        count += 1

def search_contact(mylist):
    valid = True
    while valid == True:
        count = 0 
        print('\nEnter Name:')
        names = input('~ ')
        for contact in mylist:
            if names == contact["name"]:
                print('\n Name:', contact["name"], '\n Contact:', contact["number"], '\n Email:', contact["email"], '\n' )
                count += 1
        if count == 0:
                print('\nNo match found :(\n')
            
def update_contact(mylist):
    index = -1
    count = 0
    print('\nEnter contact number to update:')
    num = input("~ ")
    for contact in mylist:
        if num == contact["number"]:
            print('\n(Leave empty if you dont want to change)')
            print(' Name:', contact["name"], '\n Contact:', contact["number"], '\n Email:', contact["email"], '\n' )
            index = count
            
            break
        count += 1
             

    if index != -1:
        valid = True
        changename = ''
        changenum = ''
        changeemail = ''

        while valid == True:
            if changename == '':
                changename = input('New Name:\n~ ')
                mylist[index]["name"] = changename
            

            if changenum == '' or not changenum.isnumeric() or not 8 <= len(changenum) <= 10:
                changenum = input('New Phone Number:\n~ ')
                mylist[index]["number"] = changenum
                continue 
           

            if changeemail == '' or not changeemail.endswith("@gmail.com"):
                changeemail = input('New Email:\n~ ')
                mylist[index]["email"] = changeemail
                continue
            
    else:
        print("\n- No match found -\n")
    
def delete_contact(mylist):
    index = -1
    count = 0
    print('\nEnter contact number to delete:')
    num = input("~ ")
    for contact in mylist:
        if num == contact["number"]:
            print('\n Name:', contact["name"], '\n Contact:', contact["number"], '\n Email:', contact["email"], '\n' )
            index = count
            
            break
        count += 1
             

    if index != -1:
        mylist.pop(index)
        print('\n- Delete Successful -\n')
    
    else:
        print("\n- No match found -\n")

#RUN MENU
run = True
while run == True:
    print('\n(1) Add contact\n(2) View all contacts\n(3) Search contact by name\n(4) Update contact\n(5) Delete contact\n(6) Exit\n ')
    menu = input('~ ')

    if menu == '1':
        add_contact(mylist)
        
    if menu == '2':
        view_contact(mylist)

    if menu == '3':
        search_contact(mylist)

    if menu == '4':
        update_contact(mylist)

    if menu == '5':
        delete_contact(mylist)

    if menu == '6':
        run = False

