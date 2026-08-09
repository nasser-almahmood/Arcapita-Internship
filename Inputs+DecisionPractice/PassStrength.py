print("Password:")
grade = input("")
gradelen = len(grade)
if gradelen < 6:
    print('Weak Password')
elif 6 <= gradelen and gradelen <= 10:
    print('Medium Password')
elif gradelen > 10:
    print('Strong Password')
