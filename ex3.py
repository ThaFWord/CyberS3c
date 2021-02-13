#!/usr/bin/python3

from math import gcd

def mmc(numeros):
    m = 2520
    for n in numeros:
        m = m * n // gcd(m, n)
    return m

numeros = range(2, 21)
print(mmc(numeros))