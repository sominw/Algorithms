# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 01:04:56 2016

@author: sominwadhwa

Median Maintenance using heapq
"""
import heapq

min_heap = []
max_heap = []
c = 0
r = 0

with open('Median.txt','r') as f:
    for line in f:
        x = int(line.strip())
        if len(max_heap) == 0:
            heapq.heappush(max_heap, x)
        else:
            if x > max_heap[0]:
                heapq.heappush(max_heap, x)
            else:
                if(len(min_heap) == 0):
                    heapq.heappush(min_heap, -x)
                else:
                    if x < -min_heap[0]:
                        heapq.heappush(min_heap, -x)
                    else:
                        heapq.heappush(max_heap, x)
        c += 1
        size_max_heap = 0
        if c%2 == 0:
            size_max_heap = c/2
            while len(max_heap) > size_max_heap:
                heapq.heappush(min_heap, -heapq.heappop(max_heap))
            while len(max_heap) <size_max_heap:
                heapq.heappush(max_heap, -heapq.heappop(min_heap))
            r += -min_heap[0]
        else:
            size_max_heap = c/2 + 1
            while len(max_heap) > size_max_heap:
                heapq.heappush(min_heap, -heapq.heappop(max_heap))
            while len(max_heap) < size_max_heap:
                heapq.heappush(max_heap, -heapq.heappop(min_heap))
            r += max_heap[0]

print (r % 10000)
