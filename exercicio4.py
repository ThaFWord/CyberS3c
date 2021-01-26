import os, sys

path = "."

print("\nSe bem vindo ao CrApRe \n")

def makeDir():
    nome = input("Qual o nome para a pasta? ")
    if os.path.exists(nome):
        print ("\nO nome ja existe, escolhe outro\n")
        main ()
    else:
        print ("\nCriado com sucesso\n")
        os.mkdir(nome)
        main()

def remDir():
    nome2 = input("Qual a pasta/ficheiro que queres eliminar? ")
    if os.path.exists(nome2):
        os.rmdir(nome2)
        main()
    else:
        print("\nO nome que escolheste nao existe\n")
        main()
    

def listDir():
    print (os.listdir())
    main()

def renameDir():
    qual = input("Qual queres renomear? ")
    if os.path.exists(path):
        novonome = input("Qual o novo nome? ")
        os.rename(qual, novonome)
        print("\nNome alterado\n")
        main()
    else:
        print("\nO nome que indicaste nao existe\n")
    
def main():
    print("\nPodes escolher \n[1] Criar uma pasta \n[2] Remover \n[3] Listar as pastas que tens \n[4] Renomear\n[5] Sair\n")
    resposta = input("\nQual queres? ")
    if resposta == "1":
        makeDir()

    if resposta == "2":
        remDir()

    if resposta == "3":
        listDir()

    if resposta == "4":
        renameDir()

    if resposta == "5":
        sys.exit()
    else:
        print("Escolhe uma opçao valida")

main()
