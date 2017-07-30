import socket
import sys
import argparse
from sys import platform
import os


def start_system():

    if platform.startswith('linux') or platform.startswith('darwin'):
       os.system("clear")
       return
    else:
        os.system("cls")
    
def all_services():
	return {
		21: "FTP",
		22: "SSH",
		23: "TelNet",
		25: "SMTP",
		26: "RSFTP",
		53: "DNS",
		57: "MTP",
		67: "DHCP",
		68: "DHCP",
		80: "HTTP",
		81: "SKYPE",
		88: "Kerberos",
		115: "SFTP",
		118: "SQL services",
		119: "NNTP",
		135: "RPC",
		137: "NetBios",
		443: "HTTPS",
		445: "microsoftDS",
		514: "SysLog",
		901: "Samba",
		1521: "Oracle DB",
		2082: "Cpanel",
		3306: "MySql",
		5432: "PostgreSQL"
	}


def banner():
    print('''
-----------------------------------------------------------
 _______           _______  _______  _______  _
(  ____ )|\     /|(  ____ \(  ____ \(  ___  )( (    /|
| (    )|( \   / )| (    \/| (    \/| (   ) ||  \  ( |
| (____)| \ (_) / | (_____ | |      | (___) ||   \ | |
|  _____)  \   /  (_____  )| |      |  ___  || (\ \) |
| (         ) (         ) || |      | (   ) || | \   |
| )         | |   /\____) || (____/\| )   ( || )  \  |
|/          \_/   \_______)(_______/|/     \||/    )_)

Author: Gabriel Dutra(T9xx)
github: github.com/T9xx
email: devgabrieldutra@gmail.com
------------------------------------------------------------
    ''')

def attempt_connections(host):
	"""Attempts to connect to the ports pre defined in the all_services function
	:param host the connection target host
	"""
	open_ports = []

	for port in all_services().keys():
		client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		client.settimeout(0.05)
                host = socket.gethostbyname(host)
		if client.connect_ex((host, port)) == 0:
			open_ports.append(port)
                client.close
	return open_ports, host


def print_results(host, open_ports):
	"""Prints the results the results based on the open ports
	:param host: the connection target host
	:param open_ports: a list containing the open ports(ports must be int)
	"""
	#print("Target MOTHERFUCKING host is {}".format(host))
	
	print("------------------------------------------------------------")
	print("Address: {}".format(attempt_connections(host)[1]))
	print("Host: {}".format(host))
	print("------------------------------------------------------------\n\n")

	if len(open_ports) == 0:
		print("Nothing OPEN")

	else:
		for port in open_ports:
			print("{}\t({})\tis OPEN".format(port, all_services()[port]))

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('--host', action='store', dest='host', help='Informe o host')
        parser.add_argument('-w', '--write', help='Save the output results.', action='store', metavar='File')
        args = parser.parse_args()

        if args.write is not None:
            sys.stdout = open(args.write, 'w')

        if args.host:                 
            try:
                host = args.host
	        open_ports = attempt_connections(host)[0]
	        print_results(host, open_ports)
            except socket.gaierror:
                print("You need to give proper hostname")
        else:
            parser.print_help()
            sys.exit(1)
        

if __name__ == '__main__':
	start_system()
	banner()
	main()
