# Class decorators
# Continuation from displayInfo_decorators.py

def decorator_function(original_function):
	def wrapper_function(*args, **kwargs): # *args, **kwargs required so that arguments passed thru original func work in wrapper
		print('Wrapper function executed this before {0}'.format(original_function.__name__))
		return original_function(*args, **kwargs) # see above
	return wrapper_function

class decorator_class(object):
	def __init__(self, original_function):
		self.original_function = original_function
	def __call__(self, *args, **kwargs):
		print('Call method executed this before {0}'.format(self.original_function.__name__))
		return self.original_function(*args, **kwargs)

@decorator_class # same result as decorator_function
def display():
	print('Display function executed')
	
@decorator_class
def display_info(name, age):
	print('display_info ran with arguments ({}, {})'.format(name, age))

display_info('John', 25)
