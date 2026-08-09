print('\nWould you like to ADD(+), SUBTRACT(-), MULTIPLY(*), DIVIDE(/)\n')
add = False
subtract = False
multiply = False
divide = False

run = True
while run == True:
    operation = input('').lower()
    if operation == 'add':
        run = False
        add = True
    if operation == 'subtract':
        run = False
        subtract = True
    if operation == 'multiply':
        run = False
        multiply = True
    if operation == 'divide':
        run = False
        divide = True
        
if add == True:
    print('Now choose two numbers')
    fn = input('First Number:')
    sn = input('Second Number:')

    answer = fn + sn
    print('=', answer)

if subtract == True:
    print('Now choose two numbers')
    fn = input('First Number:')
    sn = input('Second Number:')

    answer = fn - sn
    print('=', answer)

if multiply == True:
    print('Now choose two numbers')
    fn = input('First Number:')
    sn = input('Second Number:')

    answer = fn * sn
    print('=', answer)


rund = True
while rund == True:
    if divide == True:
        print('Now choose two numbers')
        fn = input('First Number:')
        sn = input('Second Number:')
        if int(sn) == 0:

            
            
            print("Can't DIVIDE by 0 mate")
            rund = True
        else: 
            rund = False
            answer = int(fn) / int(sn)
            print('=', answer)


