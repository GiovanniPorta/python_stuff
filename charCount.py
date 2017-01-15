import pprint

message = 'It was a bright cold day in April.'

message2 = ['It', 'was', 'a', 'bright', 'cold', 'day', 'in', 'April.']

count = {}

#for item in message2:
#    print(item)

print(message)
print('I am now going to analyse the characters in the message:')

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

#pprint.pprint(count)

for k, v in count.items():
    print('The character ' + k + ' appears ' + str(v) + ' times.')
    
