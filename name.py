print("What is your name?")
name = input()
space = " "
print("Hello" + space + name + "!")

print("What is your age?")
age = input()
age = int(age)

if age < 19:
    print("You are a kid")
elif age > 50:
    print("You are a senior")
elif age >= 19:
    print("You are an adult")
