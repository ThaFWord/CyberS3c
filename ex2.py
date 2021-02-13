#!/usr/bin/python3

import collections


p = int(input("Dá-me o primeiro valor "))
s = int(input("Dá-me o segundo valor "))
t = int(input("Dá-me o terceiro valor "))
q = int(input("Dá-me o quarto valor "))

lista = [p, s, t, q]
pares = 0
impares = 0

for item in lista:
    if item % 2 == 0:
        pares += 1
    else:
        impares += 1

diferentes = collections.Counter(lista).keys()

print("temos ", pares, "par(es) e", impares, "impar(es) e ", len(diferentes), "diferente(s)")