def print_two(*args): # *args means all args
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)

def print_two_two(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)

def print_one(arg1):
    print "arg1: %r" % arg1

def print_none():
   print "No parameter(s)"


print_two("Egy", "Ketto")
print_two_two("Egy", "Ketto")
print_one("Egy")
print_none()
