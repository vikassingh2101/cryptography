#!/usr/bin/env python

print("Enter integers for which gcd is to be computed:")
x = int(input("Enter first integer:"))
y = int(input("Enter second integer:"))

if x >= y:
    a, b = x, y
else:
    a, b = y, x

r = a % b
while r != 0:
    a, b = b, r
    r = a % b

print("GCD({},{})={}".format(x, y, b))
