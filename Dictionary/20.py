#Write a Python program to count the frequency of a dictionary.
from collections import Counter

original_dict = {'V': 10, 'VI': 10, 'VII': 40, 'VIII': 20, 'IX': 70, 'X': 80, 'XI': 40, 'XII': 20}

frequency_counter = Counter(original_dict.values())

print("Count the frequency of the dictionary:")
print(frequency_counter)
