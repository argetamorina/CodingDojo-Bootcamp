import random
y = 0
z = 0
for x in xrange(1,5000):
	random_num = random.random()
	x_rounded = round(random_num)
	if x_rounded == 1:
		y = y + 1
		print "Attempt # %(first)d: Throwing a coin... It's a head! ... Got %(second)d head(s) so far and %(third)d tail(s) so far " % {"first" : x, "second" : y, "third" : z}
	else: 
		z = z + 1
		print "Attempt # %(first)d: Throwing a coin... It's a tail! ... Got %(second)d head(s) so far and %(third)d tail(s) so far " % {"first" : x, "second" : y, "third" : z}																														

	