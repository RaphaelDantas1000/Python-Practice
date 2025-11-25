
## For Loop examples

for i in [1, 2, 3, 4, 5]:
    print(i)

for i in [10, 20, 30, 40, 50]:
    value = i ** 2    
    print(value)


## Example: counting approved and failed students

grades = [5, 6, 1, 3.5, 6.7, 9.6, 10, 8, 7.5, 1.3]

approved = 0    # counting how many students were approved
failed = 0      # counting how many students failed

for grade in grades:
    print("Student's grade:", grade)
    if grade < 6:
        failed = failed + 1
        print("failed")
    else:
        approved = approved + 1
        print("approved")

print(f"We have {failed} failed students and {approved} approved students.")
