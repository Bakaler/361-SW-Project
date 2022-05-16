import math

def sqrt(x : float or int) -> float or int:

    return abs(x) ** .5

def neg(x : float or int) -> float or int:
    return -x

def fact(x : float or int) -> float or int:
    print(x)
    return math.gamma(x+1)

def log(x : float or int) -> float or int:
    return math.log(x, 10)

def exp(x : float or int) -> float or int:
    return x * x

def square(x : float or int) -> float or int:
    return x ** 2

def recip(x : float or int) -> float or int:
    return 1/x

def TenPoY(x : float or int) -> float or int:
    return 10 ** x