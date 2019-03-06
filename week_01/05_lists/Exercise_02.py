'''
Given the two lists below, find the elements that are the same
and put them in a new list.
Put the elements that are different in another list.

Print both.
'''

list_one = [0, 4, 6, 18, 25, 42, 100]
list_two = [1, 4, 9, 24, 42, 88, 99, 100]


#4, 42, 100
#0, 1, 6, 9, 18, 24, 25, 88, 99


duplicate_list = []


for item in list_one:
    if item in list_two:
        duplicate_list.append(item)

#print(duplicate_list)


merge_list = list_two + list_one

#print(merge_list)

s = set(merge_list)

#print(s)

for i in duplicate_list:
    if i in s:
        s.remove(i)

print(duplicate_list)
print(s)




