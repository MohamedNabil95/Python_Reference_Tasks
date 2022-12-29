print("Proplem 17 i\n If P is a logical expression, the law of noncontradiction states that P AND (NOT P) is always false. \n Verify this for P true and P false. \n Soulution: ")
print("for p=1 ") ,
print(1 and (not 1)) ,
print("for p=0  ") ,
print(0 and (not 0)) ;
print("===================================== \n ")
print("Let P and Q be logical expressions. De Morgan’s rule states that NOT (P OR Q) = (NOT P) AND (NOT Q) and NOT (P AND Q) = (NOT P) OR (NOT Q). Generate the truth tables for each statement to show that De Morgan’s rule is always true. \n Soultion :")
print(" for NOT (P OR Q) ")
P, Q = 1,1 ; print("for P=1 Q =1 ")
print(not(P or Q)) ,
P, Q = 1,0; print("for P=1 Q=0 ")
print(not(P or Q)) ,
P, Q = 0,1; print ("for P=0 Q=1 ")
print(not(P or Q)),
P, Q = 0,0; print ("for P=0 Q =0")
print(not(P or Q)) ;
print("------------------- \n ")
print("for (NOT P) AND(NOT Q)")
P, Q = 1,1 ; print("for P=1 Q =1 ")
print((not P) and (not Q)) ,
P, Q = 1,0; print("for P=1 Q=0 ")
print((not P) and (not Q)) ,
P, Q = 0,1; print ("for P=0 Q=1 ")
print((not P) and (not Q)),
P, Q = 0,0; print ("for P=0 Q =0")
print((not P) and (not Q))
print("Same Result then two experessions are equal ! ")
print ("----------------------------------- \n ")
print("checking if  NOT (P AND Q) = (NOT P) OR (NOT Q)")
print("for NOT (P AND Q)")
P, Q = 1,1 ; print("for P=1 Q =1 ")
print(not (P and Q)) ,
P, Q = 1,0; print("for P=1 Q=0 ") ,
print(not (P and Q))
P, Q = 0,1; print ("for P=0 Q=1 ")
print(not (P and Q)),
P, Q = 0,0; print ("for P=0 Q =0")
print(not (P and Q))
print("---------------------------------- \n ")
print("for (NOT P) OR (NOT Q)")
P, Q = 1,1 ; print("for P=1 Q =1 ")
print((not P) or (not Q)) ,
P, Q = 1,0; print("for P=1 Q=0 ") ,
print((not P) or (not Q)) 
P, Q = 0,1; print ("for P=0 Q=1 ")
print((not P) or (not Q)) ,
P, Q = 0,0; print ("for P=0 Q =0")
print((not P) or (not Q)) 
print(" Same results .... then two experessions are equal !")
print ("============================================= \n")
print("23. Do the following calculation at the Python command prompt:e2 sinπ/6 + loge(3) cosπ/9 − 53.")
import math 
print("result equal")
print(math.exp(2)*math.sin(math.pi/6)+math.log(3,math.e)*math.cos(math.pi/9)-5**3)
print("================================================\n")
print("24. Do the following logical and comparison operations at the Python command prompt. You may assume that P and Q are logical expressions. For P = 1 and Q = 1, compute NOT(P) AND NOT(Q). For a = 10 and b = 25, compute (a < b) AND (a = b). \n Solution :")
print(" NOT(P) AND NOT(Q)--->"),print(not(1) and not(1));
print("for a and b ------> ") ,print((10<25) and (10==25))
print("====================================== \n ")


