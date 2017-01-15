# Closures
# A closure is an inner function that remembers and has access to variables in the local scope
# in which is was created, even after the outer function has finished executing.

# Use case?
# Adding functionality to a function without altering the code of the functions themselves
# For example, the logger function example (see loggerFunc_closures.py) adds logging capabilities to
# the add and subtract functions, all without adding any logging code to those functions themselves.
# This allows us to keep all of the logic separated into their own specific functions
# Read more: 'Aspect Oriented Programming'

# Credit to Corey Schafer on Youtube


#def outer_func():
def outer_func(msg):
#	message = 'Hi'
	message = msg	
		
	def inner_func():
		print(message)
	
	return inner_func
	
#my_func = outer_func()
#print(my_func.__name__) # prints inner_func
#my_func() # equal to inner_func

hi_func = outer_func('Hi')
hello_func = outer_func('Hello')

hi_func()
hello_func()
