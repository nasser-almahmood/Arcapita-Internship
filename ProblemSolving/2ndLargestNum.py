print('\nEnter a list of numbers and ill tell you the 2nd largest:\n')
nums = (input('~ '))
nums = nums.split(',')
max1 = max(nums)

while max1 in nums:
    nums.remove(max1)

max2 = max(nums)

print('The second largest number is:', max2)

