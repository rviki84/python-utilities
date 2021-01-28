#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 23:56:37 2019

@author: Vignesh
"""

import matplotlib.pyplot as plt
import pydicom
from pydicom.data import get_testdata_files

filename = get_testdata_files("CT_small.dcm")[0]
ds = pydicom.dcmread(filename)
plt.imshow(ds.pixel_array, cmap=plt.cm.bone) 
plt.show()
