## Functions Part 02:

def student_registration(name="Unknown", age=18):
    print(f"Student {name} is {age} years old")

student_registration("Yukio", 38)
student_registration(age=38)
student_registration(name="Yukio")


## Return:

def calculation(a=1, b=1, c=2, d=3):
    multiplication = a * b * c * d
    addition = a + b + c + d
    potency = (((a ** b) ** c) ** d)
    return addition

x = calculation(10, 2, 2, 3)
y = calculation(5, 2, 2, 3)

print(x * y)


## Returning multiple values:

def calculation(a=1, b=1, c=2, d=3):
    multiplication = a * b * c * d 
    addition = a + b + c + d 
    potency = (((a ** b) ** c) ** d)
    return addition, multiplication, potency

x = calculation(10, 2, 2, 1)
print(x)

x, y, z = calculation(10, 2, 2, 1)
print(x)
print(y)
print(z)
  