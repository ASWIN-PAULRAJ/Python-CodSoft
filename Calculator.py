#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return " Error! Cannot perform divide by zero"
    
def modulus(x,y):
    if y != 0:
        return x % y
    else:
        return "Error! Cannot perform modulus with zero"

def calculator():
    print("Simple Calculator")

    
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    
    print("Choose operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")

    
    choice = input("Enter choice (1/2/3/4/5): ")

    
    if choice == '1':
        result = add(num1, num2)
    elif choice == '2':
        result = subtract(num1, num2)
    elif choice == '3':
        result = multiply(num1, num2)
    elif choice == '4':
        result = divide(num1, num2)
    elif choice== '5':
        result =modulus(num1,num2)
    else:
        result = "Invalid Input"

    
    print("Result: ", result)


calculator()


# In[ ]:




