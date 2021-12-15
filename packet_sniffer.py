#!/usr/bin/env python

import scapy.all as scapy
from scapy.layers import http

def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=lambda x: x.summary())

def process_sniffed_packet(packet):
    if packet.hasLayer(http.HTTPRequest):
        print(packet.show())

sniff('eth0')