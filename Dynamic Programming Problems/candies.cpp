#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    vector<int> r;
    vector<int> c;
    int total = 0;
    long long n,x;
    cin >> n;
    for (long i = 0; i < n; i++){
    		cin >> x;
    		r.push_back(x);
    }
    for (long i = 0; i < n; i++){
    	c.push_back(1);
    	if (i > 0){
    		if(r[i] > r[i-1])
    			c[i] = c[i-1] + 1;
    		else{
    			long j = i;
    			while(j > 0 && r[j-1] > r[j]){
    				c[j-1] = max(c[j-1],c[j]+1);
    				j--;
    			}
    		}
    	}
    }
    for (long i = 0; i < n; i++){
    	total = total + c[i];
    }
    cout << total;
    return 0;
}
