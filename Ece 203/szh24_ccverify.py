# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""



def sum_digits(n):
   sum = 0
   while n:
       sum, n = sum + n % 10, n // 10
   return sum


CreditN=raw_input("Input a credit card number " )
CredLen=len(CreditN)

Num1=CreditN[CredLen::-2]
Sum1=sum_digits(int(Num1)) 
    
Sum2=0
array=[]
for item in CreditN[0::2]:
    array.append(2*int(item))
    
    
strarray=str(array)    
char="[ ],"
for item in char:
    Num2=strarray.replace(item,"")
    strarray=Num2
    
Sum2=sum_digits(int(Num2))   


ValidationSum=Sum1+Sum2
strVal=str(ValidationSum)

if strVal[-1]=='0':
    print("This Credit Card number is valid")
else:
    print("Sorry this Credit Card Number is not valid")
    
#Sum1=
#rSum=