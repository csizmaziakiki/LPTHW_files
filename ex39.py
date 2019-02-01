stuff = {'name': 'Kiki', 'age': 25}
print stuff['name']
print stuff['age']

for key, value in stuff.items():
	print "%s: %s" % (key, value)

del stuff['name']
#safely get key that maybe not exists, from value (none is default)
skey = stuff.get('City', None)

if not skey:
	print "Sorry, no City" 
