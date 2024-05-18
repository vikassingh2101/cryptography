#!/usr/bin/env python

def MillerRabinTest(n):
    if n == 2:
        return "Prime"
    elif n % 2 == 0:
        return "Composite"
    else:
        k = 0
        q = n - 1
        while q % 2 == 0:
            k += 1
            q = q // 2

        for a in range(2, n-1):
            if (a ** q) % n == 1:
                continue

            flag = False
            for j in range(0, k):
                if (a ** ((2 ** j) * q)) % n == (n - 1):
                    flag = True
                    break

            if flag is False:
                return "Composite"

        return "Highly likely to be a prime number"


n = int(input("Enter an integer to test for primality:"))
print(MillerRabinTest(n))
