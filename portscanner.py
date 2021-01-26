#!/usr/bin/python3

import os, datetime, socket, time, threading, sys, queue
from concurrent.futures import ThreadPoolExecutor


ipAddr = input("Por favor insira um IP valido > ")
if not os.path.isdir("Scans"):
    os.mkdir("Scans")
    os.chdir("Scans")

def portScanner(ip, port):
    with threading.Lock():
        try:
            file = open("portscan.txt", "a")
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            resultado = sock.connect_ex((ip, port))
            if resultado == 0:
                print("A porta " + str(port) + " esta aberta\n")
                file.write("A porta " + str(port) + " esta aberta\n")
            else:
                print("Port " + str(port) + " esta fechada" )
            sock.close()
            q.task_done()
            file.close()
        except socket.gaierror:
            print("Nao foi possivel identificar o endereco.")   
            sys.exit()
        except socket.error:
            print("Ocorreu um erro de socket.")
            sys.exit()
        except KeyboardInterrupt:
            print("Scan terminado com sucesso.")
            sys.exit()
        except:
            print("Ocorreu um erro")
            sys.exit()

q = queue.Queue()

t0 = datetime.datetime.now()
if __name__ == "__main__":
    port = 0
    for port in range(1, 1025):
        x = threading.Thread(target=portScanner, args=(ipAddr, port,))
        x.deamon = True
        x.start()
        x.join()
        
    for item in range(1025):
        q.put(item)
        
t1 = datetime.datetime.now() - t0
print("Demorou " + str(t1) + " segundos")

q.join()
