 ## Conditionals

score = 5

if score < 6:
    print("Failed")
else:
    print("Approved")


## Multiple conditions

if score > 8:
    print("Excellent")
elif score >= 6 and score < 8:
    print("Good")
else:
    print("Bad")


## Using input()

score = float(input("Insert your score here: "))

if score > 8:
    print("Excellent")
elif score >= 6 and score < 8:
    print("Good")
else:
    print("Bad")


## Investment term example

term = int(input("What is the term of your financial investment (in days)? "))
performance = float(input("What is the return on your investment? "))

if term < 180:
    rate = 0.225    # 22.5%
elif term <= 360:
    rate = 0.20     # 20%
elif term <= 720:
    rate = 0.175    # 17.5%
else:
    rate = 0.15     # 15%

tax = rate * performance

print("The tax rate levied on your investment is:", tax)
          
           