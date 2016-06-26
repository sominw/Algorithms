/* Simple implementation of QuickSort with an avg 
	case running time of O(nlog(n))

	Author : sominwadhwa@gmail.com
*/
	
#include <iostream>
using namespace std;
int partition(int A[],int p,int r){
	int x = A[r-1];
	int i = p - 1;
	int temp;
	for (int j=p;j<r-1;j++){
		if (A[j] <= x){
			i = i + 1;
			temp = A[i];
			A[i] = A[j];
			A[j] = temp;

		}
	}
	A[r-1] = A[i+1];
	A[i+1] = x;
	return i+1;
}
void quick_sort(int A[],int p,int r){
	if (p<r){
		int q = partition(A,p,r);
		quick_sort(A,p,q);
		quick_sort(A,q+1,r);
	}
}
int main(void){
	int const n = 100;
	int A[n],size = 0;
	cout << "Enter size of the Array: ";
	cin >> size;
	for(int i=0;i<size;i++){
		cin >> A[i];
	}
	quick_sort(A,0,size);
	cout << endl << "Sorted Array is: "<<endl<<endl;
	for(int i=0;i<size;i++){
		cout << A[i] << endl;
	}
return 0;
}