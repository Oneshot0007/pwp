# Define two sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print("Set 1:", set1)
print("Set 2:", set2)

# Union
union_set = set1.union(set2)
print("\nUnion of sets:", union_set)

# Intersection
intersection_set = set1.intersection(set2)
print("Intersection of sets:", intersection_set)

# Set Difference
diff1 = set1.difference(set2)  
diff2 = set2.difference(set1)  
print("Set1 - Set2 (Difference):", diff1)
print("Set2 - Set1 (Difference):", diff2)

# Symmetric Difference
sym_diff = set1.symmetric_difference(set2)
print("Symmetric Difference:", sym_diff)
# Clear a set
set1.clear()
print("Set1 after clearing:", set1)
