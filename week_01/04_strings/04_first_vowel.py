'''
Write a script that finds the first vowel in a a user inputted string.

'''

vowels= 'aeiou'
count = 0
string = 'Hello World'
for s in string:
        if s in vowels: count=count+1

print(count)