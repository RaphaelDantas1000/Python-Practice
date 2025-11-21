## 2.3 — Booleans (True and False)

age = input("What's your age? ")
age = int(age)

print(age >= 18)          # comparison
print(type(age >= 18))    # bool
print((age >= 18) + 1.5)  # True→1 or False→0


## 2.4 — Lists
# A collection of items, mutable, multiple values in one variable

salary = [1500, 2000, 1300, 1800, 1700]

print(salary[1])    # accessing the second salary
print(salary[-1])   # accessing the last salary

salary.append(1300)
print(salary)

print(salary * 3)   # repetition of list
print(type(salary))


## 2.5 — Tuples (immutable list-like objects)

salary_tuple = (1500, 2000, 1300, 1800, 1700)

print(type(salary_tuple))

# salary_tuple.append(1300)   # ERROR — tuples are immutable

print(salary_tuple * 2)       # repetition works
print(type(salary_tuple))


## 2.6 — Dictionaries (key–value pairs)

client = {
    "name": "Yukio",
    "age": 37,
    "city": "Sao Paulo"
}

print(client["age"])      # access value

client["age"] = 38        # modify value

print(type(client))


## 2.7 — Sets (unordered, unique items)

ids = {39495, 2943848, 293985, 392843}

# ids[0]  # ERROR — cannot access by index

ids.add(2049402)          # add new item

print(ids)


