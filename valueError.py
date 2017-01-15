print('Type in an integer')

try:
    number = int(input())
    print(number)
except ValueError:
    print('That is not a number')
