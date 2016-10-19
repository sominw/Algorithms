# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 01:23:42 2016

@author: sominwadhwa

Median Maintenance Test Code
"""

import heapq

heap_min = []
heap_max = []
y = 0
r = 0

    
def MedianMaintenance_insert(x):
    
    global heap_min, heap_max,y,r
    
 
    if (len(heap_min) == 0):
        heapq.heappush(heap_min, -x)
    else:
        m = -heap_min[0]
        if x > m:
            heapq.heappush(heap_max, x)
            if len(heap_max) > len(heap_min):
                y = heapq.heappop(heap_max)
                heapq.heappush(heap_min, -y)
        else:
            heapq.heappush(heap_min, -x)
            if len(heap_min) - len(heap_max) > 1:
                y = -heapq.heappop(heap_min)
                heapq.heappush(heap_max, y)
   
    r += -heap_min[0]  
    return -heap_min[0],r


        

def main():
    data = []
    with open('Median.txt','r') as f:
        for line in f:
            data.append(int(line.strip())) 
    medians = []
    
    for x in data:
        median, r = MedianMaintenance_insert(x)
        medians.append(median)
    print (r % 10000)


if __name__ == '__main__':
    main()