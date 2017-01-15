# Logger function
# Applies concept of first-class functions and closures
# Credit to Corey Schafer on Youtube

import logging
logging.basicConfig(filename='logs/loggerfunc.log', level=logging.INFO)

def logger(func): # logger takes function as argument
	def log_func(*args): # takes any number of arguments
		logging.info('Running "{}" with arguments {}'.format(func.__name__, args))
		print(func(*args)) # will run the function with its arguments, then print result
	return log_func

def add(x, y):
	return x+y

def sub(x, y):
	return x-y

# Adds function to logger as variable, makes these two new functions equal to the inner function log_func
add_logger = logger(add) # will log add function
sub_logger = logger(sub) # will log sub function

add_logger(3, 3)
add_logger(4, 5)

sub_logger(10, 5)
sub_logger(20, 10)



