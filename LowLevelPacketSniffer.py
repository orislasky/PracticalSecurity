# This script should be run as admin
import socket

def notinteresting():
	print ("I have no interst in news or whatever else you're browsing...")
	notinteresting.__code__ = (lambda:None).__code__

def gotcha():
	print ("Hey! You're browsing amazon!!! I'm going to start logging what you will type!!")
	gotcha.__code__ = (lambda:None).__code__


def snifferFunc():
	#Create a new socket using the given address family, socket type and protocol number.
	s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP) # on linux the address family is different

	# gethostname() returns a string containing the hostname of the machine where the Python interpreter is currently executing.
	# gethostbyname() translates a host name to IPv4 address format, extended interface.
	hostIp = socket.gethostbyname(socket.gethostname())

	s.bind((hostIp, 0)) # Binds the socket to address.

	# iInclude IP headers
	s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

	# receive all packages
	s.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

	# An infinite loop, so our bot can monitor the traffic indefinitely!
	while True:

		# Receive data from the socket. The return value is a pair (string, address)
		# where string is a string representing the data received and address is the
		# address of the socket sending the data.
		# For best match with hardware and network realities, the value of bufsize
		# should be a relatively small power of 2, for example, 4096
		data = s.recvfrom(65565)[0]
		# print (data)
		if 'amazon.com' in str(data):
			gotcha()
		else:
			notinteresting()

snifferFunc()
