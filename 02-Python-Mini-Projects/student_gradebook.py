mylist =[] 

run = True

# DEFS
def add_student(mylist):
        print('Add student score:\n')
        id = input('Student ID: ')
        name = input('Name: ')
        score = int(input('Score: '))
        mylist.append({"id": id, "name": name, "score": score})

def view_students(mylist):
        num = 1
        for student in mylist:
            idp = student["id"]
            namep = student["name"]
            scorep = student["score"]
            print('\n\n'+str(num)+'.', '\n ID: ', idp, '\n Name: ', namep, '\n Score: ', scorep)
            num += 1

def class_average(mylist):
    total = 0
    totalst = len(mylist)
    for student in mylist:
        total += int(student["score"])
    avg = total / totalst
    print('Average Score:', avg)

def top_student(mylist):
    max = 0
    topstudent = ""
    for student in mylist:
          if int(student["score"]) > max:
               max = int(student["score"])
               topstudent = student["name"]
               topmark = str(student["score"])
    print('\nTop Student: '+topstudent, 'with', topmark)
     


def passfail(mylist):
     for student in mylist:
        if int(student["score"]) >= 40:
               name = student["name"]
               print('Passed:', name)
        elif int(student["score"]) < 40:
               name = student["name"]
               print('Failed:', name)
          

        
        

        






# RUN
while run == True:
    print("\n\n(1) Add student score\n(2) View all students\n(3) Show class average\n(4) Show top student\n(5) Show pass/fail list\n(6) Exit\n\n ")
    menu = input('~ ')
    

    # ADD STUDENT
    if menu == '1':
        add_student(mylist)
        
        
    # VIEW ALL STUDENTS
    if menu == '2':
         view_students(mylist)
         
  
    # CLASS AVERAGE
    if menu == '3':
         class_average(mylist)

    # TOP STUDENT
    if menu == '4':
        top_student(mylist)


    # SHOW PASS/FAIL LIST
    if menu == '5':
         print('')
         passfail(mylist)
         
         


    if menu == '6':
        run = False