
def draw_stars(x):
	star = ""
	for i in xrange(0,len(x)):
		for j in xrange(0,x[i]):
			star = star + "*"
		print star
		star = ""
x =[4, 6, 1, 3, 5, 7, 25]


def draw_stars2(z):
	star = ""
	for i in xrange(0,len(z)):
		if (type(z[i]) ==  int):
			for j in xrange(0,z[i]):
				star = star + "*"
		else : 
			for l in xrange(0,len(z[i])):
				star = star + z[i].split()[0][0].lower()
		print star
		star = ""
z = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
draw_stars2(z)
# draw_stars(x)

