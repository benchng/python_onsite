'''
Write a script that takes in a list of numbers and:
    - sorts the numbers
    - stores the numbers in tuples of two in a list
    - prints each tuple


Notes:

If the user enters an odd numbered items in the list, add the last item
to a tuple with the number 0.

'''
'''
try:
    list_ = (input('Enter numbers with spaces : ')).split()
    
    f_list = []
    
    if len(list_) % 2 == 0:
        #print('length is even' , len(list_))
        for item in list_:
            f_list.append(float(item)) #Convert list to float
        else: #add a zero to the list to make it even
            list_.append(0)
                f_list.append(float(item)) # Convert list to float
        
except ValueError
    print('that\'s not a number restart the script')
    
'''

try:
    list_ = (input('Enter numbers with spaces : ')).split()

    f_list = []

    for item in list_:
        f_list.append(float(item)) # Convert list to float

except ValueError:
    print('that\'s not a number restart the script')

    f_list.sort()

    if len(f_list) % 2 != 0:
            f_list.append(0)

#create pairs
#print('Length ' , len(f_list))

tuple_pair_list = []
count = 0

for i in range(0, len(f_list), 2):
    #print(i)
    #count += i
    tuple_pair = (f_list[i], f_list[i+1])
    #print('index', i, i +1)
    #print(i, 'count', count)
    #print(tuple_pair)
    tuple_pair_list.append(tuple_pair)

print('Tuple Pair List', tuple_pair_list)

#prints each tuple
for pair in tuple_pair_list:
    print(pair)
