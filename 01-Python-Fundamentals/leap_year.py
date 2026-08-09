print('\nGive me a year and ill tell you if its a LEAP YEAR')
year = int(input('-'))
if (year % 4 == 0 and year < 1000) or (year % 400 == 0 and year >= 1000):
    print('Yup its a LEAP YEAR')
elif (year % 4 != 0 and year < 1000) or (year % 400 != 0 and year >= 1000):
    print('Nope its Not a LEAP YEAR')
    