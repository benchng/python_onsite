'''
Write a script that takes a user inputted string
and prints it out in the following three formats.
    - All letters capitalized.
    - All letters lower case.
    - All vowels lower case and all consonants upper case.

'''

first = "starbucks"
second = ""
#vowels = 'aeiou'
vowels = ['a','e','i','o','u']

for i in first:
    if i in vowels:
        second = second+i.lower()
    else :
        second = second+i.upper()
print (second)