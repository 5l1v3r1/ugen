#!/usr/bin/env python
import sys
import os.path
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--input', '-i', help='Input file', type=str, required=True)
parser.add_argument('--output', '-o', help='Output file', type=str, required=True)
parser.add_argument('--numbers', '-n', help='Add\'s numbers 1-5 to the end of each username (increases the size of output)', action='store_true')

args = parser.parse_args()

#First lets do a check to see if the input file exists
if not os.path.exists(args.input): 
    print("{} not found".format(args.input))
    sys.exit(0)

#If it exists then we will open and will store content in "names"
f = open(args.input)
names = f.read().splitlines()
f.close()

#Now we check to see if the output file exists and if not create or append to it
path = os.path.join(os.getcwd(), args.output)
f = open(path, 'w+')

#Now we will loop through each of the names from the input files
for name in names:
	#Split the names by the comma between firstname and lastname
	parts = name.split(",")

	#Set fname = firstname and lname = lastname
	fname = parts[0].lower().strip()
	lname = parts[-1].lower().strip()

	#Write different variations back to the output file
	f.write(fname + "\n")                      #joe
	f.write(lname + "\n")                      #bloggs
	f.write(fname + lname + "\n")              #joebloggs
	f.write(lname + fname + "\n")              #bloggsjoe
	f.write(fname + "." + lname + "\n")        #joe.bloggs
	f.write(lname + "." + fname + "\n")        #bloggs.joe
	f.write(fname[0] + lname + "\n")           #jbloggs
	f.write(lname[0] + fname + "\n")           #bjoe
	f.write(fname[0] + "." + lname + "\n")     #j.bloggs
	f.write(lname[0] + "." + fname + "\n")     #b.joe
	f.write(lname + fname[0] + "\n")           #bloggsj
	f.write(fname[0] + "-" + lname + "\n")     #j-bloggs
	f.write(lname[0] + "-" + fname + "\n")     #b-joe
	f.write(fname + "-" + lname + "\n")        #joe.bloggs
	f.write(lname + "-" + fname + "\n")        #bloggs.joe
    
	#If we choose to have numbers then loop through and add 1-5 onto each of the username formats	
	if args.numbers is True:
		for x in range(1,6):
		  f.write(fname + str(x) + "\n")                      #joe1
			f.write(lname + str(x) + "\n")                      #bloggs1
			f.write(fname + lname + str(x) + "\n")              #joebloggs1
			f.write(lname + fname + str(x) + "\n")              #bloggsjoe1
			f.write(fname + "." + lname + str(x) + "\n")        #joe.bloggs1
			f.write(lname + "." + fname + str(x) + "\n")        #bloggs.joe1
			f.write(fname[0] + lname + str(x) + "\n")           #jbloggs1
			f.write(lname[0] + fname + str(x) + "\n")           #bjoe1
			f.write(fname[0] + "." + lname + str(x) + "\n")     #j.bloggs1
			f.write(lname[0] + "." + fname + str(x) + "\n")     #b.joe1
			f.write(lname + fname[0] + str(x) + "\n")           #bloggsj1
			f.write(fname[0] + "-" + lname + str(x) + "\n")     #j-bloggs1
			f.write(lname[0] + "-" + fname + str(x) + "\n")     #b-joe1
			f.write(fname + "-" + lname + str(x) + "\n")        #joe.bloggs1
			f.write(lname + "-" + fname + str(x) + "\n")        #bloggs.joe1
     
f.close()

print('Output file: ' + args.output)
