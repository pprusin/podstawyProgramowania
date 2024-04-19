# Write a Python program to get a dictionary from an object's fields.
class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

person_obj = Person("Alice", 30, "New York")

person_dict = vars(person_obj)

print("Dictionary from object's fields:")
print(person_dict)
