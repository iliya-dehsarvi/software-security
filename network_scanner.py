#!/usr/bin/env python

import scapy.all as scapy

def scan(IP):
    arp_request = scapy.ARP(pdst=IP)
    broadcast = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')   
    arp_request_broadcast = broadcast/arp_request
    answered, _ = scapy.srp(arp_request_broadcast, timeout=1)
    print(answered.summary())

if __name__ == '__main__': 
    scan('10.20.3.134.1/24')