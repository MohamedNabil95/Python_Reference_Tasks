import numpy as np
import math
from math import floor ,log,ceil
print("Proplem 1 ")
def my_bin_2_dec(b):
   l=len(b) 
   out=0
   for i in range(0,l):
    out=out+b[-(i+1)]*2**i
   return out
b1=[1, 1, 1]
b2=[1, 0, 1, 0, 1, 0, 1]
b3=[1]*25
print(f"OUT 1 --> {my_bin_2_dec(b1)}...{my_bin_2_dec(b2)}....{my_bin_2_dec(b3)}")
print("========================================")
print("proplem 2 ")
def my_dec_2_bin(d):
   b=d #will be used in index
   out=[]
   while (floor(b/2) != 0):
    out.append(b%2)
    b=floor(b/2)
   out.append(b%2)
   out.reverse()
   return out
print(f"23-->{my_dec_2_bin(23)}.......2097----->{my_dec_2_bin(2097)}...34-->{my_dec_2_bin(34)}")
print("=====================================")
print("proplem 3 ")
print(f"same Number---->{ my_bin_2_dec(my_dec_2_bin(12654))}")
print("====================================================")
print("proplem 4 ")
def  my_bin_adder(b1,b2) :
   l1=len(b1)
   l2=len(b2)
   out=[]
   #Making both lists same length i.e appending 0's to shorter list
   if l2 > l1 :
    for i in range (0,l2-l1):
     b1.append(0)
    b1.reverse()
   elif l1 > l2 :
    for i in range (0,l1-l2):
     b2.append(0)
    b2.reverse()
   print(f"b1={b1}")
   print(f"b2={b2}")
   for i in range(0,len(b1)):
    if (b1[-(i+1)]+b2[-(i+1)]) ==2:
     out.append(0)
     if i == len(b1)-1 :
      out.append(1)
     else :
      b1[-(i+2)]+=1
     
    elif (b1[-(i+1)]+b2[-(i+1)])==3:
     out.append(1)
     if i == len(b1)-1 :
      out.append(1)
     else:
      b1[-(i+2)]+=1
    elif (b1[-(i+1)]+b2[-(i+1)]) < 2  :
     out.append((b1[-(i+1)]+b2[-(i+1)]))
      
   out.reverse()
   return out
print(f"{my_bin_adder([1, 1, 1, 1, 1], [1])}")
print(f"second -->{my_bin_adder([1, 1, 1, 1, 1], [1, 0, 1, 0, 1, 0, 0])}")
print("===================================================")
print("proplem 5")
print("Allocating more bits to the fraction results increase in the precesion for low numbers \n I don't think assigning more bits have beniefits on the sign")
print("=============================================================")
print("proplem 6")
def my_ieee_2_dec(ieee):
   m=[] #sub list
   exponent=[] #exponnet list
   list(ieee)
   l=len(ieee)
   fraction=1.0
   j=0    #exp for 2 of fraction
   for i in range(0,l): #Make the sub list with integers
    m.append(int(ieee[i]))
   for i in range(0,l): #do the ieee function calculation
    if i in range(1,12):
      exponent.append(m[i])
      if i ==11:
       expo=my_bin_2_dec(exponent) #exponenet value
    if i in range(12,64):
     j=j-1
     fraction=fraction+m[i]*2**j
     
   sign=(-1)**m[0]  
   out=sign*(2**(expo-1023))*fraction
   #print(sign)
   #print(expo)
   #print(fraction)
   #print(j)
   return out
   
print(my_ieee_2_dec("1100000001001000000000000000000000000000000000000000000000000000"))
print(my_ieee_2_dec("0100000000001011001100110011001100110011001100110011001100110011"))
print("================================================================")
print("Proplem 7")
def my_dec_2_ieee(d):
   out=[]
   test=[]
   fracz=[]
   if d > 0 :
    out.append(0)
    i_p=floor(d)
   else:
    out.append(1)
    i_p=ceil(d)                      # non fraction part of d
   exponent=floor(log(abs(i_p),2))+1023
   expo_list=my_dec_2_bin(exponent)  #exponenet converted to binary stored in list
   print(exponent)
   for i in range(0,11):             #storing non fractional part in out list
    out.append(expo_list[i])
    test.append(expo_list[i])
   
   frac=abs(d-i_p)                    #fractional part
   fac=0.5                           #dividing factor
   if frac !=0 :
    for i in range(0,52):
     out.append(floor(frac/fac))
     fracz.append(floor(frac/fac))
     if floor(frac/fac) ==1:
      frac=frac-fac
     fac=fac/2
   print(exponent)
   print(d)
   print(i_p)
   print(abs(d-i_p))
   print(fracz)
   return out
print(f"{my_dec_2_ieee(-309.14174)}")  
#print(my_ieee_2_dec(my_dec_2_ieee(-309.141740)))
print("there is a mistake in the fraction part Will be back to it later")
