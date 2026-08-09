
numbers = '1234567890'

def mylen(mynum):
    len = 0
    for char in mynum:
        len += 1
    return len

def isnum(numbers):
    numcount = 0
    for char in mynum:
        if char in numbers:
            numcount += 1
    return numcount

def unique_digits(mynum):
    check = ''
    for char in mynum:
        if char not in check:
            check = check + char

    if check != mynum:
        print('\nNo it is NOT unique :(\n')
    else:
        print('\nYes it IS unique :)\n')

print('\nWe\'ll check if your number is unique.\nEnter your number:\n')
valid = True
while valid == True:
    mynum = input('~ ')
    if isnum(numbers) != mylen(mynum):
        print('\n- Only numbers please -\n')
    else:
        valid = False
unique_digits(mynum)

