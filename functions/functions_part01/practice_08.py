## Functions (Funções) – Python Course 2, Part 1

## Functions are reusable blocks of code that perform a specific task.
## You define them once and can call them anywhere to avoid repetition.

def greeting():
    print("Hello, Welcome!")

greeting()   ## Calling the function


## Using function parameters:

def sum(a, b):
    result = a + b 
    print(f"The sum of {a} + {b} is {result}")

sum(10, 5)
sum(3, 2)


def multiplication(a, b, c, d):
    result = a * b * c * d 
    print(f"The result of the multiplication of {a}, {b}, {c} and {d} is {result}")

multiplication(10, 4, 3, 1)


def calculation(a, b, c, d):
    result = a * b
    result = result - c + d
    print(f"The calculation with {a}, {b}, {c}, {d} results in {result}")

calculation(2, 2, 4, 5)
