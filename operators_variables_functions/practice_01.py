## Basic Operations

print(10+14)

## Variables

salary= 10000
pi = 3.1415
name= "Yukio"

random_calculation = salary ** 0.5 + pi * (salary/2)
print (random_calculation)

#Functions

def function_name():
    pass #steps you wish the function to have
    return None #this line gives you the result in a format you can you for other calculations


def ola_mundo():
    print ("Ola, mundo!")   

def net_salary (salary, tax):
    gross_salary = salary
    net_salary = salary * (1-tax)
    return net_salary
employee_salary1 = net_salary(2000,0.1)
employee_salary2 = net_salary(3500,0.14)

print(employee_salary1)
print(employee_salary2)



