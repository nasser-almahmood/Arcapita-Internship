print('\nWord frequency counter:\nEnter text:\n')
dict = {}
text = input('~ ')
text = text.split(' ')

for item in text:
    if item in dict:
        dict[item] = dict[item] + 1
    else:
        dict[item] = 1

print(dict)