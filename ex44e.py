class Other(object):
	def override(self):
		print "Other override"

	def implicit(self):
		print "Other implicit"

	def alter(self):
		print "Other altered"

class Child(object):
	def __init__(self):
		self.other = Other()

	def implicit(self):
		self.other.implicit()

	def override(self):
		print "Child override"

	def alter(self):
		print "Before alter"
		self.other.alter()
		print "After alter"

son = Child()

son.implicit()
son.override()
son.alter()
