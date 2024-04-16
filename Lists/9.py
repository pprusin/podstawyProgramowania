#Write a Python program to clone or copy a list.
def clone_list(items):
    return items[:]

original_list = [1, 2, 3]
copied_list = clone_list(original_list)
print(copied_list)
