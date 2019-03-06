'''
Take in a number from the user and print "Monday", "Tuesday", ...
"Sunday", or "Other" if the number from the user is 1, 2,... 7,
or other respectively. Use a "nested-if" statement.

'''


days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
leng_of_days = len(days)
#print(length_of_days)

user = int(input('Select a Number for a day: '))

if user <=  leng_of_days:
    print(days[user + -1])
else:
    print("other")

