print("Give me your grade.")
grade = int(input(""))
if 0 <= grade < 60:
    print('F...Bad student')
elif 60 <= grade and grade < 70:
    print('D')
elif 70 <= grade < 80:
    print('C')
elif 80 <= grade < 90:
    print('B')
elif 90 <= grade <= 100:
    print('A')
else:
    print('Invalid')