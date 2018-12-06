import os
data = []
P_name=[]
bck01=[]
with open ("domainName.txt",'r') as d_name :
	data=d_name.readlines()
	#print (data)
	for domainName in data:
		#print(domainName.strip('\n'))
		d_name =  domainName.strip('\n')
		#os.system("cat ns.conf | grep -i "+d_name+" | cut -d ' ' -f4-6 >> Prod_vserver.txt")
		os.system("cat Prod_vserver.txt")
#os.system("cat Prod_vserver.txt | cut -d ' ' -f1 >> Prod_name.txt")
#print ("Prod_Name")
#os.system("cat Prod_name.txt")
with open ("Prod_name.txt",'r') as Ps_name :
	P_name= Ps_name.readlines()
	for prod_serv in P_name:
		p_s=prod_serv.strip('\n')
		#os.system("cat ns.conf | grep -i "+ p_s+ " | grep -i 'backupvserver' | cut -d ' ' -f4-6 >> backup_vserver.txt ")
os.system("cat backup_vserver.txt")

# To check that if cob has any backup
# cat ns.conf | grep -i  svsbbo-B177705-COB | grep -i backupvserver | cut -d ' ' -f4-6
os.system("cat backup_vserver.txt | cut -d ' ' -f3 > bckp.txt")

with open ("bckp.txt",'r') as b:
	bck01 = b.readlines()
	for backup_server  in bck01:
		b_s =  backup_server.strip('\n')
		os.system("cat ns.conf | grep -i " + b_s + " | grep -i 'backupvserver' | cut -d ' ' -f4-6 > dump.txt")
		value = os.system("cat dump.txt | wc -l ")
		if value == 1:
			print ("Backup_Vserver"+ b_s + "has single prod-cob environment")
		else:
			print ("Hmm!! Sorry Man, "+ b_s +"Pls. check this Cob setup manually")






		
