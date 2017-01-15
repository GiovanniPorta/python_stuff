listNums = [1, 2, 3]
print('Enter a number')
num = input()
if int(num) not in listNums:
    print('The number ' + num + ' is not in the list')
else:
    print('The number ' + num + ' exists - congrats!')
