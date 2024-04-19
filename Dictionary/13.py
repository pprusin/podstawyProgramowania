#Write a Python program to remove spaces from dictionary keys.
def remove_spaces_from_keys(d):
    return {key.replace(' ', ''): value for key, value in d.items()}

sample_dict = {'apple pie': 10, 'banana bread': 20, 'cherry tart': 30}

result = remove_spaces_from_keys(sample_dict)
print("Dictionary after removing spaces from keys:")
print(result)
