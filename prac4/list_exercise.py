times = int(input('How many times:'))
numbers = []
for a in range (times):
    numbers.append(a)
    number = input('number:')


print(f'The first number is {numbers[0]}')
print(f'The last number is {numbers[times-1]}')
print(f'The smallest number is {min(numbers)}')
print(f'The largest number is {max(numbers)}')
print(f'The average of the numbers is {sum(numbers)/ times}')




