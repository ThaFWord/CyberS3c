#!/usr/bin/python3

def segparahoras(segundos):
    a=str(segundos//3600)
    b=str((segundos%3600)//60)
    c=str((segundos%3600)%60)
    d=["{} horas {} minutos {} segundos".format(a, b, c)]
    return d

seg = int(input("Quantos segundos das? "))

print(segparahoras(seg))