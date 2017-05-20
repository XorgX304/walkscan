import socket
import sys
from sys import platform
from os import system


def start_system():

    if platform.startswith('linux') or platform.startswith('darwin'):
        system("clear")
    else:
        system("cls")


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

 _______           _______  _______  _______  _
(  ____ )|\     /|(  ____ \(  ____ \(  ___  )( (    /|
| (    )|( \   / )| (    \/| (    \/| (   ) ||  \  ( |
| (____)| \ (_) / | (_____ | |      | (___) ||   \ | |
|  _____)  \   /  (_____  )| |      |  ___  || (\ \) |
| (         ) (         ) || |      | (   ) || | \   |
| )         | |   /\____) || (____/\| )   ( || )  \  |
|/          \_/   \_______)(_______/|/     \||/    )_)


github: github.com/JulioOliveiraCosta
github: github.com/mr0mx
github: github.com/fbleite
email: devgabrieldutra@gmail.com


    ''')

def attempt_connections(host):
	"""Attempts to connect to the ports pre defined in the all_services function
	:param host the connection target host
	"""
	open_ports = []

	for port in all_services().keys():
		client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		client.settimeout(0.05)

		if client.connect_ex((host, port)) == 0:
			open_ports.append(port)

	return open_ports


def print_results(host, open_ports):
	"""Prints the results the results based on the open ports
	:param host: the connection target host
	:param open_ports: a list containing the open ports(ports must be int)
	"""
	print("Target MOTHERFUCKING host is {}".format(host))
	if len(open_ports) == 0:
		print("Nothing OPEN MOTHERFUCK!")
	else:
		for port in open_ports:
			print("{}({}) is OPEN MOTHERFUCK!".format(port, all_services()[port]))

def main():
	try:
		host = sys.argv[1];
		open_ports = attempt_connections(host)
		print_results(host, open_ports)
	
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
	
