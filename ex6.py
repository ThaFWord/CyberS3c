#usr/bin/python3

soma = int()
multi = []
soma = 0
       
for numero in range(1, 1000):
    if numero % 3== 0 or numero % 5 == 0:
        soma = soma + numero
        multi.append(numero)                

print("\n Os números divisíveis por 3 e 5 são: " + str(multi))
print("\n" "A soma dos números divisíveis por 3 e 5 é: " , str(soma))