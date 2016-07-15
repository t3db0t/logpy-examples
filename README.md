# logpy-examples
A couple of nifty logic programming examples for logpy including the infamous Zebra Problem

# To Run
```
pip install logic
python officePeople.py
```

# Notes

## officePeople.py

Some basic examples of querying the `logpy` 'facts' relational knowledge base

## logpyZebra.py

An implementation of the ['Zebra' logic puzzle](http://en.wikipedia.org/wiki/Zebra_puzzle), adapted from/inspired by David Nolen's core.logic implementation here: https://rosettacode.org/wiki/Zebra_puzzle#Clojure

The Zebra Puzzle provides 16 clues describing relationships between five houses and their properties, such as "In the middle house they drink milk" and "They drink water in a house next to the house where they smoke Blend", and finally asks, "Who owns the Zebra?"

The solution to the puzzle is essentially a table of data, where each row represents one of 5 houses:

| Nationality  | Smokes | Drinks | Pet | Color |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| Englishman  | ... | ... | ... | ... |
| Swede  | ... | ... | ... | ...  |

If you had all the data ahead of time, then you could just put it all in a database and query it with SQL.  However, the clues don't give you this information: they provide relations between several properties, including positions ('The Norwegian lives next to the blue house').  Logic programming enables you to encode these clues elegantly, then stipulate them declaratively to the solver, and the computer does the work for you.  Then you just print out the solution.

### Details

`(eq, 		(var(), var(), var(), var(), var()), houses)`

Sets up `houses` as a list of logic variables (each house), each of which will itself contain a list of logic variables (each property of that house)

`(membero,	('Englishman', var(), var(), var(), 'red'), houses)`

Stipulates that *one of the houses* has both the 'Englishman' and 'red' properties. The other properties are left 'blank' as logic variables, which get 'filled in' by the solver.

## officePeoplePuzzle.py

A pretty trivial 'puzzle' version of `officePeople.py`, with a FAR smaller solution space.  I didn't spend too much time on this so a lot of the rules are useless or redundant.