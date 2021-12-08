#!/usr/bin/env python

import scapy.all as scapy

def scan(IP):
    arp_request = scapy.ARP(pdst=IP)
    broadcast = scapy.Ether('ff:ff:ff:ff:ff:ff')   
    arp_request_broadcast = broadcast/arp_request
    answered, unanswered = scapy.srp(arp_request_broadcast)

if __name__ == '__main__': 
    scan('192.168.89.133.1/24')