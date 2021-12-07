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


if __name__ == '__main__': 
    options, _ = get_args()
    change_mac(options.interface, options.new_mac)

    ifconfig_result = subprocess.check_output(['ifconfig', options.interface])
    print(ifconfig_result)

    results = re.search(r'\w\w:\w\w:\w\w:\w\w:\w\w:\w\w', ifconfig_result)
    
    if results: print(results.group[0])