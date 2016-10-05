# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 20:28:21 2016

@author: sominwadhwa

Implementation of Kasraju's SCC in a directed graph using DFS
"""

import sys
import time
import resource #Manage usage of system resources during execution especially STACK
import heapq #Provides an implementation of the heapq algorithm ie: Priority Queue (Min)
from itertools import groupby #Construct and return iterators with common grouping key(s)
from collections import defaultdict

sys.setrecursionlimit(10 ** 6) #Prevent overflow of the C stack and crashing Python

class Track(object):
    #Keeping track of 'current' parameters
    def __init__(self):
        self.current_time = 0;
        self.current_source = 0;
        self.leader = {} #{node: leader,...}
        self.finish_time = {}
        self.explored = set()

def dfs(graph_dict, node, tracker):
    #Serves as the inner loop and explores all possible reachable nodes.
    tracker.explored.add(node)
    tracker.leader[node] = tracker.current_source
    for head in graph_dict[node]:
        if head not in tracker.explored:
            dfs(graph_dict, head, tracker)
    tracker.current_time += 1
    tracker.finish_time[node] = tracker.current_time

def dfs_loop(graph_dict, nodes, tracker):
    #Serves as an outer loop and checks out all SCCs. Current source node changes with every inner loop
    for node in nodes:
        if node not in tracker.explored:
            tracker.current_source = node
            dfs(graph_dict,node,tracker)

def graph_reverse(graph):
    reversed_graph = defaultdict(list)
    for tail, head_list in graph.items():
        for head in head_list:
            reversed_graph[head].append(tail)
    return reversed_graph

def scc(graph):
    out = defaultdict(list)
    track1 = Track()
    track2 = Track()
    nodes = set()
    reversed_graph = graph_reverse(graph)
    for tail, head_list in graph.items():
        nodes |= set(head_list)
        nodes.add(tail)
    nodes = sorted(list(nodes), reverse = True)
    dfs_loop(reversed_graph, nodes, track1)
    sorted_nodes = sorted(track1.finish_time, key = track1.finish_time.get, reverse = True)
    dfs_loop(graph, sorted_nodes, track2)
    for lead, vertex in groupby(sorted(track2.leader, key = track2.leader.get), key = track2.leader.get):
        out[lead] =  list(vertex)
    return out
        


def main():
    start = time.time()
    graph = defaultdict(list)
    with open('SCC2.txt') as ginput:
        for line in ginput:
            x,y =  int(line.split()[0]), int(line.split()[1])
            graph[x].append(y)
    t1 = time.time() - start
    print ("Initialization completed in ",t1," seconds\n\nComputing SCCs...")
    groups = scc(graph)
    t2 = time.time() - start
    print ("\nComputation completed in ",t2," seconds.")
    five_largest_groups = heapq.nlargest(5, groups, key = lambda x: len(groups[x]))
    #The above Return a list with the n largest elements from the dataset defined by iterable. key
    final = []
    for i in range(5):
        try:
            final.append(len(groups[five_largest_groups[i]]))
        except:
            final.append(0)
    return final
    

if __name__ == '__main__':
    print (main())
