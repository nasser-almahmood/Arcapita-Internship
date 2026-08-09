print("\nGive three numbers and i'll tell you the max of them.")
run1 = True
run2 = True
run3 = True
while run1 == True:
    fn = input('First number: ')
    if fn.isdigit():
        run1 = False

while run2 == True:
    sn = input('Second number: ')
    if sn.isdigit():
            run2 = False
    
while run3 == True:
    tn = input('Third number: ')
    if tn.isdigit():
         run3 = False

if fn > sn:
     if fn > tn:
          print(fn)
elif sn > tn:
     print(sn)
else:
     print(tn)
