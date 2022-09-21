def lotsOfPrinting():
  print("-------------")


def fibonacci(number):
  # Program to display the Fibonacci sequence up to n-th term

  num1 = 0
  num2 = 1
  count = 1

  print('Fibonacci sequence:')
  print(num1, end=' ')
  print(num2, end=' ')
  while count < number:

    num3 = num1 + num2
    print(num3, end=' ')
    num1 = num2
    num2 = num3
    count += 1

lotsOfPrinting()

number = int(input('Enter a number to continue... : '))
fibonacci(number)
