import math
def square_root(a):
    try:
        return math.sqrt(a)
    except ValueError:
        return "Error: Cannot take square root of a negative number"
def hypotenuse(a, b):
    return math.hypot(a, b)
def add(a, b): 
    return a + b
def subtract(a, b):
    return a - b
def mul(a, b):
    return a*b
def div(a, b):
    try:
        return b/a
    except ZeroDivisionError:
        return "Cannot divide by 0"
def logarithm(a, b):
    try:
        return math.log(a, b)
    except ValueError:
        return "Error: Cannot log a negative number"
def exp(a, b):
    return a**b


