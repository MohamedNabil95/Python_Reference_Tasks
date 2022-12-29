#trial 
import multiprocessing as mp
import time
from multiprocessing import pool
from joblib import Parallel, delayed
#print(f"Number of cpu: {mp.cpu_count()}")
print("=================================================")
t0 = time.time()
results=[]
def plus_cube(x, y):
   return (x+y)**3
for x, y in zip(range(100), range(100)):
 results.append(plus_cube(x, y))
t1 = time.time()
print(f"Execution time {t1 - t0} s")
t2=time.time()
n_cpu = mp.cpu_count()
pool = mp.Pool(processes=n_cpu)
results1 = [pool.starmap(plus_cube , zip(range(100), range(100)))]
t3=time.time()
print(f"Execution time {t3 - t2} s")
t4=time.time()
results2 = Parallel(n_jobs=-1)(delayed(plus_cube)(x,y) for x, y in zip(range(100), range(100)))
t5=time.time()
print(f"Execution time {t5 - t4} s")
