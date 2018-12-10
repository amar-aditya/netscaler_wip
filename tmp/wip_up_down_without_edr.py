#This is Python Script is going to determin which all WIP are up & Down
#Also it will output  that UP & down in seperate WIP.text -> up_wip.txt & down_WIP.txt
import os
import socket

def ping_reach(host):
	hostname =  host
	response = os.system('ping -c 1 ' + hostname)
	return response
def host_lookup(host):
	hostname = host
	try:
		socket.gethostbyname(hostname)
		return 1
	except socket.error:
		return 0
data =[]

with open ("domainName.txt",'r') as d_name :
	data=d_name.readlines()
	for domainName in data :
		#print(domainName.strip('\n'))
		domainName =  domainName.strip('\n')
		ping = ping_reach(domainName)
		host = host_lookup(domainName)
		if (ping == 0 and host == 1):
			os.system("echo " + domainName + " is up & running >> wip_up")
		else:
			os.system("echo " + domainName + "sesms to be down, Pls. check Manually >> wip_down")
			
