import numpy as np
import math
from math import sin
print("Proplem 1 ")
def my_sum(lst):
   l=len(lst)    #Length of list
   SUM=0
   for i in range(0,l):
       SUM+=lst[i]
   return SUM
print(f"Expected 6 -->{my_sum([1, 2, 3])}....expected 5050 -->{my_sum(range(1,101))}")
print("=================================================================================")
print("Proplem 2 ")
def my_chebyshev_poly1(n,x):
   y=[]
   l=len(x)
   z=[]
   if n==0:
    return 1
   if n==1 :
    return x
   else:
    d=my_chebyshev_poly1(n-1,x)
    d2=my_chebyshev_poly1(n-2,x)
    for i in range(0,l) :
     if (type(d) == list and type(d2) == list): y.append(x[i]*2*d[i]-d2[i]) 
     if (type(d) == list and type(d2) == int) : y.append(x[i]*2*d[i]-d2)   
     if (type(d) == int and type(d2) == int)  : y.append(x[i]*2*d-d2)       
    return y
    
x = [1, 2, 3, 4, 5]
print(f"Expected  [1, 1, 1, 1, 1]  --> {my_chebyshev_poly1(0,x)}....expected  [1, 2, 3, 4, 5]-->{my_chebyshev_poly1(1,x)}")
print(f"Expected   [1, 26, 99, 244, 485]  --> {my_chebyshev_poly1(3,x)}")
print("=======================================================================")
print("proplem 3 ")
def my_ackermann(m,n) :
    if m==0 :
     return n+1
    elif (m>0 and n==0):
     return my_ackermann(m-1,1)
    elif (m>0 and n>0):
     return my_ackermann(m-1,my_ackermann(m,n-1))
print(f"Expected 3-->{my_ackermann(1,1)}..expected 4-->{my_ackermann(1,2)}")
print(f"Expected 3-->{my_ackermann(2,3)}..expected 61-->{my_ackermann(3,3)}")
print("============================================")
print("proplem 4 ")
def my_n_choose_k(n,k):
   if n==k:
    return 1
   elif k==1:
    return n
   else:
    return my_n_choose_k(n-1,k)+my_n_choose_k(n-1,k-1)
print(f"expected 10 -->{my_n_choose_k(10,1)}...expected 120 -->{my_n_choose_k(10,3)}")
print("proplem 7")
def my_gcd(a, b):
   if b==0 :
    return a
   elif a==0 :
    return b
   else :
    return my_gcd(b,a%b)
print(f"expected 2-->{my_gcd(10, 4)}...expected 11 -->{my_gcd(33, 121)}...expected 1 -->{my_gcd(18, 1)}")
print("======================================================")
"""print("proplem 8")
out=[]
def my_pascal_row(m):
   if m==1:
    return 1
   else :
   return out.append()"""
"""print("proplem 9")
def my_spiral_ones(n):
   z=np.zeros((n,n))
   if n==1:
    for i in range (0,n)
        z.append(i)
    return z
   if n==2
    for i in range ("""
print("proplem 11")
def my_towers(N, from_tower, to_tower, alt_tower):

   if N != 0:

    my_towers(N-1, from_tower, alt_tower, to_tower)

    print("Move disk %d from tower %d to tower %d."%(N, from_tower, to_tower))

    my_towers(N-1, alt_tower, to_tower, from_tower)
print(f"{my_towers(4,1,3,2)}")
