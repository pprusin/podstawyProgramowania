#Write a Python program to remove spaces from a given string.
def remove_spaces(string):
    return string.replace(" ", "")

input_string = "This is a sample string with spaces."
result = remove_spaces(input_string)
print("String after removing spaces:", result)
