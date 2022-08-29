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



#Program to display the Fibonacci sequence up to n-th term
number = int(input('Enter a number to continue... : '))
num1 = 0
num2 = 1
count = 1

print('Fibonacci sequence:')
print(num1, end=' ')
while count < number:

    num3 = num1 + num2
    print(num3, end=' ')
    num1 = num2
    num2 = num3
    count += 1

