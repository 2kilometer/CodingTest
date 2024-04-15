from math import prod
from fractions import Fraction
def solution(a, b):
    b = Fraction(a,b).denominator
    
    def divide(b):
        if b%2 == 0:
            return divide(b/2)
        elif b%5 == 0:
            return divide(b/5)
        elif b == 1:
            return 1
        else:
            return 2
    
    return divide(b)