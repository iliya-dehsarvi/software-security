#!/usr/bin/env python
import subprocess
import optparse
import re

def get_args():
    parser = optparse.OptionParser()
    parser.add_option('-i', '--interface', dest='interface', help='Interface t0 CHANGE its mac address')
    parser.add_option('-m', '--mac', dest='new_mac', help='new MAC address')
    options, args = parser.parse_args()
    if not options.interface: raise Exception('[-] missing interface argument')
    if not options.new_mac: raise Exception('[-] missing MAC address argument')
    return options, args

def change_mac(interface, new_mac):
    print('[+] Changing interface for ' + interface + ' to ' + new_mac)
    subprocess.call(['ifconfig', interface, 'down'])
    subprocess.call(['ifconfig', interface, 'hw', 'ether', new_mac])
    subprocess.call(['ifconfig', interface, 'up'])

def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(['ifconfig', interface])
    results = re.search(r'\w\w:\w\w:\w\w:\w\w:\w\w:\w\w', ifconfig_result)
    if results: return results.group[0]

def validate(current_mac, new_mac):
    if current_mac != new_mac: return '[+] the MAC, ' + current_mac + ' was changed to ' + new_mac

if __name__ == '__main__': 
    options, _ = get_args()
    current_mac = get_current_mac(options.interface)
    change_mac(options.interface, options.new_mac)
    new_mac = get_current_mac(options.interface)
    validate(current_mac, new_mac)