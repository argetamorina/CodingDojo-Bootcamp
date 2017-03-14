# a = [1, 2, 5, 10, 255, 3]
# print sum(a)/len(a)
number = 1
def function():
	for number in range(1,2000):
		if number % 2 == 0:
			print "Number is  %(first)d. This is an even number." % {"first": number}
		else: 
			print "Number is %(second)d. This is an odd number." % {"second":number}
			number + 1
function()
