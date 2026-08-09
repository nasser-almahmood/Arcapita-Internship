valid = True
while valid == True:
    num = int(input('Enter Number between 0 and 50: ~ '))
    if 0 <= num <= 50:
        valid = False
    else:
        continue
    
if num % 3 == 0 and num % 5 != 0:
    print('Fizz')
elif num % 5 == 0 and num % 3 != 0:
    print('Buzz')
elif num % 3 == 0 and num % 5 == 0:
    print('FizzBuzz')
else:
    print('Neither')