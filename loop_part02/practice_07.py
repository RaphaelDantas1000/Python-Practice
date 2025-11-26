
## Part two: While loop

value = 0

for i in [10, 15, 30, 35, 50]:
    print("i =", i)
    if i % 2 == 0:
        value += 1        ## Obs: This can also be written as: value = value + 1
    print("value =", value)


for n in range(5):
    print(n)


counter = 0

for n in range(5):
    counter += 1

print(counter)


counter = 1

while counter < 5:
    counter += 1
    print("after being added", counter)


## While can create infinite loops, example:

counter = 1

while counter < 5:
    print(counter)


option = ""

while option != "3":
    print("\n=== MENU ===")
    print("1 - See Message")
    print("2 - See Other Message")
    print("3 - Leave")

    option = input("Choose an option: ")

    if option == "1":
        print("Option 1 selected")
    elif option == "2":
        print("Option 2 selected")
    elif option == "3":
        print("Shutting down program...")
    else:
        print("Option not valid. Try again")


while True:
    password = input("Type the password: ")
    if password == "1234":
        print("Access granted!")
        break
    else:
        print("Incorrect password. Try again.")


maximum_attempts = 3
attempts_made = 0
right_password = "password123"

while attempts_made < maximum_attempts:
    password_attempt = input("Type your password: ")
    attempts_made += 1

    if password_attempt == right_password:
        print("Access granted!")
        break  ## Stops loop as soon as the right password is inserted
    else:
        print(f"Incorrect password. You still have {maximum_attempts - attempts_made} attempts")

    if attempts_made == maximum_attempts:
        print("The maximum number of attempts has been exceeded. Access blocked")



