#all three combined
class Parent(object):
	def implicit(self):
		print "Parent implicit"

	def override(self):
		print "Parent override"

	def altered(self):
		print "Parent altered"

class Child(Parent):
	def override(self):
		print "Child override"

	def altered(self):
		print "Child before parent altered"
		super(Child, self).altered()
		print "Child after parent altered"

dad = Parent()
son = Child()

print "Implicit:"
dad.implicit()
son.implicit()

print "\nOverride:"
dad.override()
son.override()

print "\nAlter:"
dad.altered()
son.altered()
