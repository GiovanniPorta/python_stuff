# First class functions
# Credit to Corey Schafer on Youtube

def square(x):
	return x * x

def my_map(func, arg_list):
	result = []
	for i in arg_list:
		result.append(func(i))
	return result
	
def logger(msg):
	def log_message():
		print('Log:', msg)
	return log_message
	
f = square

#print(square)
#print(f)
#print(f(5))

squares = my_map(square, [1, 2, 3, 4, 5])

print(squares)

log_hi = logger('Hi')

log_hi()
# these two are same
logger('Hi 2')()
