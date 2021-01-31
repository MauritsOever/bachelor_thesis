# -*- coding: utf-8 -*-
"""
Created on Fri May 29 12:46:16 2020

@author: gebruiker

This function fits the GARCH model, and gets the correlations
returns a df with dates, rets_p, and corrs
"""

def CORRtester3000(retcorr):
    import pandas as pd
    import scipy as sc
    import numpy as np
    
    sort_retcorr = retcorr.sort_values('rets')
    
    # get cutoff values
    cutoffLow = round(0.05*len(retcorr['rets']))
    
    cutoffMid1 = round(0.475*len(retcorr['rets']))
    cutoffMid2 = round(0.525*len(retcorr['rets']))
    
    cutoffHigh = round(0.95*len(retcorr['rets']))

    # define vectors of correlations corresponding to rets
    lowret_corrs = sort_retcorr.corrs[:cutoffLow]
    
    midret_corrs = sort_retcorr.corrs[cutoffMid1:cutoffMid2]
    
    highret_corrs = sort_retcorr.corrs[cutoffHigh:]
    
    
    #print averages of corrs, to figure out which ones highest and stuff
    print('Average of lowret corrs:')
    print(np.average(lowret_corrs))

    print('Average of midret corrs:')
    print(np.average(midret_corrs))
    
    print('Average of highret corrs:')
    print(np.average(highret_corrs))
    
    # rank-sum test those sons of bitches
    print('low vs mid')
    print(sc.stats.ranksums(lowret_corrs, midret_corrs))
    
    print('low vs high')
    print(sc.stats.ranksums(lowret_corrs, highret_corrs))
    
    print('mid vs high')
    print(sc.stats.ranksums(midret_corrs, highret_corrs))
    
    return







































