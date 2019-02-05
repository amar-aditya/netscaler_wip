#!/usr/bin/env python2.6
# This script will fetch all the Email owner info from the CSV file copied to directory.
#Provide - file_1 location - List of the WIP's down which has been earlier extracted from the  wip_status.py
#Provide - file_2 location - CSV file location
#For simplicity keep the name of the file_1 as file_1 & file_2 as email_info

import os
file_1 = raw_input ("Pls. enter the file location of the wip_down_list ")
file_2 = raw_input("Pls. enter the file location of the wip_owner ")
data_down = []
with open (file_1,'r') as read_down:
	data_down=read_down.readlines()
	for d in data_down:
		d=d.strip('\n')
		if d in open (file_2).read():
#			print (d)
#			output = (os.popen("cat 2  | grep -i ' " + d | ).read())
#			os.system("echo  " + output + "  >> info_e-mail")
#			print (output)
			os.system("cat  email_info | grep -P '^("+d+"?)' | head -1 >> mail.txt ")
#			os.system("cat"+file_2+"| grep -P '^("+d+"?)' | head -1 >> mail.txt ")

				
		else:
			os.system ("echo " + d + " >> mail_not_found.txt")

#os.system("cat mail.txt | sort -u >> e-mail.list")
