
## OPTIMIZATION PROJECT dijktras algorithm

import numpy as np
import time

def problem():
    
    """   
 here 'a' is taken as a starting pont and 'b' 'c' and 'd' are the differrent 
 locations with their weights(distance or units) from each other
 
    """
    diagram = {'a': {'b':7 , 'c':12},
               'b': {'c':3 , 'd':14},
               'c': {'a':12 ,'d':4} }
    
    return diagram


dia = problem()

nearest_destination = []
nearest_destination.append('a')
min_dis1 = 0

tic = time.perf_counter()

for i in dia.keys():
        
    u = list(dia[i].values())
    m = list(dia[i].keys())
    n = len(m)
    
    min_dis = min(u)
    
    for j in range(n):
        
        if min_dis == u[j]:
            
            min_dis1 = min_dis + min_dis1  
            print(f'closet destination from a to {m[j]} and distance is {min_dis1} and then')
            
toc = time.perf_counter()        

print(f'calculation took {1000000*(toc-tic)} micro seconds ')     
        
    
