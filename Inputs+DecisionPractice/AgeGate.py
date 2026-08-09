run = True
print("\nEnter your AGE")
while run == True:
    
    age = input('')
    if age.isdigit() and int(age) >= 0:
        run = False
    else:
        run = True
if int(age) < 13:
    print('Child')
elif 13 <= int(age) <= 19:
    print('Teenager')
else:
    print('Adult')