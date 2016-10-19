# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 22:49:48 2016

@author: sominwadhwa

2 Sum Problem with million integers
"""
def findTwoSum(dic):
    
       target = 0 #Output
       for t in range(-10000,10001):
           for x in dic:
               y = t - x
               if y in dic and y != x:
                   target = target + 1
                   break
       return target

def main():
    f = open('HashInt.txt')
    lines = f.readlines()
    dic = {(int)(elem) for elem in lines}
    print ("Target values [-10000,10000] are: ", findTwoSum(dic))

if __name__ == '__main__':
    main()
    
