print('\n-------------')
number = int(input('Enter a number to continue... : '))

sum = 0
for sum in range(number):
    sum += 1
    print(sum, end=' ')

print('\n-------------')
number = int(input('Enter a number to continue... : '))
sum = 0

for sum in range(number):
    sum = sum + sum
    print(sum, end=' ')
print('\n-------------')
number = int(input('Enter a number to continue... : '))
sum = -1
num = 0

while num < number:
    sum = (sum+2)
    num = num + 1
    print(sum, end=' ')