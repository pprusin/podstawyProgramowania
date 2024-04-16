#Write a Python program to flatten a shallow list.
shallow_list = [[1, 2], [3, 4], [5, 6]]
flattened_list = [item for sublist in shallow_list for item in sublist]
print(flattened_list)
