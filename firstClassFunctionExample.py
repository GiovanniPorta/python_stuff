# First-class functions
# Credit to Corey Schafer on Youtube

def html_tag(tag): # outer func
	def wrap_text(msg): # inner func
		print('<{0}>{1}</{0}>'.format(tag, msg)) # executed when inner func is called
	return wrap_text #outer func returns inner func with tag variable set, still requires msg as argument
	
print_h1 = html_tag('h1') # outer func tag variable set, print_h1 is equal to wrap_text

print(print_h1.__name__) # prints wrap_text

print_h1('Test Headline!') # prints the msg ('Test Headline!') argument surrounded by the tag ('h1') argument, which was set earlier

# What to take from this: the inner function will remember variables set by the outer function, even when executed outside of its scope

