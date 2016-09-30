# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 21:36:24 2016

@author: sominwadhwa

A simple implementation of Kargers' Min Cut Algorithm
"""

import random
import math
import copy

class adjacencyList(object):
    def __init__(self, node, edge):
        self.node = node
        self.edge = edge
    def contract(self, other):
        self.node = self.node + other.node
        self.edge = [i for i in self.edge + other.edge if i not in self.node]
    def __repr__(self):
        return ('Adjacency: Node = %r , Edge = %r'% (self.node, self.edge))

def cut(graph):
    if len(graph) == 2:
        return graph
    else:
        randPick = random.choice(graph)
        mergeNode = random.choice(randPick.edge)
        mergePick = [i for i in graph if mergeNode in i.node]
        randPick.contract(mergePick[0])
        graph.remove(mergePick[0])
        return cut(graph)

def minCut(graph):
    trailNo = int(math.pow(len(graph), 1) * math.log(len(graph)))
    minCross = float('inf')
    for i in range(trailNo):
        trial  = cut(copy.deepcopy(graph))
        cutCross = len(trial[0].edge)
        if cutCross <= minCross:
            minCross = cutCross
            out = trial
    return out, minCross

def main():
    file = open('kargerMinCut.txt')
    data = [[[int(line.split()[0])], [int(i) for i in line.split()[1:]]] for line in file]
    graph = [adjacencyList(i[0], i[1]) for i in data]
    return minCut(graph)

if __name__ == '__main__':
    print (main())
        