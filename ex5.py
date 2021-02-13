#!/usr/bin/pyton3

import string, random

letra1 = str(input("Escolhe a primeira letra: ")).lower()
letra2 = str(input("Escolhe a segunda letra: ")).lower()

alfabeto = string.ascii_lowercase

opçao1 = alfabeto.find(letra1)
opçao2 = alfabeto.find(letra2)

posiçaonormal = (opçao1 + opçao2) /2

if opçao1 > opçao2:
    posiçaonormal = posiçaonormal +0.5
    print("A letra que se encontra entre ambas é ", alfabeto[int(posiçaonormal)])
else:
    print("A letra que se encontra entre ambas é ", alfabeto[int(posiçaonormal)])