#!/usr/bin/python3

ipList = []
portList = []

ipListFile = open("ip.txt", "w")

portListFile = open("port.txt", "w")

for ip in range(1, 256):
    print(ip)
    ipListFile.write(str(ip) + '\n')

for port in range(1, 1025):
    print(port)
    portListFile.write(str(port) + '\n')

ipListFile.close()

portListFile.close()