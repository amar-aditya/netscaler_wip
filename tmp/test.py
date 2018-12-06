import os
data = []
new_data = []
with open("test.txt",'r') as test:
	data =  test.readlines()
	for items in data:
		#new_data.extend(data.split())
		d=items.strip('\n')
		prod_vs =   os.system("cut -d ' ' -f2 test.txt")
		domain_vs = os.system("cut -d ' ' -f1 test.txt")
		print(prod_vs)
		print(domain_vs)
		print (d)
print (new_data)
