#Write a Python script to concatenate the following dictionaries to create a new one.
def concatenate_dicts(*dicts):
    concatenated_dict = {}
    for d in dicts:
        concatenated_dict.update(d)
    return concatenated_dict

dict1 = {1: 'a', 2: 'b'}
dict2 = {3: 'c', 4: 'd'}
dict3 = {5: 'e', 6: 'f'}

concatenated_dict = concatenate_dicts(dict1, dict2, dict3)
print("Concatenated Dictionary:", concatenated_dict)
