'''
Create a new dictionary using the three dictionaries below.
Then print out each key-value pair.

'''


dict_1 = {1: 1, 2: 4}
dict_2 = {3: 9, 4: 16}
dict_3 = {5: 25, 6: 36, 7: 49}

result = {key: dict_1.get(key, 0) + dict_2.get(key, 0) + dict_3.get(key, 0)
          for key in set(dict_1) | set(dict_2) | set(dict_3)}

print(result)