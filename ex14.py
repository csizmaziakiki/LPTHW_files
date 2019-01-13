from sys import argv

script, user_name = argv
prompt = '>'

print "Hi %s! I'm the %s script!" % (user_name, script)

print "Do you like coffee?"
coffee = raw_input(prompt)

print "Do you like music?"
music = raw_input(prompt)

print "You said that it's %r that you like coffee, and %r that you like music" % (coffee, music)

