#!/usr/bin/env python
import scapy.all as scapy

packet = scapy.ARP(op=2, pdst='192.168.89.134', hwdst='00-0C-29-4F-CF-16', psrc='192.168.89.2')