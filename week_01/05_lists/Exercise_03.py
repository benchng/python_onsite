'''
Sum up all elements from the nested list of integers below.

'''

list_ = [1, 2, [10, 11], [42, 3], 9]

flat_list = []
for i in list_:
    #if isinstance(i, list): if type(i) == list:
    if type(i) == list:
        for j in i:
            flat_list.append(j)
    else:
        flat_list.append(i)

print(flat_list)

