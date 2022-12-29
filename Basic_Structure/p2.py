print("1. Assign the value 2 to the variable x and the value 3 to the variable y. Clear just the variable x \n Soulution: \n")
x,y = 2 ,3 ;
print("Value of X and y" );
print(x , y )
del x ;
print("list of all variables after clearing x ")
print("Variable   Type    Data/Info \n ----------------------------\ny  int  3")
print("========================================\n")
print("3. Let x = 10 and y=3. Write a line of code that will make each of the following assignments")
x,y = 10,3 ; 
u=x+y ; v=x*y; w=x/y; 
print("u ,v ,w equals \n")
print(u); print(v); print(w);
from math import sin ;
z=sin(x) ; r=8*sin(x); s=5*sin(x*y); p=x**y;
print("values of z ,r ,s ,p are :");
print(z); print(x); print(s); print(p);
print("=============================================")
print(" 5. Assign string 123 to the variable S. Convert the string into a float type and assign the output to the variable N. Verify that S is a string and N is a float using the type function \n Solution:");
s="123";print("s is %s"%(s))
n=float(s); print("n eqial %f"%(n))
print("type of s ");print(type(s));
print("type of n");print(type(n));
print("============================================")
print("Proplem 7 Solution:");
n="engineering";  x="book"; l=len(n); d=len(x);
print("Number of letters in Engineerings and book are %i %i"%(l,d));
print("=====================================================");
print("8. Check if (Python) is in (Python is great!.)")
x="python"; y="python is great!."
print("Results is :");print(x in y);
print("=================================================")
print("Proplem 9")
x="python is great"
print("last word of the string is --->", x[10:])
print("====================================")
print("Proplem 10")
list_a=[1,8,9,15]
print(f"list_a is {list_a}")
list_a.insert(1,2)
print(f"list after insertion is {list_a}")
list_a.append(4)
print(f"List after append is {list_a}")
print("===========================================")
print("proplem 11 ")
list_a.sort(reverse=True)
print(f"list after sorting is -->{list_a}")
print("=====================================")
print("prolem 12 ")
m=list(y)
print(f"String after being Listed is --->{m}")
print("==============================================")
print("proplem 13 ")
tuble_a=["one",1]
print(f"tuble_a is -->{tuble_a}")
print("==============================================")
print("proplem 14 ")
print(f"second element in tuble_a is -->{tuble_a[1]}")
print("==============================================")
print("proplem 15")
print(f"Uniqe elements are --->{set ([2, 3, 2, 3, 1, 2, 5])}")
print("==============================================")
print("proplem 16 to be discussed")
#set_a=[(2, 3, 2)]
#set_b=[(1, 2, 3)]
#print(f"Union has errror !")
#print(f"Intersecion is --> {set_a.intersection(set_b)}  ")
#rint(f"difference is -->{set_a - set_b}")
print("proplem 17")
new_dict=[("A","a"),("B","b"),("C","c")]
print(f"Dictionary is -->{new_dict}")
print("===============================================")
print("proplem 18")
e="B"
print(f"Checking B inside Dictionary -->{e in new_dict}")
print("=====================================================")
print("proplem 19 ,20,22")
import numpy as np
x =np.array( [1, 4, 3, 2, 9, 4] )
y=np.array([2, 3, 4, 1, 2, 3])
u=x+y ; v=x*y; w=x/y;
z=np.sin(x) ; r=8*np.sin(x); s=5*np.sin(x*y); p=x**y;
print("u ,v ,w equals \n")
print(u); print(v); print(w);
print("values of z ,r ,s ,p are :");
print(z); print(x); print(s); print(p);
print("-----------------------------------------------------")
print(f"Array is -->{np.linspace(-10,10,100)}")
print("-----------------------------------------------------")
y=np.array([[(3,2,3)],[(5,2,8)],[(3,5,9)]])
print(f"array is -->{y}")
print(f"Transpose is -->{y.T}")
