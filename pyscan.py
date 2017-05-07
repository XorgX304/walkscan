import socket
import sys
import os
from sys import platform
from os import system

def sistema():

    if platform.startswith('linux'):
        system("clear")
    else:
        system("cls")


def banner():
    print('''

 _______           _______  _______  _______  _       
(  ____ )|\     /|(  ____ \(  ____ \(  ___  )( (    /|
| (    )|( \   / )| (    \/| (    \/| (   ) ||  \  ( |
| (____)| \ (_) / | (_____ | |      | (___) ||   \ | |
|  _____)  \   /  (_____  )| |      |  ___  || (\ \) |
| (         ) (         ) || |      | (   ) || | \   |
| )         | |   /\____) || (____/\| )   ( || )  \  |
|/          \_/   \_______)(_______/|/     \||/    )_)

                                                      
github: github.com/gDutr4
email: devgabrieldutra@gmail.com

    ''')

'''
def argumentos():

    if len(sys.argv) != 2:
        print "#=========================================#"
        print "#  Exemplo: python pyscan.py google.com   #"
        print "#=========================================#"
'''

def main():
    host = sys.argv[1];

    ports = [21, 22, 23, 25, 26, 53, 57, 80, 81, 88,
            115, 118, 119, 137, 138, 135, 443, 445,
            514, 901, 911, 1521, 2082, 3306, 5435]

    for port in ports:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(0.05)
        r = client.connect_ex((host, port))

        if r == 0:
            print str(port) + "-> open"

sistema()
banner()
main()

print "#======================#"
print "#     Finish scan      #"
print "#======================#"
