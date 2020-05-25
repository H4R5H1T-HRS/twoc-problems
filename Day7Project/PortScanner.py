#!/bin/python3
import sys
import socket
from datetime import datetime

#Define our Target
if len(sys.argv) == 2: #If User give two arguments (Script name & IP address)
	target = socket.gethostbyname(sys.argv[1]) #Translate Hostname to IPv4
else:
	print("Invalid amount of arguments.")
	print("Syntax: python3 PortScanner.py <ip>")

#Banner
print("-"*50)
print("Scanning taget"+target)
print("Time started: "+str(datetime.now()))
print("-"*50)

try:
	for port in range (1,65535):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
		#AF_INET is IPv4 & SOCK_STREAM is Port
		socket.setdefaulttimeout(1)
		result = s.connect_ex((target,port)) #Returns an error indica
		#print(f"Checking port {port}")
		if result == 0:
			print(f"Port {port} is opent")
		s.close()

except KeyboardInterrupt:
	print("\nExiting Program.")
	sys.exit()

except socket.gaierror:
	print("Hostname could not be resolved.")
	sys.exit()

except socket.error:
	print("Couldn't connect to server.")
	sys.exit()

