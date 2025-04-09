
dict1 = {'a': 10, 'b': 20, 'c': 30}
dict2 = {'a': 5, 'b': 8, 'c': 15}

result = {}

for key in dict1:
    if key in dict2:
        result[key] = dict1[key] - dict2[key]

print("Result after subtraction:", result)
