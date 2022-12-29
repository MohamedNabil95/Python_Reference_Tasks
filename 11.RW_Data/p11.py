"""f=open("test.txt","w")
for i in range(5):
   f.write(f"this line is {i} \n")
f.close()
f=open("test.txt","a")
f.write(f"There is another line f")
f.close()
f=open("test.txt","r")
content=f.read()
print(content)
import numpy as np
arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
np.savetxt("arr.txt",arr,fmt="%.2f",header="col1 col2 col3")
import numpy as np
data = np.random.random((100,5))
np.savetxt("test.csv", data, fmt = "%.2f",
delimiter=",", header = "c1, c2, c3, c4, c5")
f=open("test.csv","r")
content=f.read()
print(content)
import h5py
import numpy as np
acc_1 = np.random.random(1000)
station_number_1 = "1"
# unix timestamp
start_time_1 = 1542000276
# time interval for recording
dt_1 = 0.04
location_1 = "Berkeley"
acc_2 = np.random.random(500)
station_number_2 = "2"
start_time_2 = 1542000576
dt_2 = 0.01
location_2 = "Oakland"
hf = h5py.File("station.hdf5", "w")
hf["/acc/1/data"] = acc_1
hf["/acc/1/data"].attrs["dt"] = dt_1
hf["/acc/1/data"].attrs["start_time"] = start_time_1
hf["/acc/1/data"].attrs["location"] = location_1
hf["/acc/2/data"] = acc_2
hf["/acc/2/data"].attrs["dt"] = dt_2
hf["/acc/2/data"].attrs["start_time"] = start_time_2
hf["/acc/2/data"].attrs["location"] = location_2
hf["/gps/1/data"] = np.random.random(100)
hf["/gps/1/data"].attrs["dt"] = 60
hf["/gps/1/data"].attrs["start_time"] = 1542000000
hf["/gps/1/data"].attrs["location"] = "San Francisco"
hf.close()"""
import numpy as np
#proplem 1 
list1=[1,2,3,4,5]
f=open("list.txt","w")
for i in range(0,5):
 f.write(f"this line is {list1[i]} \n")
f.close()
f=open("list.txt","r")
content=f.read()
print(content)
#proplem 2
np.savetxt("list.csv",list1,delimiter=",",fmt="%.2f",header="Header")
f=open("list.csv","r")
content=f.read()
print(content)
#proplem 3
arr=np.array([[1,2,3],[1,2,3]])
np.savetxt("arr.txt",arr,fmt="%.2f",header="c1 c2")
out=np.loadtxt("arr.txt")
print(out)
#proplem 4 
import pickle 
pickle.dump(arr, open("arr.pkl", "wb"))
out=pickle.load(open("arr.pkl", "rb"))
print("===============================================")
print(out)
#proplem 5
import json
my_dict={"A": 0 ,"B": 1 , "C": 2}
json.dump(my_dict, open("dic.json", "w"))
out=json.load(open("dic.json","r"))
print("============================")
print(out)



