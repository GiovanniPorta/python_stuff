import sys

while True:
    print('Use "end" to exit')
    command = input()
    if command == 'end':
        sys.exit()
    print('Unknown: ' + command)
    
