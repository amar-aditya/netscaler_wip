#!/usr/bin/ python2.6
import os
file_1 = raw_input("Pls. enter the first file ")
file_2 = raw_input(" Pls. enter the second file ")
with open (file_1,"r") as diff:
	diff=diff.readlines()
	for item in diff:
		item = item.strip("\n")
		if item in open (file_2).read():
			os.system("echo " + item + " >> common_domain.txt")
		else:
			os.system("echo " + item + " >> Not_present.txt")
