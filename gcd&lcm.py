#gcd and lcm

#OR
m=int(input('Enter m value'))
n=int(input('Enter n value'))
def gcd(m,n):
    r=m%n
    m=n
    n=r
    return m
print(gcd(2,3))
