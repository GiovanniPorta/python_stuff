while True:
    print('Who are you?')
    name = input()
    if name != 'Giovanni':
        continue
    print("Hello, Giovanni. What is the password?")
    password = input()
    if password == 'misty':
        print('Access granted.')
        break
