print('Price of Movie Tickets:')
age = int(input("Your AGE:\n"))
day = input('Is today WEEKDAY or WEEKEND: \n').lower()
if age < 12:
    print('$5')
elif age >= 12 and age <= 64 and day == 'weekday':
    print('$10')
elif age >= 12 and age <= 64 and day == 'weekend':
    print('$12')
elif age >= 65:
    print('$6')
