'''
Algorithms - design and analysis (Stanford), Part I.
Programming Question 2:
1) Task is to compute the total number of comparisons used to sort the given input file by QuickSort.
2) Compute the number of comparisons (as in Problem 1), always using the final element of the given array as the pivot element
3) Compute the number of comparisons (as in Problem 1), using the "median-of-three" pivot rule
@author: Alimbekov Renat
'''

PIVOT_FIRST = 1
PIVOT_FINAL = 2
PIVOT_MEDIAN = 3

comparisons = 0


def swap(ar, i, j):
    t = ar[i]
    ar[i] = ar[j]
    ar[j] = t
    
    
def is_median(ar, i, j, k):
    return (ar[i] < ar[j] and ar[i] > ar[k]) or\
           (ar[i] > ar[j] and ar[i] < ar[k])


def _quickSort(ar, l, r, pivot):
    
    global comparisons
    
    
    if l >= r:
        return
    
    
    p = 0
    if pivot == PIVOT_FIRST:
        p = ar[l]
    elif pivot == PIVOT_FINAL:
        p = ar[r]
        swap(ar, l, r)
    elif pivot == PIVOT_MEDIAN:
        m = l + ((r-l) >> 1)
        if is_median(ar, l, m, r):
            p = ar[l]
        elif is_median(ar, m, l, r):
            p = ar[m]
            swap(ar, l, m)
        else:
            p = ar[r]
            swap(ar, l, r)
            
   
    comparisons += (r-l)
    
    
    i = l+1
    for j in range(l+1, r+1):
        if ar[j] < p:
            swap(ar, i, j)
            i += 1
    swap(ar, l, i-1)
    
   
    _quickSort(ar, l, i-2, pivot)
    _quickSort(ar, i, r, pivot)
    


def quickSort(ar, pivot):
    _quickSort(ar, 0, len(ar)-1, pivot)



def main():
    
    global comparisons
    
     # Test Cases
    input_array = [1,3,5,2,4,6]
    quickSort(input_array, PIVOT_FIRST)
    print(input_array)
    
    # Assignment data
    f = open('QuickSort.txt', 'r')
    lst = []
    
    for line in f.readlines():
        lst.append(int(line))
        
    
    # Task 1
    input_array = lst[:] # make a copy
    comparisons = 0
    quickSort(input_array, PIVOT_FIRST)
    print(comparisons)
    
    # Task 2
    input_array = lst[:] # make a copy
    comparisons = 0
    quickSort(input_array, PIVOT_FINAL)
    print(comparisons)
    
    # Task 3
    input_array = lst[:] # make a copy
    comparisons = 0
    quickSort(input_array, PIVOT_MEDIAN)
    print(comparisons)
    
    
if __name__ == '__main__':
    main()