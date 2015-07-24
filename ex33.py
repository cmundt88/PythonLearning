low = int(raw_input("Input your low number: "))
high = int(raw_input("Input your high number: "))
change = int(raw_input("Input how much you want to increment: "))

def incrementor(bottom, ceiling, increment):
	numbers = []
	
	for bottom in range(bottom, ceiling + 1, increment):
		print "At the top, your number is %r" % bottom
		numbers.append(bottom)
		print "Number now: ", numbers
		print "At the bottom, bottom is %r" % bottom
		
	return numbers

mylist = incrementor(low, high, change)
	
print "The numbers: "

for num in mylist:

	print num