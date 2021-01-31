# -*- coding: utf-8 -*-
"""
Created on Mon May 11 13:22:56 2020
delet swerwords wehneber showin code :DDDDDDD

@author: M0_R1ch
"""

#lets get us some nice big PACKAGES to work with ( ͡° ͜ʖ ͡°)
import os
os.chdir(r"C:\Users\gebruiker\Desktop\VU\Bachelor\Year 3\THESIS\3. data and code files")
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from arch.univariate import arch_model
import arch
import scipy as sc

from defps import defp
from summstats import sumstat
from summstats import sumarray
from summstats import readin
from summstats import autocorr
from GARCHfitter import GARCHfitter3001
from CORRtester import CORRtester3000

#df = readin()

# get summary statistics using highly advanced custom-made function
#summs = sumstat(df)
#summs = summs.transpose()

#print(summs.to_latex(index= True))

p = defp(21)

retcorr = GARCHfitter3001(p)

retcorr.to_excel("retcorr.xlsx")
#CORRtester3000(retcorr)