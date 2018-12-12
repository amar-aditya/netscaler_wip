#!/usr/bin/env python2.7
__author__  = "Amer Aditya" 
#This Python script will give below ouputs
#All the Domain from ns.conf
#All the prod_gslb_vserver which are active-active domain
#AlL the prod & cob gslb vserver from the active/passive setup
#GSLB Domain setup which are with & without EDR
#NOTE:- EDR is importaint parameter as if not enabled then though GSLB VS is down, yet domain keeps and resolving & ip is resolved.

import os
import os.path
data = []
def domainName():
	os.system("cat ns.conf | grep -i domainName | cut -d ' ' -f6 > New_domain.txt")

def prodcob():
	with open ("New_domain.txt",'r') as d_name :
		data=d_name.readlines()
		for domain in data:
			domain=domain.strip('\n')
			prod_vs_value =  (os.popen("cat ns.conf | grep -i "+ domain + " | cut -d ' ' -f4 | head -1" ).read()).strip('\n')
			bckp_vs_value = (os.popen("cat ns.conf | grep -w " + prod_vs_value + " | grep -i 'backupVserver' | cut -d ' ' -f6  | head -1").read()).strip('\n')
			#print (bckp_vs_value)
			#cob_backup = (os.popen("cat ns.conf | grep -i 'set gslb vserver " + bckp_vs_value + "' | grep -i  'backupVserver' " + " |  cut -d ' ' -f6 ").read()).strip('\n')
			#print (cob_backup)
			if (prod_vs_value and bckp_vs_value):
				cob_backup = (os.popen("cat ns.conf | grep -i 'set gslb vserver " + bckp_vs_value + "' | grep -i  'backupVserver' " + " |  cut -d ' ' -f6 ").read()).strip('\n')
				#os.system("echo " +domain + " " +prod_vs_value+ " " + bckp_vs_value +  " " + ">>  all_Prod_cob.txt" )
				if (cob_backup):
					#print ("prod_cob_cob " + domain + " "+ " "+ prod_vs_value+ " " + " " +  bckp_vs_value + " "+cob_backup)
					os.system("echo " +  domain + "  "+ prod_vs_value+ " " + " " +  bckp_vs_value + " "+cob_backup + " >>prod_cob_cob.txt")
				else:
					os.system("echo " +domain + " " +prod_vs_value+ " " + bckp_vs_value +  " " + ">>  all_Prod_cob.txt" )
			else:
				os.system("echo"+ " " + domain + " " + prod_vs_value + "   >> only_prod_gslb.txt"  )
		

#cat ns01.conf | grep -i svsbbo-B177705-Prod | grep -i add | grep -oP '(?<=-EDR )[^ ]*'	
def check_edr(edr_value):
	#print(edr_value)
	#value=(os.popen("cat ns.conf | grep -i 'add gslb vserver " + edr_value + " ' | grep -oP '(?<=-EDR )[^ ]*' | head -1").read()).strip('\n')
	#value1=(os.popen("cat ns.conf | grep -i 'set gslb vserver " + edr_value + " ' | grep -oP '(?<=-EDR )[^ ]*' | head -1").read()).strip('\n')
	value =  (os.popen("cat ns.conf | grep -i " + edr_value + " | grep -i 'set ' | grep -i 'edr' | head -1 ").read()).strip('\n')
	value1 = (os.popen("cat ns.conf | grep -i " + edr_value + " | grep -i 'add ' | grep -i 'edr' | head -1 ").read()).strip('\n')
	
	#string = "ENABLED"
	#print (value + " "+  value1)
	#if (value.lower() == string.lower()) or (value1.lower() == string.lower()):
	if (value or value1):
	
		return 1
	else:
		return 0
	
def edr():
	if os.path.exists("only_prod_gslb.txt"):
		with open ("only_prod_gslb.txt",'r') as d_name :
			data=d_name.readlines()
			for domain in data:
				domain = domain.strip('\n')
				os.system("echo "+ domain + " > only_prod_vs.txt")
				prod_value = (os.popen ("cat only_prod_vs.txt | cut -d ' ' -f2 ").read()).strip('\n')
				domainName = (os.popen (" cat only_prod_vs.txt | cut -d ' ' -f1 ").read()).strip('\n')
				value = check_edr(prod_value)
				if value == 1:
					os.system("echo " + domainName + " >> edr.txt")
				else:
					os.system("echo " + domainName + " >> Non_edr.txt")
	else:
		pass
		
	if os.path.exists("all_Prod_cob.txt"):
		with open ("all_Prod_cob.txt",'r') as d_name :
			data=d_name.readlines()
			for domain in data:
				domain = domain.strip('\n')
				os.system("echo "+ domain + " > only_prod_vs.txt")
				prod_value = (os.popen ("cat only_prod_vs.txt | cut -d ' ' -f2 ").read()).strip('\n')
				cob_value =  (os.popen ("cat only_prod_vs.txt | cut -d ' ' -f3 ").read()).strip('\n')
				domainName = (os.popen (" cat only_prod_vs.txt | cut -d ' ' -f1 ").read()).strip('\n')
				prodValue = check_edr(prod_value)
				cobValue  = check_edr(cob_value)
				if (prodValue == 1) and (cobValue == 1):
					os.system("echo " + domainName + " >> edr.txt")
				else:
					os.system("echo " + domainName + " >> Non_edr.txt")
	else:
		pass

	
def main():
	if os.path.exists("New_domain.txt"):
		pass
	else:
		domainName()
	if os.path.exists("only_prod_gslb.txt") or os.path.exists("all_Prod_cob.txt"):
		pass
	else:
		prodcob()

	if os.path.exists("edr.txt"):
		pass
	else:
		edr()
main()	

