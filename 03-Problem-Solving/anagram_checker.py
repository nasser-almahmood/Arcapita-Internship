alphabet = 'abcdefghijklmnopqrstuvwxyz'
print('\nEnter two words and i\'ll tell you if they are ANAGRAMS.\n')
word1 = input('First word:\n~ ').lower()
word2 = input('Second word:\n~ ').lower()

def get_index(letter):
    count = 0
    index =-1
    for item in alphabet:
        if item == letter:
            index = count
            break
        count += 1
    return index
        
def find_smallest_index(myinput):
    smallest_index = 27
    for item in myinput:
        current_index = get_index(item)
        if current_index < smallest_index:
            smallest_index = current_index
    
    return smallest_index

def mysort(myinput):
    sorted_input = ''

    while len(myinput) != 0:
        smallest_index = find_smallest_index(myinput)
        sorted_input += alphabet[smallest_index]
        myinput = myinput.replace(alphabet[smallest_index], '', 1)
        

    return sorted_input

sorted1 = mysort(word1)
sorted2 = mysort(word2)

if sorted1 == sorted2:
    print('\nYes, these words are ANAGRAMS.\n')
else:
    print('\nNo, these words are NOT anagrams.\n')