# -*- coding: utf-8 -*-
"""
Created on Wed May 13 14:01:01 2020
function to make a matrix full of summary statistics
@author: gebruiker
"""
def readin():
    import os
    import pandas as pd
    import numpy as np
    from scipy import stats
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
    return df


def sumarray(y):
    import numpy as np
    from scipy import stats
    length = len(y)
    y = y[1:length+1]
    list = [length, np.nanmean(y), min(y), max(y), np.std(y), stats.skew(y, nan_policy = 'omit'), stats.kurtosis(y, nan_policy = 'omit')]
    return list



def sumstat(df):
    import pandas as pd
    sumstats = pd.DataFrame(index = ['Obs','Mean','Min','Max','$ \sigma $','Skewness','Kurtosis'])
    #sumstats['Index'] = ['mean','min and max','mean','variance','skewness','kurtosis' ]
    
    # first do price level data: 
    sumstats['US stock price'] = sumarray(df.stocks_us)
    sumstats['Asia stock price'] = sumarray(df.stocks_as)
    sumstats['Euro stock price'] = sumarray(df.stocks_eu)
    sumstats['US bond price'] = sumarray(df.bonds_us)
    sumstats['Asia bond price'] = sumarray(df.bonds_as)
    sumstats['Euro bond price'] = sumarray(df.bonds_eu)
    sumstats['Commodity price'] = sumarray(df.bbcoms)
    
    # then do some rets bruh
    sumstats['US stock returns'] = sumarray(df.su)
    sumstats['Asia stock returns'] = sumarray(df.sa)
    sumstats['Euro stock returns'] = sumarray(df.se)
    sumstats['US bond returns'] = sumarray(df.bu)
    sumstats['Asia bond returns'] = sumarray(df.ba)
    sumstats['Euro bond returns'] = sumarray(df.be)
    sumstats['Commodity returns'] = sumarray(df.co)
    
    return sumstats

def autocorr(df):
    from statsmodels.graphics.tsaplots import plot_acf
    # prices first
    plot_acf(df.stocks_us, lags = 50, title = "US stock price ACF")
    plot_acf(df.stocks_as, lags = 50, title = "AS stock price ACF")
    plot_acf(df.stocks_eu, lags = 50, title = "EU stock price ACF")
    
    plot_acf(df.bonds_us, lags = 50, title = "US bond price ACF")
    plot_acf(df.bonds_as, lags = 50, title = "AS bond price ACF")
    plot_acf(df.bonds_eu, lags = 50, title = "EU bond price ACF")
    
    plot_acf(df.bbcoms, lags = 50, title = "Commodity price ACF")
    
    # now returns
    plot_acf(df.su[1:5013], lags = 50, title = "US stock return ACF", zero = False)
    plot_acf(df.sa[1:5013], lags = 50, title = "AS stock return ACF", zero = False)
    plot_acf(df.se[1:5013], lags = 50, title = "EU stock return ACF", zero = False)
    
    plot_acf(df.bu[1:5013], lags = 50, title = "US bond return ACF", zero = False)
    plot_acf(df.ba[1:5013], lags = 50, title = "AS bond return ACF", zero = False)
    plot_acf(df.be[1:5013], lags = 50, title = "EU bond return ACF", zero = False)
    
    plot_acf(df.co[1:5013], lags = 50, title = "Commodity return ACF", zero = False)