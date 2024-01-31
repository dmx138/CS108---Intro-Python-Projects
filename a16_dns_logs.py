# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 20:50:13 2023

@author: bayst
"""

# File: a16_dns_logs.py
# your name: Ding Xin
# your email: dmx@bu.edu
# U63555835
# CS108 A1

from a16_dict_operations import print_dict

def process_dns_logs(dns_filename):
    '''procs a CSV and returns a dict with top-level domains as keys and IPs that requested that host domain as key values'''
    
    file = open(dns_filename, 'r')
    
    result = []
        
    for line in file:
        
        result += line
            
    file.close()
    
    return result
    





if __name__ == '__main__':
    dns_filename = 'dnslogs_sample.csv'
    dns = process_dns_logs(dns_filename)
    print_dict(dns)