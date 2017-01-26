#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>


int main() {
    unsigned long long t[21];
    int n;
    std :: cin >> t[0] >> t[1] >> n;
    for (int i = 2; i < n; i++){
    	t[i] = t[i-1]^2 + t[i-2];
    }
    std :: cout << t[n-1];

    return 0;
}