#!/usr/local/python

from scapy.all import *

# subnet scanner

for lsb in range(1,255) :
	ip = "192.168.163." +str(lsb)
	arpRequest = Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ip, hwdst="ff:ff:ff:ff:ff:ff")
	arpResponse = srp1(arpRequest, timeout=1, verbose=0)
	if arpResponse :
		print "IP: " + arpResponse.psrc + " MAC: " + arpResponse.hwsrc
