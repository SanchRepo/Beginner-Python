# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 17:10:14 2017

@author: Sancheet Hoque
"""





#Function that takes a digit from 0-9 and converts it into a barcode cluster


def printDigit(digit):
    digit=int(digit) #Making sure input is a integer
    
    #Having respective cases for each digit
    if digit == 0:
        code = '!!...'
    elif digit == 1:
        code = '...!!'
    elif digit == 2:
        code = '..!.!'
    elif digit == 3:
        code = '..!!.'
    elif digit == 4:  
        code = '.!..!'
    elif digit == 5:
        code = '.!.!.'
    elif digit == 6: 
        code = '.!!..'
    elif digit == 7:
        code = '!...!'
    elif digit == 8:
        code = '!..!.'
    elif digit == 9:      
        code = '!.!..'
    
    return code

#Function that takes in a zipcode and converts it into a barcode

def printBarCode(zip_code):
    
    #a function for finding the sum of the digits of a number
    def sum_digits(n):
        sum = 0
        while n:
            sum, n = sum + n % 10, n // 10
        return sum
    
    #converting the inputted number into a string for parsing
    strzip=str(zip_code)

    #list initialization
    barcode=[]
    
    #for loop to go through each digit and convert each one ito a barcode cluster using printDigit function
    for item in strzip:
      barcode.append(printDigit(item))#appends to barcode list
    
    #calculates the checkdigit
    checkdig= 10-sum_digits(zip_code)%10
    barcode.append(printDigit(checkdig))
    
    #combines the strings in the list to gether with a space in between
    barcode=' '.join(barcode)
    
    #adds '!' at the beginning and end of the barcode string
    barcode= '!'+barcode+'!'
    
      
      
    return barcode  
f = open('szh24_barcode.txt', 'w')#Creating a file to write to

print>> f, printBarCode(95014)  #example output 

f.close() #closing file
       

    
    