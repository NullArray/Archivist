#!/usr/bin/env python
#
# Subject to improvements.
#

import sys, os
import binascii

target = raw_input("Provide the path to a windows binary: ")

try:
	binFile = open(target, 'rb')
	binaryData = binFile.read(8)
except Exception as e:
	print "[!]Problem reading binary data\n"
	sys.exit(e)

while True:
	print "Please enter your choice below\n"
	choice = raw_input("[1]Print result\n [2]Write to file\n [3]Both\n")

	if choice == '1':
		print binascii.hexlify(binaryData)
		break
	elif choice == '2':
		outfile = open('hex-rep.txt', 'wb')
		outfile.write(binascii.hexlify(binaryData))
		outfile.close()

		os.system('clear')
		print "[+]Saved to hex-rep.txt in " + os.getcwd() + "\n\n"
		break

	elif choice == '3':
		print binascii.hexlify(binaryData) + "\n\n"
		os.system("sleep 2")

		outfile = open('hex-rep.txt', 'wb')
		outfile.write(binascii.hexlify(binaryData))
		outfile.close()

		print "[+]Saved to hex-rep.txt in " + os.getcwd() + "\n\n"
		break

	else:
		print "[!]Unhandled Option"
