#Write a Python program to check if a dictionary is empty or not.
def is_dict_empty(d):
    return not bool(d)

sample_dict = {}
print("Is the dictionary empty?", is_dict_empty(sample_dict))

sample_dict = {'a': 1, 'b': 2}
print("Is the dictionary empty?", is_dict_empty(sample_dict))
