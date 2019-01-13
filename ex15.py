from sys import argv

script, filename = argv

txt = open(filename)

print "This is the file: %r" % filename
print txt.read()

print "Type in another filename:"
file_again = raw_input("> ")
txt_again = open(file_again)

print txt_again.read()
