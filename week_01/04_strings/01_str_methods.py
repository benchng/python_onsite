'''
There are many string methods available to perform all sorts of tasks.

Experiment with some of them to make sure you
understand how they work. strip and replace are particularly useful.

Python documentation uses a syntax that might be confusing.
For example, in find(sub[, start[, end]]), the brackets indicate
optional arguments. So sub is required, but start is optional, and if
you include start, then end is optional.

For this exercise, demonstrate the following string methods below:
- strip
- replace
- find

'''

sentence = " hEllo how are you?"

print((sentence.strip))
print((sentence.rstrip))
print((sentence.lstrip))

print(sentence.strip())
print(sentence.rstrip())
print(sentence.lstrip())

print(sentence.replace('l', 'LL'))

print(len(sentence))
print('\tFind R', sentence.rfind('h')) #find fines the first position on the argument to be seen
print(sentence[15])


print('\tFind R', sentence.rfind('h')) #finds the first posistion on the right hand side
print(sentence[2])

