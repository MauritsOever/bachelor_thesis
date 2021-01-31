# -*- coding: utf-8 -*-
"""
Created on Tue May 12 14:37:58 2020

@author: gebruiker
"""

# function to make that portfolios based on number you give it
# make it so it takes nr and df

def defp(nr):
    import os
    import pandas as pd
    import numpy as np
    os.chdir(r"C:\Users\gebruiker\Desktop\VU\Bachelor\Year 3\THESIS\3. data and code files")
    
    df = pd.read_csv(r"df.csv")
    df['Date'] = pd.to_datetime(df['Date'])

# get rid of NaN problems
    df = df.fillna(method='ffill')


# now calculate some log returns, denoted as SU, SA, SE, BU, BA, BE, CO
    df['su'] = np.log(df.stocks_us) - np.log(df.stocks_us.shift(1))
    df['sa'] = np.log(df.stocks_as) - np.log(df.stocks_as.shift(1))
    df['se'] = np.log(df.stocks_eu) - np.log(df.stocks_eu.shift(1))
    df['bu'] = np.log(df.bonds_us) - np.log(df.bonds_us.shift(1))
    df['ba'] = np.log(df.bonds_as) - np.log(df.bonds_as.shift(1))
    df['be'] = np.log(df.bonds_eu) - np.log(df.bonds_eu.shift(1))
    df['co'] = np.log(df.bbcoms) - np.log(df.bbcoms.shift(1))
    
    lop = ["su,sa","su,se","su,bu","su,ba","su,be","su,co","sa,se","sa,bu","sa,ba","sa,be","sa,co","se,bu","se,ba","se,be","se,co","bu,ba","bu,be","be,co","ba,be","ba,co","be,co"]
    pairused = lop[nr-1]
    splitpair = pairused.split(',')
    
    p = pd.DataFrame()
    p['date'] = df.Date
    p[splitpair[0]] = df[splitpair[0]]
    p[splitpair[1]] = df[splitpair[1]]
    p['port'] = 0.5*df[splitpair[0]] + 0.5*df[splitpair[1]]
    return p
