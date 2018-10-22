#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""@package cpu_parser
Copyright (C) 2018 University of Virginia. All rights reserved.

file      cpu_calculation.py
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

brief     calculate the cpu utilization of LDM.
usage     python cpu_calculation <cpu_info.csv>
"""

from __future__ import division
import sys
import numpy as np
# Open the file
f = open(str(sys.argv[1]), 'r')
lines = f.readlines()
f.close()


cpu = []
file = open (str(sys.argv[2]), 'w')
for l in lines:
    print l
    if(l == '\n'):
        cpu = np.array(cpu).astype(np.float)
        a= np.sum(cpu)
        file.write(str(a))
        file.write('\n')
        cpu = []
        continue
    else:
        cpu.append(l)
file.close()
