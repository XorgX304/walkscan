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

servicos = {
    "21": "FTP",
    "22": "SSH",
    "23": "TelNet",
    "25": "SMTP",
    "26": "RSFTP",
    "53": "DNS",
    "80": "HTTP",
    "81": "SKYPE",
    "88": "Kerberos",
    "115": "SFTP",
    "118": "SQL services",
    "119": "NNTP",
    "137": "NetBios",
    "443": "HTTPS",
    "445": "microsoftDS",
    "514": "SysLog",
    "901": "Samba",
    "1521": "Oracle DB",
    "2082": "Cpanel",
    "3306": "MySql",
    "5432": "PostgreSQL"

    }

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
Exemplo: python pyscan.py google.com

    ''')

'''
def help():
    if(argv[1] == "-h"):
        print ("#=========================================#")
        print ("#  Exemplo: python pyscan.py google.com   #")
        print ("#=========================================#")
'''

def main():
    
    host = sys.argv[1];

    ports = [21, 22, 23, 25, 26, 53, 57, 80, 81, 88,
            115, 118, 119, 135, 137, 443, 445,
            514, 901, 1521, 2082, 3306, 5435]

    for port in ports:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(0.05)
        r = client.connect_ex((host, port))

        if r == 0:
            if str(port) in servicos:
                print("{}({}) is OPEN MOTHERFUCK!".format(str(port), servicos[str(port)]))

#chamando as funcoes do script
sistema()
banner()
main()

print ("\n\n")
print ("#======================#")
print ("#                      #")
print ("#     Finish scan      #")
print ("#                      #")
print ("#======================#")
