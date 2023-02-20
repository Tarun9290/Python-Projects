#ROOTS OF QUADRATIC EQUATION CODE IN PYTHON

import cmath 

a = int(input())
b = int(input())
c = int(input())

# calculate the discriminant
d = (b**2) - (4*a*c)

# find two solutions
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)

print('The solutions are {0} and {1}'.format(sol1,sol2))