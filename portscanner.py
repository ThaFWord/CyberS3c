#!/usr/bin/python3

import os, datetime, socket, time, threading, sys
from concurrent.futures import ThreadPoolExecutor

ipAddr = input("Por favor insira um IP valido > ")
if not os.path.isdir("Scans"):
    os.mkdir("Scans")
    os.chdir("Scans")

def portScanner(ip, port):
    try:
        file = open("portscan.txt", "a")
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        resultado = sock.connect_ex((ip, port))
        if resultado == 0:
            print("Port " + str(port) + " is open\n")
            file.write("Port " + str(port) + " is open\n")
        else:
            print("Port " + str(port) + " is closed" )
        sock.close()
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


t0 = datetime.datetime.now()
if __name__ == "__main__":
    thread_lock = threading.Lock()
    port = 0
    executer = ThreadPoolExecutor(max_workers=30)
    for port in range(1, 1025):
        executer.submit(portScanner)
        x = threading.Thread(target=portScanner, args=(ipAddr, port,))
        x.start()
t1 = datetime.datetime.now() - t0
print("Demorou " + str(t1) + " segundos")

