import numpy as np
import math
from math import sin , cos
print("proplem 1")
y= 0
for i in range(1000):
    for j in range(1000):
        if i == j:
            y += 1
print(y)
print("=================================")
print("proplem 2 ")
def my_max(x):
   MAX=-1*math.exp(17)
   for i in x:
       if x[i]>MAX:
           MAX=x[i]
           
   return MAX
print(f"Max expect 18 -->{my_max(range(19))}")
print("===========================================")
print("prolem 3 ")
def my_n_max(x, n):
   m=[]
   for i in range(0,n):
       m.append(max(x))
       x.remove(max(x))
   return m
x = [7, 9, 10, 5, 8, 3, 4, 6, 2, 1]
y = [7, 9, 10, 5, 8, 3, 4, 6, 2, 1,21,24,50,40]   
print(f"Max list numbers is {my_n_max(x,4)}  expect 10 9 8 7")
print(f"Max list numbers is {my_n_max(y,4)}  expect 50 40 24 21")
print("======================================================")
print("proplem 4")
def  my_trig_odd_even(m) :
   r=len(m)
   c=len(m[0])
   q=np.zeros((r,c))
   for i in range(0,r):
       for j in range (0,c):
           if m[i,j]%2 ==0 :
            q[i, j] = sin(m[i, j])
           else :
            q[i, j] = cos(m[i, j]) 
   return q
x=np.array([[150,135],[135,150]])
print(f"Result should be -0.71 -0.99 -0.99 -0.71 --->{my_trig_odd_even(x)}")
print("======================================================================")
print("proplem 5")
def my_mat_mult(P, Q):
   r=len(P)                #rows of first arr
   c=len(Q[0])             #columns of 2nd arr  
   m=np.zeros((r,c))
   s=len(Q)                #rows of first arr
   for i in range(0,r):
       for j in range (0,c):
           for k in range (0,s):
               m[i,j]+=P[i,k]*Q[k,j]
   return m
P= np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
Q = np.array([[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4]])
print(f"Expected  array([[30, 30, 30], [70, 70, 70]]) ..... my result--->{my_mat_mult(P,Q)}")
print("==============================================================")
print("proplem 7")
def my_find(M):
    k=len(M)
    s=[]        #empty list to be used
    for i in range (0,k):
        if M[i]==1:
         s.append(i)
    return s
print(f"Expected out  [0, 2, 3] ... my result is --> {my_find([1, 0, 1, 1, 0])}")
print("==============================================================================")
print("proplem 9")
def my_is_prime(n):
    for i in range (2,n):
        if n%i !=0:
         out="prime"
        elif n%i ==0 :
         out="not prime"
         break
    return out
print(f"4-->{my_is_prime(4)} 71 -->{my_is_prime(71)}...9--->{my_is_prime(9)}...17 {my_is_prime(17)}")
print("========================================================================")
print("proplem 14")
words = ["test", "data", "analyze"]
l=len(words)
out=[words[i].upper() for i in range (0,l)]
print(f"Results is TEST DATA ANALYZ ....My Result -->{out}")
    


       
