import os


for line in open("/home/aditya/netscaler/domainName.txt", "r"):
	with open('domainName.txt') as f:
		mylist = f.read()	
		os.system (" cat ns.conf | grep -i "  + str(mylist) + " |cut -d ' ' -f4-6  > prod-cob.txt")	
	#print (line)
