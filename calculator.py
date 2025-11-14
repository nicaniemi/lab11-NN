#https://github.com/nicaniemi/lab11-NN.git
import math
def square_root(a):
    try:
        return math.sqrt(a)
    except ValueError as e:
        raise e
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
    except ZeroDivisionError as e:
        raise e
def logarithm(a, b):
    try:
        return math.log(a, b)
    except ValueError as e:
        raise e
def exp(a, b):
    return a**b


