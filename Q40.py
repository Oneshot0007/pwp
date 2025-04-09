my_set = set()

# Add members
my_set.add("Apple")
my_set.add("Banana")
my_set.update(["Cherry", "Date"])  # Adding multiple items

print("Set after adding items:", my_set)

# Remove one item
my_set.remove("Banana")

print("Set after removing 'Banana':", my_set)
