print('\nI will reverse your sentance:\n')
mysent = input('~ ')
for char in mysent:
    splittedlist = mysent.split(' ')
final = list(reversed(splittedlist))
finalresult = ' '.join(final)
print('\n'+finalresult+'\n')
    