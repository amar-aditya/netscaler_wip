import os

os.system("ls")
os.system("cat ns.conf | grep -i 'domainName' | cut -d ' ' -f6,4 > domain.txt ")
