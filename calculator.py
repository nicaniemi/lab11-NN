import math
"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
def add(a, b): 
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a*b
def divide(a, b):
    try:
        return b/a
    except ZeroDivisionError:
        return "Cannot divide by 0"
def logarithm(a, b):
    try:
        return math.log(a, b)
    except ValueError:
        return "Error: Cannot log a negative number"
def exponent(a, b):
    return a**b


