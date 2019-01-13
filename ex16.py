from sys import argv

scrip, filename = argv

print "We are going to erase the contents of", filename

print "Opening the file..."
target = open(filename, 'w')

print "Deleting the file..."
target.truncate()

print "Type two lines to write into the file"
line1 = raw_input("line 1:")
line2 = raw_input("line 2:")

target.write(str(line1))
target.write("\n")
target.write(str(line2))
target.write("\n")

print "Closing the file..."
target.close()
