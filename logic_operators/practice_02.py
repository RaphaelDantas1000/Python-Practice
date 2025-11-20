## Logical Operators in Python
## AND, OR, NOT

# -------------------------------
# AND Operator
# -------------------------------

age = int(input("Type your age: "))
status_hs = input("High School status (Concluded / Incomplete): ")

if age >= 18 and status_hs == "Concluded":
    print("Approved registration")
else:
    print("Registration not approved")

# -------------------------------
# OR Operator
# -------------------------------

years_as_client = int(input("For how long have you been a client: "))
balance = int(input("Amount invested in the bank: "))

if years_as_client >= 5 or balance >= 50000:
    print("Approved registration")
else:
    print("Registration not approved")

# -------------------------------
# NOT Operator
# -------------------------------

print(not True)   # False
print(not False)  # True

options = int(input("Select one of the options from 1 to 5: "))

if not options == 3:
    print("Forwarding to an agent...")
else:
    print("You need to speak with your account manager")

