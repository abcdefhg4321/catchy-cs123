# Last Edited by Ariix333
# Program make a simple calculator that can add, subtract, multiply and divide using functions. (additionally sin,cos,tan functions)
# This function adds two numbers 

import math

def add(x, y):
   return x + y
# This function subtracts two numbers 
def subtract(x, y):
   return x - y
# This function multiplies two numbers
def multiply(x, y):
   return x * y
# This function divides two numbers
def divide(x, y):
   return x / y
def sin(x):
   return math.sin(x)
def cos(x):
   return math.cos(x)
def tan(x):
   return math.tan(x)
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Sin")
print("6.Cos")
print("7.Tan")
print("8.Exit")
# Take input from the user 
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
i=1
while i==1:
    choice = input("Enter choice(1/2/3/4/5):")
    if choice == '1':
        print(num1,"+",num2,"=", add(num1,num2))
    elif choice == '2':
        print(num1,"-",num2,"=", subtract(num1,num2))
    elif choice == '3':
        print(num1,"*",num2,"=", multiply(num1,num2))
    elif choice == '4':
        print(num1,"/",num2,"=", divide(num1,num2))
    elif choice == '5':
        print("sin(",num1,")=", sin(num1))
    elif choice == '6':
        print("cos",num1,"=", cos(num1))
    elif choice == '7':
        print("tan",num1,"=", tan(num1))
    elif choice == '8':
        print("Exit. Good Bye")
        i=0
    else:    
        print("Invalid Input. Enter Again")
