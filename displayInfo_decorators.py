# Decorators

def decorator_function(original_function):
	def wrapper_function(*args, **kwargs): # *args, **kwargs required so that arguments passed thru original func work in wrapper
		print('Wrapper function executed this before {0}'.format(original_function.__name__))
		return original_function(*args, **kwargs) # see above
	return wrapper_function

@decorator_function
def display():
	print('Display function executed')
	
@decorator_function
def display_info(name, age):
	print('display_info ran with arguments ({}, {})'.format(name, age))

display_info('John', 25)
display()
