'''
Write a function called most_frequent that takes a string and prints
the letters in decreasing order of frequency.

For example, the follow string should produce the following result.

string_ = 'hello'

Output:
l, h, e, o

For letters that are the same frequency, the order does not matter.

'''


my_string = "hi there"
new_stringset = set(my_string)
my_dict= {}


for item in my_string:
    if item in my_dict.keys():
        my_dict[item] = my_dict[item] + 1
    else:
        my_dict[item] = 1
print (my_dict)

print(set(my_dict))

new_list = []



for key, value in my_dict.items():
    key_value_list = []
    key_value_list.append(value)
    key_value_list.append(key)
    new_list.append(key_value_list)

new_list.sort()
new_list.reverse()

print(new_list)

for i in new_list:
    print(i[1])




#x = sorted(my_dict.items(), key=lambda kv: kv[1], reverse=True)

#print (x)
