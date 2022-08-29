number = int(input('Enter a number to continue... : '))
sum = 0
for sum in range(number):
    sum += 1
    print(sum, end=' ')

print('-------------')
number = int(input('Enter a number to continue... : '))
sum = 0

for sum in range(number):
    sum = sum + sum
    print(sum, end=' ')