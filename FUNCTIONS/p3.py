print("Proplem 1 ")
def my_sinh(x):
               """ 
       This is a function that Calculate sinh of the input float
               """
               from math import exp
               out=(exp(x)-exp(-x))/2;                
               return out ;
print(f"for 0 -->{my_sinh(0)}  for 1 -->{my_sinh(1)}   for 2 --> {my_sinh(2)}")
print("=======================================================")                                        
print("Proplem 2 to be done in later chapters for easier method ")
"""def my_checker_board(n):
   import numpy as np
   m=np.zeros((n,n))
   #i is first matrix index j second matrix index ---- k is index for even n matrix  -----l is index for odd n matrix
   i=0; j=0; k=0; l=0; 
   while(1) :
    while(n%2 != 0):
     if l%2 == 0 : 
         m[i,j]=1; 
     if i < n :
         i=i+1; l=l+1
     if i >= n :
         j=j+1 ; i=0;
     if j ==n :
         break ;
    while(n%2 == 0):
     if k%2 == 0:
         m[i,j]=1; 
     if i < n :
         i=i+1; 
     if i >= n & i%2!=0 :
         j=j+1 ; i=1;
     if i >= n & i%2==0 :
         j=j+1 ; i=0;
     if j ==n :
         break ;   
        
   return m
print(f"M(1) array is --> {my_checker_board(1)}")
print(f"M(2) array is --> {my_checker_board(2)}")
print(f"M(3) array is --> {my_checker_board(3)}")
print(f"M(5) array is --> {my_checker_board(5)}")
print(f"M(4) array is --> {my_checker_board(4)}")
print("=================================================")"""
print("====================================================")
print("proplem 3 ")
def my_triangle(b,h):
   out=0.5*b*h; 
   return out
print(f"area of triangle (1,1)-->{my_triangle(1,1)}  area of triangle (2,1) --> {my_triangle(2,1)}  area of triangle (12,5)--->{my_triangle(12,5)}")
print("================================================")
"""print("proplem 4")
import numpy as np
def my_split_matrix(m):
   rows = len(m);
   columns= len(m[0]);
   c=int((columns+1)/2)
   c2=int((columns-1)/2)
   i=0; #index
   if (columns%2) == 0 :
     m1=np.zeros((columns/2,columns/2))  
     m2=np.zeros((columns/2,columns/2));
   if (columns%2 != 0):
     m1=np.zeros((c,c)) 
     m2=np.zeros((c2,c2));
   m.T; m1.T; m2.T;     
   while(i<columns/2):
     m1[i]=m[i]; m2[-(i+1)]=m[-(i+1)]; i=i+1;
   
   while(i<(Columns+1)/2):
     m1[i]=m[i]; 
   if(i+1 < columns/2):
      m2[-(i+1)]=m[-(i+1)]; 
      i=i+1;
   m1.T; m2.T;
   return m1 , m2
print(f"m1 and m2 ar --> {my_split_matrix(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))}")
print(f"m1 and m2 are --> {my_split_matrix(np.ones((5, 5)))}")"""
print("=================================================");
print("proplem 6")
import numpy as np
def my_n_odds(a):
   l=len(a); #length of array
   i=0; n=0;     # index
   while(i<l):
    if(a[i]%2 !=0) : 
     n=n+1;
    i=i+1;
   return n 
print(f"number of odds is --> {my_n_odds(np.arange(100))}     ---> {my_n_odds(np.arange(2, 100, 2))}")
print("===============================================================")
print("proplem 7")
def my_twos(m,n) :
   x=np.zeros((m,n))
   i=0; j=0; #index
   while(1):
    while(j<n):
     x[i,j]=2
     j=j+1
    i=i+1  
    if(i>m & j==n) :
     break;
    else:
     j=0;
   return x 
print(f"Results is -->{my_twos(5,4)}")    
print("==============================================")
print("proplem 8")
my_f=lambda x,y: x-y   
print(f"Result when  (3,2) ----> {my_f(3,2)}")  
print("==============================================")
print("proplem 9")
add_string=lambda s1,s2: s1+s2
s1 = add_string("Programming", " ")
s2 = add_string("is ", "fun!")
print(f"adding Test case result is ----> {add_string(s1,s2)}")
print("==============================================")

   
   
   
    
  
   
       
   
