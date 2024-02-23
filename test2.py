# Define a class representing a person
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Define a function to calculate the factorial of a number
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Create a list of numbers
numbers = [1, 2, 3, 4, 5]

# Calculate and print the factorial of each number in the list
for num in numbers:
    print(f"The factorial of {num} is {factorial(num)}")

# Create an instance of the Person class
person = Person("Alice", 30)

# Call the greet method of the Person instance
person.greet()
