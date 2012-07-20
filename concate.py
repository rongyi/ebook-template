#!/usr/bin/python

import re
import sys
OUTPUT_FILE = "concated.txt" #use as default no much parameter for method

def concatLastWord(inputFileName):
	"""delete the last - in one line and concat the word
	for example there are two lines copied from pdf file like:
	grand-
	mother
	with this function process, the resul will be a single line 
	with a word grandmother
	@fileName the file to be processed"""
	needConcatFlag = re.compile(r".*-$")
	inputFile = file(inputFileName, "rb")
	finalRet = "" # result to be writtern
	for line in inputFile:
		if needConcatFlag.match(line):
			line = line.rstrip("\n-")
		finalRet += line

	outputFile = file(OUTPUT_FILE, "wb")
	outputFile.write(finalRet)
	outputFile.close()

argv_len = len(sys.argv)
if argv_len != 2:
	print("please give the input file name")
	exit(-1)
else:
	concatLastWord(sys.argv[1])
