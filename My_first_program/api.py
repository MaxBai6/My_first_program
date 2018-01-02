# coding=utf-8
from jqdata import *
from pandas.core.frame import DataFrame
import pandas as pd
import numpy as np
import time
import statsmodels.api as sm
import copy
import matplotlib.pyplot as plt
import datetime
from datetime import timedelta
     
def add_one(a):
    """
    Return a + 1.
    """
    return a + 1

#子功能，用于向前或向后推移时间数据
#DATA is a dataframe,it at least have two attributes--"data", "month" ,n is the time of delaying
def N_month_ago(DATA,data_name,month_name,n=0):
    DATA['new_month']=copy.deepcopy(DATA[month_name])

    new_month=[]
    for i in range(0,len(DATA)):
        year=int(str(DATA['new_month'][i])[:4])
        month=int(str(DATA['new_month'][i])[5:7])

        year_new=year
        month_new=(month-n)%12
        Newmonth=month-n
        if Newmonth==0: month_new=12
        if Newmonth>12: year_new=year+1
        if Newmonth<=0: year_new=year-1
        #if Newmonth>24: year_new=year+2
        #if Newmonth>36: year_new=year+3            
        if Newmonth<-12: year_new=year-2
        if Newmonth<-24: year_new=year-3  

        month_new_str="0"+str(month_new)

        date_new=str(year_new)+"-"+month_new_str[-2:]
        new_month.append(date_new)
    new_month={'new_month':new_month}
    new_month=DataFrame(new_month)
    DATA['date_new{0}'.format(n)]=new_month

def r2_table(x1,x2,table1,table2,month_name,data_name1,data_name2):
    Price=table1
    DATA2=table2

    #合并目标价格的表格，计算影响的提前或延后
    month=[]
    corr_all=[]
    r2=[]
    coef=[]
    p=[]

    for n in range(x1,x2):
    #for i in [-2,-7]:
        DATA=copy.deepcopy(DATA2)
        N_month_ago(DATA,data_name2,month_name,n)
        DATA=DATA.drop(['stat_month'], axis=1)
        DATA.rename(columns={'date_new{0}'.format(n):'stat_month'}, inplace=True)
        print(n)
        DATA=DATA.dropna()
        result2 = pd.merge(Price,DATA, on='stat_month')
        result2=result2.dropna()

        #DATA.drop(['stat_month'], axis=1)
        y=result2[data_name1]
        X=result2[data_name2]
        model = sm.OLS(y,X)
        results = model.fit()

        #print(results.summary())

        corr=result2[data_name1].corr(result2[data_name2])

        corr_all.append(corr)
        month.append(n)
        r2.append(results.rsquared)
        p.append(float(results.pvalues))
        #coef.append(results.params[1])
        #sns.pairplot(result2.loc[:,['yield_rate_month_end','retail_sin']], size=5)

    DATA_corr={"month":month,
               "r2":r2,
               "correlation":corr_all,
               'p':p}
    #"coef":coef}
    DATA_corr=DataFrame(DATA_corr) 
    
    return DATA_corr
