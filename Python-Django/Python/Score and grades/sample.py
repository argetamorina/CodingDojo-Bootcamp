import random
print "Score and grades"
# score = 100
# print 2 * random.random(),
# 4251231
for x in xrange(1,11):
	score = input()
	if score < 60:
		print "You fail"
	if score >= 60 and score <= 69:
		print "Score is %(first)d. Your grade is D" % {"first": score}
	if score >= 70 and score <= 79:
		print "Score is %(first)d. Your grade is C"  % {"first": score}
	if score >= 80 and score <= 89:
		print "Score is %(first)d. Your grade is B"  % {"first": score}
	if score >= 90 and score <= 100:
		print "Score is %(first)d. Your grade is A"  % {"first": score}
	if score > 100 or score < 0:
		print "Error"
