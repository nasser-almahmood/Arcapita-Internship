
print('\nEnter a word and i\'ll tell you if ts\'s a PALINDROME.\n')
word1 = input('Enter word:\n~ ').lower()
w1 = ''
count = 1
index = -99
for item in word1:
    index = len(word1) - count
    count += 1
    w1 += (word1[index])

if word1 == w1:
    print('Yes it is a PALINDROME :)')
else:
    print('No it is NOT a PALINDROME :(')