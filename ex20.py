from sys import argv

script, input_file = argv

def print_all(f):
    print f.read()

def rewind(f):
    f.seek(0)

def print_line(line_count, f):
#no option to print the third line first, can only move line by line
    print line_count, f.readline()

current_file = open(input_file)

print "The whole file:"
print_all(current_file)

#print "Rewinding to the beginning of the file:\n"
rewind(current_file)

print "Printing line one:"
print_line(1, current_file)
