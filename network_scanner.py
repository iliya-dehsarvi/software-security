#!/usr/bin/env python

import scapy.all as scapy

def scan(IP):
    arp_request = scapy.ARP(pdst=IP)
    broadcast = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')   
    arp_request_broadcast = broadcast/arp_request
    answered, _ = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)
    for element in answered: print(element[1].psrc, element[1].hwsrc)

if __name__ == '__main__': 
    scan('172.20.10.1/24')