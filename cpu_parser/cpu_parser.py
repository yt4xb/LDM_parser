#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""@package cpu_parser
Copyright (C) 2018 University of Virginia. All rights reserved.

file      cpu_parser.py
author    Yuanlong Tan <yt4xb@virginia.edu>
version   1.0
date      May 1, 2018

LICENSE

This program is free software; you can redistribute it and/or modify it
under the terms of the GNU General Public License as published by the Free
Software Foundation; either version 2 of the License, or（at your option）
any later version.

This program is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for
more details at http://www.gnu.org/copyleft/gpl.html

brief     Parses the cpu with PId.
"""


import re
import sys
targetCPU = []

def parseCPU(line):
    """Parses the input xml file and finds the control plane IP.

    Args:
        line: A line of the raw xml file.

    Returns:
        ip:     The IP address found.
        -1:     Indicates invalid IP or none found.
    """
    #match = re.search(r'hostname=\"(.*)\" port=\"(\d+)\" username=\"yt4xb\"', line)
    match1 = re.search(r'(.*) 21702 ldmd', line)
    match2 = re.search(r'(.*) 21724 ldmd', line)
    match3 = re.search(r'(.*) 21725 mldm_sender', line)

    if match1:
        name1 = match1.group(1)
        #port = match.group(2)
        #return name+":"+port
        return name1
    elif match2:
        name2 = match2.group(1)
        #port = match.group(2)
        #return name+":"+port
        return name2
    elif match3:
        name3 = match3.group(1)
        #port = match.group(2)
        #return name+":"+port
        return name3 + '\n'
    else:
        return -1

def main(response):
    """Reads the XML response and parses the IP addresses.

    Args:
        xmlfile : Filename of the XML response.
    """
    with open(response, 'r') as xmlfile:
        for i, line in enumerate(xmlfile):
            cpu = parseCPU(line)
            if cpu != -1:
                targetCPU.append(cpu)
                print cpu
    xmlfile.close()
    with open("parsed_cpu.log", 'w') as dn:
        for i in targetCPU:
            dn.write(i)
            dn.write('\n')
    dn.close

if __name__ == "__main__":
    main(sys.argv[1])
