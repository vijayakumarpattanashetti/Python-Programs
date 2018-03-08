#1 way
import math
a=math.factorial(3)
print(a)
#another way
from math import factorial
print (factorial(4))
#another way
def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
print(fact(5))


