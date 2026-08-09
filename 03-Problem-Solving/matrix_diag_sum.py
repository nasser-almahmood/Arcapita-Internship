matrix = []

print('\nMatrix size: i x i\n')
i = int(input('~ i = '))
print('')
count = 1
for item in range(i):
        print('Row', count, ':')
        row = list(input('~ ').split(' '))
        count += 1
        matrix.append(row)

add = 0
for i in range(i):
    add += int(matrix[i][i])


print('\nDaigonal Sum =', add, '\n')
    


