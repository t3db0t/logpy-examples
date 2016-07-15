from logpy import *
from logpy.core import lall
import time

def lefto(q, p, list):
	# give me q such that q is left of p in list
	# zip(list, list[1:]) gives a list of 2-tuples of neighboring combinations
	# which can then be pattern-matched against the query
	return membero((q,p), zip(list, list[1:]))

def nexto(q, p, list):
	# give me q such that q is next to p in list
	# match lefto(q, p) OR lefto(p, q)
	# requirement of vector args instead of tuples doesn't seem to be documented
	return conde([lefto(q, p, list)], [lefto(p, q, list)])

people = var()

peopleRules = lall(
	# there are 4 people
	(eq,		(var(), var(), var(), var()), people),
	# Carlos wears blue
	(membero,	('Carlos', var(), 'blue'), people),
	# Loz drinks coffee
	(membero,	('Loz', 'coffee', var()), people),
	# Ted sits left of Bruce
	(lefto, 	('Ted', var(), var()),
				('Bruce', var(), var()), people),
	# A person who drinks tea sits next to Bruce
	(nexto,		(var(), 'tea', var()),
				('Bruce', var(), var()), people),
	# Carlos sits next to someone wearing red
	(nexto,		(var(), var(), 'red'),
				('Carlos', var(), var()), people),
	# Loz is last
	(eq, 		(var(), var(), var(), ('Loz', var(), var())), people),
	# A tea-drinker is first
	(eq, 		((var(), 'tea', var()), var(), var(), var()), people),
	# A coffee-drinker is last
	(eq, 		(var(), var(), var(), (var(), 'coffee', var())), people),
	# The black-shirt-wearer drinks tea
	(membero,	(var(), 'tea', 'black'), people),
	# The red-shirt-wearer is second
	(eq, 		(var(), (var(), var(), 'red'), var(), var()), people),
	# Carlos is left of the yellow-shirt-wearer
	(lefto,		('Carlos', var(), var()),
				(var(), var(), 'yellow'), people),
	# a coffee drinker wears red
	(membero,	(var(), 'coffee', 'red'), people),
	# blue drinks tea
	(membero,	(var(), 'tea', 'blue'), people)
)

t0 = time.time()
solutions = run(0, people, peopleRules)
t1 = time.time()
dur = t1-t0

count = len(solutions)
# zebraOwner = [house for house in solutions[0] if 'zebra' in house][0][0]

print "%i solutions in %.2f seconds" % (count, dur)
# print "The %s is the owner of the zebra" % zebraOwner
print "Here are all the solutions:"

for s in solutions:
	for line in s:
		print str(line)
	print "-----------"