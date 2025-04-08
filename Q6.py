
my_dict = {'apple': 5, 'banana': 2, 'cherry': 8, 'mango': 3}

sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1]))

print("Sorted dictionary (by value):", sorted_dict)
