#!/usr/bin/python

# take command line argument from user and print it 5 times.

import sys

def print5times(line_to_print):

	for count in range(0,5) :
		print line_to_print


## (sys.argv[1]) - command line input from user 
print5times(sys.argv[1])
