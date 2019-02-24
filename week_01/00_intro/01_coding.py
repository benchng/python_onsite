'''
Write the necessary code to display the follow message to the console
Challenge: write code to duplicate the "co-" part
instead of writing it 3 times.

Time for co-co-co-ding.

'''


#1.
word = "ding"
word1 = "co-"

word2 = word1 * 3 + word
print(word2)

#2.
print('Time for ' + 'co-'* 3 + 'ding')

#3   012345
a = 'coding'
b = (a[0:2] + '-') * 3 + a[2:6]
c = 'Time for ' + b
print(c)

#4
x = ''
for i in range(3):
    x = x + "co-"
    print(i, x)
print('Time for ' + x + 'ding')

#f string is formatting variable and string together
#f string can input multiple variable inside the strings
# Using f string to add the "co variable inside the string and multiplying by 3
print(f"Time for {'co-' * 3}ding")