#!/usr/bin/env python

import scapy.all as scapy

def scan(IP):
    arp_request = scapy.ARP(pdst=IP)
    broadcast = scapy.Ether('ff:ff:ff:ff:ff:ff')   
    arp_request_broadcast = broadcast/arp_request
    arp_request_broadcast.show()

if __name__ == '__main__': 
    scan('192.168.89.133')