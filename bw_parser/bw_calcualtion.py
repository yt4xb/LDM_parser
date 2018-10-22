
"""@package cpu_parser
Copyright (C) 2018 University of Virginia. All rights reserved.

file      bw_calcualtion.py
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

brief     calculate the bw of LDM.
usage     python bw_calculation
"""
from __future__ import division
import sys
import numpy as np
bw_list = []
bw = []
with open('sar.log', 'r') as f:
    for i, lines in enumerate(f):
        for j in lines.split():
            bw_list.append(j)
        bw_list.append('\n')
    #print bw_list
f.close()

with open('bw.csv', 'w+') as w:
    for i in bw_list:
        if(i == '\n'):
            bw = np.array(bw).astype(np.float)
            a= np.sum(bw)
            w.write(str(a) + '\n')
            bw = []
            continue
        else:
            bw.append(i)
w.close()
