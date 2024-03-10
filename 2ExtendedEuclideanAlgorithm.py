#!/usr/bin/python3

print("Enter integers for which gcd is to be computed:")
m = int(input("Enter first integer:"))
n = int(input("Enter second integer:"))

if m >= n:
    a, b = m, n
else:
    a, b = n, m

x0, x1 = 1, 0
y0, y1 = 0, 1

r = a % b

while r != 0:
    q = a // b
    x2 = x0 - q * x1
    y2 = y0 - q * y1
    a, b = b, r
    x0, x1 = x1, x2
    y0, y1 = y1, y2
    r = a % b

print("GCD({},{})={}".format(m, n, b))
if m >= n:
    print("x={}, y={}".format(x2, y2))
else:
    print("x={}, y={}".format(y2, x2))