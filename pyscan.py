import socket

print('''\033[0;35m
###############################################
#[+]Author:   mr0mx                           #
#[+]Email:    devgabrieldutra@gmail.com       #
#[+]Github:   github.com/mr0mx                #
#[+]Facebook: fb.com/mr0mx                    #
#[+]Version:  1.0                             #
#[+]Exemple:  Host: 192.168.1.1               #
#             TimeOut: 0.05                   #
###############################################
\033[0;36m
''')

host = raw_input("Host: ")
timeout = float(raw_input("Timeout: <default = 0.05>: "))

ports = [21, 22, 23, 25, 80, 135, 443, 3306]

for port in ports:
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	client.settimeout(timeout)
	resp = client.connect_ex((host, port))

	if resp == 0:
		print str(port) + "-> Open"

	else:
		print str(port) + "-> Closed"

print "Scan Finalizado"
