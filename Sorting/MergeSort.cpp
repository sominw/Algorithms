/* Divide & Conquer approach demonstration using Merge Sort */

#include <iostream>
using namespace std;
void merge(int A[],int p,int q,int r){
    int n = q-p+1;
    int m = r-q;
    int L[n],R[m];
    for (int i=0;i<n;i++){
        L[i] = A[p+i];
    }
    for (int i=0;i<m;i++){
        R[i] = A[q+i+1];
    }
    int i=0,j=0;
    int k;
    for (k=p;k<=r;k++){
        if(L[i]<=R[j] && i<n){
            A[k] = L[i];
            i++;
        }
        else {
            A[k] = R[j];
            j++;
        }
    }
    while(i < n) {
        A[k++] = L[i++];
    }
    while(j < m) {
        A[k++] = R[j++];
    }
    
    
}

void merge_sort(int A[],int p,int r){
    int q = 0;
    if (p < r){
        q = (p + r)/2;
        merge_sort(A,p,q);
        merge_sort(A,q+1,r);
        merge(A,p,q,r);
    }
}

int main(void){
    int const n = 100;
    int A[n],size=0;
    cin >> size;
    for (int i = 0; i < size; i++){
        cin >> A[i];
    }
    cout << "Sorted Array Is: "<<endl;
    merge_sort(A,0,size-1);
    for (int i=0; i<size; i++)
        cout << A[i]<<endl;
    return 0;
}