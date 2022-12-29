import numpy as np
import math
import matplotlib.pyplot as plt
print("Proplem 5 First proplem in practical ")
class Point():
    def __init__(self, x, y):
       self.x = x
       self.y = y
    def plott(self):
       plt.plot(self.x,self.y);
       plt.show();
    def calculate_dist(self,x1,y1):
       out=((self.x-x1)**2 +(self.y-y1)**2)**0.5
       print(f"Distance is {out}")
x=range(1,10)
y=range(9,18)
mid=Point(x,y)
print(f"Point (x,y) x-->{mid.x} ...y--->{mid.y} plot-->{mid.plott()}")
print("==============================================")
print("proplem 6")
mid=Point(5,6)
m=mid.calculate_dist(1,2);
print(m)
print("=====================================")
print("Proplem 11")
class Car():
   def __init__(self,brand,color,Type):
      self.brand = brand;
      self.color = color;
      self.Type = Type ;
   def start_car(self):
      print("Car Started")
class Loader(Car):
   def __init__(self,brand,color,Type,size):
      super().__init__(self,brand,color)
      self.brand = brand
      self.color=color
      self.Type= Type
      self.size = size
      
   def Loader_info(self):
      print(f"{self.brand}..{self.color}...{self.Type}...{self.size}")
   def start_Loader(self,key):
      if key == 1:
       print("Loader has started")
      else :
       print("Wrong key ")
   def Loader_break(self,Break):
      if Break == 2:
       print("Loader has stopped")
      else :
       print("Ma3 nafsak ya 7mar !")
class Van(Car):
   def __init__(self,brand,color,Type,size):
      super().__init__(self,brand,color,Type)
      self.size=size
   def start_Van(self,key):
      if key == 1:
       print("Van has started")
      else :
       print("Wrong key ")
   def Van_break(self,Break):
      if Break == 2:
       print("Van has stopped")
      else :
       print("Ma3 nafsak ya 7mar !")
Loader1=Loader("Suzuki","Yellow","Large","Sand Collector")
print(f"Loader 1 -->{Loader1.Loader_info()}")
print("===========================================")
print("Proplem 1")
print("Object is an instance of a class. Class is a blueprint or template from which objects are created.")
print("=================================================================")
print("proplem 2")
print("By using the “self” we can access the attributes and methods of the class in python. It binds the attributes with the given arguments")
print("=====================================================================")
print("proplem 3")
print("Constructors initialize the new object, that is, they set the startup property values for the object. They might also do other things necessary to make the object usable. You can distinguish constructors from other methods of a class because constructors always have the same name as the class")
print("==============================================================================")
print("proplem 4")
print("Class attributes are the variables defined directly in the class that are shared by all objects of the class. Instance attributes are attributes or properties attached to an instance of a class. Instance attributes are defined in the constructor. Defined directly inside a class")
print("Proplem 7")
print("Inheritance allows us to define a class that inherits all the methods and properties from another class")
print("==============================================================")
print("proplem 8")
print("By using class ClassName(superclass) we Enhirit methods to the child class from the Superclass")

      
