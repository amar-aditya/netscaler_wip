 
import os
data = []
def domainName():
	os.system("cat ns.conf | grep -i domainName | cut -d ' ' -f6 > New_domain.txt")

def prodcob():
	with open ("New_domain.txt",'r') as d_name :
		data=d_name.readlines()
		for domain in data:
			domain=domain.strip('\n')
			prod_vs_value =  (os.popen("cat ns.conf | grep -i "+ domain + " | cut -d ' ' -f4").read()).strip('\n')
			bckp_vs_value = (os.popen("cat ns.conf | grep -w " + prod_vs_value + " | grep -i 'backupVserver' | cut -d ' ' -f6 ").read()).strip('\n')
			#print (bckp_vs_value)
			#cob_backup = (os.popen("cat ns.conf | grep -i 'set gslb vserver " + bckp_vs_value + "' | grep -i  'backupVserver' " + " |  cut -d ' ' -f6 ").read()).strip('\n')
			#print (cob_backup)
			if (prod_vs_value and bckp_vs_value):
				cob_backup = (os.popen("cat ns.conf | grep -i 'set gslb vserver " + bckp_vs_value + "' | grep -i  'backupVserver' " + " |  cut -d ' ' -f6 ").read()).strip('\n')
				#os.system("echo " +domain + " " +prod_vs_value+ " " + bckp_vs_value +  " " + ">>  all_Prod_cob.txt" )
				if (cob_backup):
					print ("prod_cob_cob " + domain + " "+ " "+ prod_vs_value+ " " + " " +  bckp_vs_value + " "+cob_backup)
				else:
					os.system("echo " +domain + " " +prod_vs_value+ " " + bckp_vs_value +  " " + ">>  all_Prod_cob.txt" )
			else:
				os.system("echo"+ " " + domain + " " + prod_vs_value + "   >> only_prod_gslb.txt"  )
		
			

	
def main():
	domainName()
	prodcob()

main()	

