#!/usr/bin/python3

import string, sys, zipfile, os.path

if len(sys.argv) < 3:
    print("Argumentos insuficientes")
    sys.exit(0)

zip_file = sys.argv[1]
wordlist = sys.argv[2]

if os.path.exists(zip_file) == False:
    print("\nFicheiro zip " + zip_file + " não encontrado")
    sys.exit(0) 

if os.path.exists(wordlist) == False:
    print("\nFicheiro de senha " + wordlist + " não encontrado")
    sys.exit(0) 


ficheiro_zipado = zipfile.ZipFile(zip_file)

with open (wordlist, "rb") as wordlist:
    for word in wordlist:
        word = word.strip()
        try:
            ficheiro_zipado.extractall(pwd=word)
        except zipfile.BadZipFile:
            print ("Ocorreu um erro a abrir o ficheiro")
            sys.exit(0)
        except Exception as Erro:
            if "Senha inválida" in str(Erro):
                pass
            else:
                pass
        except KeyboardInterrupt:
                print("Programa interrompido")
                sys.exit()
        else:
            print("A password é:", word.decode())
            sys.exit(0)

print("\nSenha não encontrada, tente outra lista.")
