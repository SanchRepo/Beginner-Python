# -*- coding: utf-8 -*-
"""
Created on Sun Aug 27 11:32:38 2017

@author: Sancheet Hoque
"""

import math




def linearfit(x,y,gtype):
    yfit=[]
    if gtype =='Linear':
        n=len(x)
        msum=0
        xsum=math.fsum(x)
        ysum=math.fsum(y)
        sqsum=0
        for i in range(n): 
            sqsum+=x[i]**2
            msum+=x[i]*y[i]
            
        a1=(n*msum-(xsum*ysum))/(n*sqsum-xsum**2)
        a0=ysum/n-a1*(xsum/n)
        
        for i in range(n):
            yfit.append(a0+a1*x[i])
        return a1,a0,yfit
        
    elif gtype =='Exponential':

        sqsum=0
        msum=0
        lymean=0

        n=len(x)
        xsum=math.fsum(x)
        ysum=math.fsum(y)                
        for i in range(n): 
            sqsum+=x[i]**2
            msum+=x[i]*math.log(y[i])
            lymean+=math.log(y[i])
            
        Sxx=sqsum/n-(xsum/n)**2
#        Sxx=sqsum/n
        Sxy=(msum/n)-((xsum/n)*(lymean/n))
        b1=Sxy/Sxx
        a1=math.exp((lymean/n)-(b1*(xsum/n)))
        
        for i in range(len(x)):
            yfit.append(a1*math.exp(b1*x[i]))        
        
        return a1,b1,yfit

    elif gtype =='Power':
        sqsum=0
        msum=0
        lymean=0
        lx=0
        xn=[]
        yn=[]
        for i in range (len(x)) :
            if x[i]>0 and y[i]>0:
                xn.append(x[i])
                yn.append(y[i])
        x=xn
        y=yn        
        n=len(x)
        xsum=math.fsum(x)
        ysum=math.fsum(y)                
        for i in range(n): 
            sqsum+=math.log(x[i])**2
            lx+=math.log(x[i])
            msum+=math.log(x[i])*math.log(y[i])
            lymean+=math.log(y[i])
            
        Sxx=sqsum/n-(lx/n)**2
#        Sxx=sqsum/n
        Sxy=(msum/n)-((lx/n)*(lymean/n))
        b1=Sxy/Sxx
        a1=math.exp((lymean/n)-(b1*(xsum/n)))
        
        for i in range(len(x)):
            yfit.append(a1*x[i]**b1) 
        return x,y,yfit
    elif gtype =='Saturation':

        sqsum=0
        msum=0
        lymean=0

        n=len(x)
        xsum=math.fsum(x)
        ysum=math.fsum(y)                
        for i in range(n): 
            sqsum+=x[i]**2
            msum+=x[i]*math.log(y[i])
            lymean+=math.log(y[i])
            
        Sxx=sqsum/n-(xsum/n)**2
#        Sxx=sqsum/n
        Sxy=(msum/n)-((xsum/n)*(lymean/n))
        b1=Sxy/Sxx
        a1=math.exp((lymean/n)-(b1*(xsum/n)))
        
        for i in range(len(x)):
            yfit.append(a1*math.exp(b1*x[i]))    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
         