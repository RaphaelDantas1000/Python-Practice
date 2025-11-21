## 1 — Introduction: Dynamic Typing in Python

salary = 10000
print(type(salary))       # int

salary = "123"
print(type(salary))       # str


## 2 — Data types in Python

# Numbers (int, float)
# Strings (str)
# Booleans (bool)
# Tuples (tuple)
# Sets (set)


## 2.1 — Integers and Floats

x = 10
print(type(x))            # int

x = float(x)
print(type(x))            # float

x = int(x)
print(type(x))            # int

y = 3.7
print(type(y))            # float

print(int(y))             # 3

print(x + y)              # 10 + 3.7 = 13.7

text = "123"
print(x + y + float(text))


## 2.2 — Strings

name = "Yukio"
position = "Data scientist"

print(name + " " + position)

print(name[0])            # first letter: 'Y'
print(name[0:3])          # 'Yuk'
print(name[-1])           # last letter
print(position[-5:])      # last 5 characters








