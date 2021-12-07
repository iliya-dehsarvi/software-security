#!/usr/bin/env python
import subprocess
subprocess.call('ifconfig', shell=True)
subprocess.call('ifconfig eth0 down', shell=True)
subprocess.call('ifconfig hw eth0 ether 00:11:22:33:44:66', shell=True)
subprocess.call('ifconfig up', shell=True)
