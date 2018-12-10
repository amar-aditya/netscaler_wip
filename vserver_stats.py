# $language = "python"
# $interface = "1.0"

# This script demonstrates how to open a text file and read it line by
# line to a server.

def main():
  crt.Screen.Synchronous = True
	# Note: A IOError exception will be generated if 'input.txt' doesn't exist.
	#
	
  for line in open("C:\\Users\\Aditya\\Desktop\\scripts\\input.txt", "r"):
		# Send the line with an appended CR
    crt.Screen.Send("stat gslb vs "+line.strip('\n')+ " | g -i 'vserver hits' ")
    crt.Screen.Send("\n")
		# Wait for my prompt before sending the next line
		crt.Screen.WaitForString(">")
    crt.Screen.Synchronous = False
main()
