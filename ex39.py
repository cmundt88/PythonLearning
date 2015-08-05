import hashmap

# create a mapping of state to abbreviation
states = hashmap.new()
hashmap.set(states,	'Oregon', 'OR')
hashmap.set(states,	'Florida', 'FL')
hashmap.set(states,	'California', 'CA')
hashmap.set(states,	'New York', 'NY')
hashmap.set(states,	'Michigan', 'MI')

# create a basic set of states and some cities in them
cities = hashmap.new()
hashmap.set(cities, 'CA', 'San Fancisico')
hashmap.set(cities, 'MI', 'Detroit')
hashmap.set(cities, 'FL', 'Jacksonville')

# add some more cities
hashmap.set(cities, 'NY', 'New York')
hashmap.set(cities, 'OR', 'Portland')

# print out some cities
print '_' * 10
print "NY State has: ", hashmap.get(cities, 'NY')
assert hashmap.get(cities, 'NY') == 'New York'
print "OR State has: ", hashmap.get(cities, 'OR')
assert hashmap.get(cities, 'OR') == 'Portland'

#print some states
print '_' * 10
print "Michigan's abbreviation is: ", hashmap.get(states, 'Michigan')
print "Florida's abbreviation is: ", hashmap.get(states,'Florida')

# do it by using the state then cities dict
print '_' * 10
print "Michigan has: ", hashmap.get(cities, hashmap.get(states, 'Michigan'))
print "Florida has: ", hashmap.get(cities, hashmap.get(states, 'Florida'))

# print every state abbreviation
print '_' * 10
hashmap.list(states)
	
# print every city in state
print '_' * 10
hashmap.list(cities)
	
# now do both at the same time
#print '_' * 10
#for state, abbrev in states.items():
#	print "%s state is abbreviated %s and has city %s" % (
#		state, abbrev, cities[abbrev])
		
print '_' * 10
state = hashmap.get(states, 'Texas')

if not state:
	print "Sorry, no Texas."

# default values using ||= with the nil result
# can you do this with one line?	
city = hashmap.get(cities, 'TX', 'Does Not Exist')
print "The city for the state 'TX' is: %s" % city