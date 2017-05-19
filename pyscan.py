import socket
import sys
import os
from sys import platform
from os import system


def start_system():

    if platform.startswith('linux'):
        system("clear")
    else:
        system("cls")


def all_services():
	return {
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


github: github.com/JulioOliveiraCosta
github: github.com/gDutr4
email: devgabrieldutra@gmail.com


    ''')


def all_ports():
	return [21, 22, 23, 25, 26, 53, 57, 80, 81, 88,
            115, 118, 119, 135, 137, 443, 445,
            514, 901, 1521, 2082, 3306, 5435]


def main():
	try:
		host = sys.argv[1];

		services = all_services()

		ports = all_ports()
		
		count_open = 0

		for port in ports:
			client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			client.settimeout(0.05)

			if client.connect_ex((host, port)) == 0:
				if str(port) in services:
					print("{}({}) is OPEN MOTHERFUCK!".format(str(port), services[str(port)]))
					
					count_open += 1
		
		if count_open == 0:
			print("Nothing OPEN MOTHERFUCK!")
	
	except IndexError:
		print("You need at least one argument MOTHERFUCK!")

		
def finish_scan():
	print ("\n\n")
	print ("#======================#")
	print ("#                      #")
	print ("#     Finish scan      #")
	print ("#                      #")
	print ("#======================#")



if __name__ == '__main__':
	start_system()
	banner()
	main()
	finish_scan()
	
