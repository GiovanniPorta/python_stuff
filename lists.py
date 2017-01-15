listItems = []
while True:
    print('Enter the name of item ' + str(len(listItems) + 1) + ' (or enter nothing to stop):')
    item = input()
    if item == '':
        break
    listItems = listItems + [item]  # list concatenation
print('The items are:')
#numItems = 1
#for x in listItems:
#    print(str(numItems) + ': ' + x)
#    numItems = numItems + 1

for i in range(len(listItems)):
    print('Index ' + str(i) + ' in the item list is: ' + listItems[i])
    
