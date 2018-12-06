#Will check the  ns.conf & will identify which of the GSLB vserver is without EDR
# Will split in  two text file
#EDR_Enable EDR_Disabled

# Check if the Vserver if prod, prod-cob,prod-cob-cob 
import os
data = []
def domainName():
	os.system("cat ns.conf | grep -i domainName | cut -d ' ' -f6,4 > New_domain.txt")
def prod-cob():
	with open ("New_doamin.txt",'r') as d_name :
		data=d_name.readlines()
		for domain in data:
		domain=domain.strip('\n')
		prod_vs_value =  os.system("cat ns.conf | grep -i "+ domain + " | cut -d ' ' -f4 ")
		bckp_vs_value = os.system("cat ns.conf | grep -i " + prod_vs_value + " | grep -i 'backupVserver' ")
		if not bckp_vs_value:
			os.system("echo" + domain + " has " prod_vs_value + "which is a standalone prod vserver >> only_prod_gslb_vs.txt")
		else:
			if (bckp_vs_value):
				#os.system("echo for" + domain + prod_vs_value + "has" + " following as the backup" + bckp_vs_value + ">> Prod_cob_vs.txt")
				cob_bck_vs_value =  os.system("cat ns.conf | grep -i " + bckp_vs_value)
				if not cob_bck_vs_value:
					os.system("echo for" + domain + prod_vs_value + "has" + " following as the backup" + bckp_vs_value + ">> Prod_cob_vs.txt")
				else:
					os.system("echo" + cob_bck_vs_value + "needs to be check manually >> Prod_cob_cob.txt")
def edr_prod():
# Will open  one by all the files  and determine which of  the vservers are without  EDR values
#domainName
#Prod - Cob EDRValues
	with open("only_prod_gslb_vs.txt",'r') as pr_vs:
	data = pr_vs.readlines()
	for prod_vs in data:
		prod_vs = prod_vs.strip('\n')
		value = os.system("cat ns.conf | grep -i " + prod_vs+ " | grep -i add | grep -oP '(?<=-EDR )[^ ]*' ")
		if not value:
			os.system("echo" )
def edr_prod_cob():

		
def main():
	domainName()
	prod-cob()

main()	

