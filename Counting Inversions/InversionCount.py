# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 22:59:13 2016

@author: sominwadhwa

Counting the number of Inversions
"""
def count_split_inv(left, right):
    merged = []
    i, j = 0, 0
    count = 0 
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
            count += len(left) - i
    while i < len(left):
        merged.append(left[i])
        i += 1
    while j < len(right):
        merged.append(right[j])
        j += 1
    
    return count, merged


def count_inversions(s):
    if len(s) <=1:
        return 0, s

    mid = len(s) // 2
    left = s[:mid]
    right = s[mid:]
    
    count_left, left = count_inversions(left)
    count_right, right = count_inversions(right)
    count_split, merged = count_split_inv(left, right)
    
    return count_left + count_right + count_split , merged    
    
def main():
    inputs = []
    f = open("/Users/sominwadhwa/Desktop/Algorithms/Counting Inversions/IntegerArray.txt", "r")
    
    for line in f.readlines():
        inputs.append(int(line.rstrip("\n")))
    
    f.close()
    
    number_of_inversions = count_inversions(inputs)
    print (number_of_inversions)[0]
    
if __name__ == '__main__':
    main()