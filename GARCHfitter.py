# -*- coding: utf-8 -*-
"""
Created on Sun May 31 15:38:22 2020

@author: gebruiker
"""

def GARCHfitter3001(pair):
    from arch.univariate import arch_model
    import arch
    import pandas as pd
    import numpy as np
    
    # scale the returns with scaling to improve algorithm performance
    scaling = 1000
    
    # determine with pair is being used
    loc = list(pair)
    
    # def rets series
    rets1 = pair[loc[1]]
    rets1 = rets1[1:]*scaling
    
    
    rets2 = pair[loc[2]]
    rets2 = rets2[1:]*scaling
    
    retsP = pair[loc[3]]
    retsP = retsP[1:]*scaling
    
    # get sigma1's 
    am = arch_model(rets1, mean='Zero', vol='GARCH', p=1, o=1, q=1, dist= 'skewt')
    res1 = am.fit(last_obs= rets1.size)
    estimates1 = res1.forecast(horizon=1, start=0)
    vf1 = np.square( (np.sqrt(estimates1.variance) / scaling) )

    # get sigma2's
    am = arch_model(rets2, mean='Zero', vol='GARCH', p=1, o=1, q=1, dist = 'skewt')
    res2 = am.fit(last_obs = rets2.size)
    estimates2 = res2.forecast(horizon=1, start=0)
    vf2 = np.square( (np.sqrt(estimates2.variance) / scaling) )
    
    # get sigmaP's
    am = arch_model(retsP, mean='Zero', vol='GARCH', p=1, o=1, q=1, dist = 'skewt')
    resP = am.fit(last_obs = retsP.size)
    estimatesP = resP.forecast(horizon=1, start=0)
    vfP = np.square( (np.sqrt(estimatesP.variance) / scaling) )
    
    ICInum = (vfP - (0.25*vf1 + 0.25*vf2))
    
    ICIdenom = 2 * (0.5*vf1 + 0.5*vf2)
    
    ICI = ICInum / ICIdenom
    
    # now make a nice lil muhfucking df with retsP and corrs
    
    retcorr = pd.DataFrame()
    
    retcorr['rets'] = retsP/scaling**2
    
    retcorr['corrs'] = ICI['h.1']
    
    retcorr['vol'] = vf1
    
    
    return retcorr



























def CORRtester3000(retcorr):
    import pandas as pd
    
    sort_retcorr = retcorr.sort_values('rets')
    
    SM_rets = retcorr.rets[:round(0.05*len(retcorr['rets']))]
    
    cutoffLow = round(0.05*len(retcorr['rets']))
    
    cutoffMid1 = round(0.475*len(retcorr['rets']))
    cutoffMid2 = round(0.525*len(retcorr['rets']))
    
    cutoffHigh = round(0.95*len(retcorr['rets']))

    
    return