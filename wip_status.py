#!/usr/bin/env python2.6
__author__  = "Amer Aditya"

#This is Python Script is going to determin which all WIP are up & Down
#Also it will output  that UP & down in seperate WIP.text -> up_wip.txt & down_WIP.txt

import os
import socket
data =[]
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

def main():
        with open ("edr.txt",'r') as d_name :
                data=d_name.readlines()
                for domainName in data :
                        #print(domainName.strip('\n'))
                        domainName =  domainName.strip('\n')
                        #ping = ping_reach(domainName)
                        #print (ping)
                        host = host_lookup(domainName)
                        #print (host)
                        #if (ping == 0 and host == 1):
			if (host == 1):
                                os.popen("echo " + domainName + "  >> wip_up.txt")
                        else:
                                os.popen("echo " + domainName + "  >> wip_down.txt")
main()
