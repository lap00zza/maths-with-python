import math

# math module has some commonly used constants
print(math.pi)

# we can use one of those constants to help us find the area of circle
def circle_area(r):
    return math.pi*r**2
radius = 3
print("Area =", circle_area(radius))

# we can also find the factorials of numbers
# 5! = 5x4x3x2x1
n = 5
print("{}! = {}".format(n, math.factorial(n)))

# and find the greatest common divisor
gcd = math.gcd(25, 120)
print(gcd)

# also lcm :)
lcm = math.lcm(2,3,19,56, 70)
print(lcm)

print(math.cbrt(39999))

# e**x
print(math.e) # eulers constant
print(math.exp(2))
# 2**x
print(math.exp2(2))
print(4**2) #important

print(math.fabs(-4))
