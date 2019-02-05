# $language = "python"
# $interface = "1.0"

# This script will read the line by line all the gslb vserver & will print the gslb vservers stats.
# This scripts/module needs to be added to securecrt. alongside the script pls. keep the prod_gslb_vs & prod_cob_gslb_vs. One at a time.
# Above sheet can be fetched via running pro_cob_ver2.py - only_prod.txt & all_prod_cob.txt
# before sharing with everyone need to check one - for me


def main():
	crt.Screen.Synchronous = True
	# Exception will happen, so use the source file with the name as input
	#
	for line in open("C:\\Users\\aa51434\\Desktop\\My_python_script\\input.txt"):
		crt.Screen.Send("sh gslb vs" + line.strip('\n') + " | g -i " + line.strip('\n'))
		crt.Screen.Send("\n")
		#wait for the prompt
		crt.Screen.WaitForString(">")
		crt.Screen.Send("stat gslb vs " + line.strip('\n') + " | g -i 'Time since last state change:' ")
		crt.Screen.Send("\n")
		#wait for the prompt
		crt.Screen.WaitForString(">")
	
	crt.Screen.Synchronous = False
main()
