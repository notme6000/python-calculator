import math

c=0

def addition(a,b):
    global c
    c = a+b
    

def subtraction(a,b):
    global c
    c = a-b
    

def multiplication(a,b):
    global c
    c = a*b
    

def division(a,b):
    global c
    c = a/b
    

def exponent(a,b):
    global c
    c = a**b
    

def calculator():
    a = int(input("enter a number:"))
    b = int(input("enter a number:"))

    print(" 1.addition\n 2.subtraction\n 3.multiplication\n 4.division\n 5.exponent")
    operator = int(input("select an operation:"))

    if operator == 1:
        addition(a,b)
    elif operator == 2:
        subtraction(a,b)
    elif operator == 3:
        multiplication(a,b)
    elif operator == 4:
        division(a,b)
    else:
        exponent(a,b)

calculator()
print("result = ",c)