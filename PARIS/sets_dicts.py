set_a = {10, 20, 30, 40, 50}
set_b = {40, 50, 60, 70, 80}
print("Initial Set A:", set_a)
print("Initial Set B:", set_b)
set_a.add(60)
set_a.update([70, 80])
print("After adding members:", set_a)
intersection_set = set_a.intersection(set_b)
print("Intersection:", intersection_set)
union_set = set_a.union(set_b)
print("Union:", union_set)
diff_set = set_a.difference(set_b)
print("Set Difference (A - B):", diff_set)
sym_diff_set = set_a.symmetric_difference(set_b)
print("Symmetric Difference:", sym_diff_set)
print("Length of Set A:", len(set_a))
print("Maximum value:", max(set_a))
print("Minimum value:", min(set_a))
set_a.clear()
print("Set A after clear():", set_a)

# Question 3 ) Write a Python program to find the sum of all items in the
sample_dict = {'a': 100, 'b': 200, 'c': 300}
total_sum = 0
for value in sample_dict.values():
    total_sum += value
print("Sum of all items:", total_sum)