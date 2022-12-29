#importing at begin
import numpy as np 
"""from math import abs"""
#starting coding to the porplems
print("proplem 1")
def my_tip_calc(bill, party) :
   if party<6 :
       tips=0.15*party
   elif 6<party<8 :
       tips=0.18*party 
   elif 8 <party<11 :
       tips=0.2*party
   elif party>11 :
       tips=0.25*party
   return tips
print(f"tips for (109.29,3) -->{my_tip_calc(109.29,3)}   for (109.29,7)-->{my_tip_calc(109.29,7)}")
print(f"tips for (109.29,9) -->{my_tip_calc(109.29,9)}   for (109.29,12)-->{my_tip_calc(109.29,12)}")
print("==============================================================")
print("proplem 2 ")
x = np.array([1,2,3,4])
y = np.array([2,3,4,5])
def my_mult_operation(a,b,operation):
   if operation=="plus" :
       out=a+b
   elif operation=="minus" :
       out=a-b
   elif operation=="mult" :
       out=a*b
   elif operation=="div" :
       out=a/b
   elif operation=="pow" :
       out=a**b
   else :
       raise TypeError("Check the string is one of plus , minus ,mult ,div ,pow")
   return out
p="plus"; m="minus"; mu="mult"; d="div"; po="pow";
print(f"plus -->{my_mult_operation(x,y,p)}  Minus -->{my_mult_operation(x,y,m)} mult-->{my_mult_operation(x,y,mu)}")
print(f"div -->{my_mult_operation(x,y,d)}  pow -->{my_mult_operation(x,y,po)}")
print("==========================================")
print("proplem 3")
def my_inside_triangle(x,y) :
   global out1
   if (y-1)/x ==-1 or (x==0 and 0<y<1) or (0<x<1 and y==0) :
       out1="border"
   elif abs(x)>1 or abs(y)>1: 
       out1="outside"
   elif 0<x<1 and 0<y<1:
       out1="inside"
   return out1
print(f"expect border --> {my_inside_triangle(.5,.5)} expected inisde -->{my_inside_triangle(.25,.25)} expected out -->{my_inside_triangle(5,5)}")
print("===========================================")
print("proplem 4")
def my_make_size10(x):
   l=len(x)
   i=0;
   m=np.arange(1,11)
   if l>10:
       while(i<10):
        m[i]=x[i]
        i=i+1
   elif l<10 :
       while(i<l):
        m[i]=x[i]
        i=i+1
       while(i>=l):
        m[i]=0
        i=i+1
        if(i==10) : break     
   return m
print(f"(1,2)-->{my_make_size10(np.arange(1,2))} (1,15) ---> {my_make_size10(np.arange(1,15))}")
print("===========================================================")
print("proplem 8")
def my_n_roots(a,b,c):
   if b**2>4*a*c:
      n_roots=2
   elif b**2<4*a*c:
      n_roots=-2
   else :
      n_roots=1
   r1=(-b+(b**2 - 4*a*c)**0.5)/2*a
   r2=(-b-(b**2 - 4*a*c)**0.5)/2*a
   r=np.array([r1,r2])
   return n_roots,r
print(f"n of roots and roots are -->{my_n_roots(1,0,-9)} ")
print(f"n of roots and roots are -->{my_n_roots(3,4,5)}")
print(f"n of roots and roots are -->{my_n_roots(2,4,2)}")
print("=====================================================")
print("prolem 9")
def my_split_function(f,g,a,b,x):
   if x<=a:
       return f(x)
   elif x>=b:
       return g(x)
   else:
       return 0
print(f"expect 2.713 -->{my_split_function(np.exp,np.sin,2,4,1)}")

   
        
    
       
   
