//
//  main.cpp
//  Insertion Sort
//
//  Created by Somin Wadhwa on 24/06/16.
//  Copyright © 2016 Somin Wadhwa. All rights reserved.
//
#include <iostream>
using namespace std;
int main(){
    int const n = 50;
    int a[n];
    int x = 0;
    cout << "Enter the number of elements: ";
    cin >> x;
    for (int i = 0;i < x;i++){
        cin >> a[i];
    }
    int key = 0 ;
    int p = 0 ;
    for (int j = 1;j < x;j++){
        key = a[j];
        p = j - 1;
        while (p >= 0 && a[p] > key){
            a[p+1] = a[p];
            p = p-1;
        }
        a[p+1] = key;
        
    }
    cout << endl <<  "Sorted Array is: ";
    for (int i = 0;i < x;i++){
        cout << a[i] << endl;
    }
    
    return 0;
}