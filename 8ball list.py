import random

messages = ['It is certain',
            'It is decidedly so',
            'Yes, definitely',
            'Too slow, try again',
            'Ask again later',
            'Concentrate and ask again',
            'My reply is no',
            'Outlook not so good',
            'Very doubtful']

print('DEBUG: number of messages: ' + str(len(messages)))
number = random.randint(0, len(messages) - 1)
print('You picked ' + str(number + 1) + ' for a number.')
print(messages[number] + '.')
