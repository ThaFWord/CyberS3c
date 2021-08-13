#!/usr/bin/python3

import random, string

caracteres = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation 
tamanho = 0 
password = "" 

file = open("password.txt","a") 

while tamanho < 8 or tamanho > 32: 
    tamanho = int(input("Sendo o numero minimo 8 e o maximo 32 qual o numero de carecteres que pretende para a password\n"))
    if tamanho < 8 or tamanho > 32:
        print("O numero escolhido nao corresponde ao solicitado")
    else: 
        print("Tamanho de password dentro dos parâmetros.")
        for x in range (tamanho):
            password += random.choice(caracteres)
        print ("A password gerada é: ", password, sep="" ) 
        file.write( password + "\n")

file.close()
