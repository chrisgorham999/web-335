#======================================
# Title: gorham_calculator.py 
# Author: Chris Gorham
# Date: 27 Mar 2023
# Description: This is the code for the Python Calculator Assignment (Exercise 3.3)
# Sources Used:  Python String Concatenation and Formatting (https://www.pythonforbeginners.com/concatenation/string-concatenation-and-formatting-in-python)
#=====================================

#add function
def add(x, y):
    return(int(x) + int(y))

#subtract function
def subtract(x, y):
    return(int(x) - int(y))

#divide function
def divide(x, y):
    return(int(x) / int(y))

#multiply function
def multiply(x, y):
    return(int(x) * int(y))    

#define variables for the add demonstration
num1 = "5"
num2 = "6"
num3 = add(num1, num2)

#create the string for the add demonstration
add_demo = "%s + %s is %s." % (num1, num2, num3)
#print the add demonstration string
print(add_demo)

#define variables for the subtract demonstration
num4 = "8"
num5 = "4"
num6 = subtract(num4, num5)

#create the string for the subtract demonstration
subtract_demo = "%s - %s is %s." % (num4, num5, num6)
#print the subtract demonstration string
print(subtract_demo)

#define variables for the divide demonstration
num7 = "8"
num8 = "4"
num9 = divide(num7, num8)

#create the string for the divide demonstration
divide_demo = "%s / %s is %s." % (num7, num8, num9)
#print the divide demonstration string
print(divide_demo)

#define variables for the multiply demonstration
num10 = "8"
num11 = "4"
num12 = multiply(num10, num11)

#create the string for the multiply demonstration
multiply_demo = "%s * %s is %s." % (num10, num11, num12)
#print the multiply demonstration string
print(multiply_demo)


    