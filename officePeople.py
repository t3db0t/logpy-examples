from logpy import *

wears = Relation()
drinks = Relation()
nextTo = Relation()

people = ('Ted', 'Bruce', 'Carlos', 'Loz')

facts(wears,	('Ted',		'Black'),
				('Bruce',	'Red'),
				('Carlos',	'Blue'),
				('Loz',		'Yellow'))

facts(drinks,	('Ted',		'Tea'),
				('Bruce',	'Coffee'),
				('Carlos',	'Tea'),
				('Loz',		'Coffee'))

def makeNextToFacts():
	for i, p in enumerate(people):
		if(i < len(people)-1):
			print "Making fact %s %s" % (p, people[i+1])
			fact(nextTo, p, people[i+1])
		if(i != 0):
			print "Making fact %s %s" % (p, people[i-1])
			fact(nextTo, p, people[i-1])

makeNextToFacts()

q = var()

print "What does Ted drink?"
print run(0, q, drinks('Ted',q))

print "Who drinks coffee?"
print run(0, q, drinks(q, 'Coffee'))

print "Who drinks coffee and wears red?"
print run(0, q, drinks(q, 'Coffee'), wears(q, 'Red'))

print "What do red-wearers drink?"
a = var()
print run(0, q, wears(a, 'Red'), drinks(a, q))

print "What does Bruce wear and drink?"
q2 = var()
print run(0, (q, q2), wears('Bruce', q), drinks('Bruce', q2))

print "Who sits next to Bruce?"
print run(0, (q, q2), eq(people, (q, 'Bruce', q2, a)))

print "Who sits next to someone wearing red?"
print run(0, q, wears(a, 'Red'), nextTo(q,a))

b = var()
print "What do people wear who sit next to coffee drinkers?"
print run(0, q, wears(a, q), nextTo(a, b), drinks(b, 'Coffee'))