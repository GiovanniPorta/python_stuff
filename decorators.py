# Decorators
# Function that takes another function as an argument, adds functionality, then returns another function
# All of this without altering the source code of the original function passed in

#def outer_function(msg):
#	def inner_function(name):
#		print(msg, name)
#	return inner_function

#hi_func = outer_function('Hi')
#bye_func = outer_function('Bye')

#hi_func('Gio')
#bye_func('Gio')

def decorator_function(original_function):
	def wrapper_function():
		print('Wrapper function executed this before {0}'.format(original_function.__name__))
		return original_function()
	return wrapper_function

@decorator_function
def display(): # NOTE: if original function takes arguments, wrapper func needs args as well. see displayInfo_decorators.py
	print('Display function executed')

#decorated_display = decorator_function(display)
#
#print(decorated_display.__name__) # wrapper_function
#decorated_display() # runs wrapper function, then original function

display() 
# since display function is wrapped (@) under decorator_function, this has the same effect as previous code
# basically decorating the display function does: display = decorator_function(display)

