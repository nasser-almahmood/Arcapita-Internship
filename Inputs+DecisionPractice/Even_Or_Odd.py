run = True
print("\nPick a number and i'll tell you wether it's EVEN or ODD")
while run == True:
    
    num = input('')
    if num.isdigit():
        run = False
    else:
        run = True
if int(num) % 2 != 0:
    print('-ODD NUMBER')
else:
    print('-EVEN NUMBER')