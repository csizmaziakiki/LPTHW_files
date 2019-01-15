def add(a, b):
	print "Adding %d + %d" % (a, b)
	return a + b

def moreadd(a, b, c):
	return a +b, a+c, b+c

age = add(20, 5)
print "Age: %d" % age

a, b, c = moreadd(10, 20, 30)
print "a=%d, b=%d, c=%d" % (a, b, c)
