#Write a Python program to check whether a string starts with specified characters.
def starts_with(string, start):
    return string.startswith(start)

input_string = "Python is great"
specified_characters = "Py"
if starts_with(input_string, specified_characters):
    print("The string starts with specified characters.")
else:
    print("The string does not start with specified characters.")
