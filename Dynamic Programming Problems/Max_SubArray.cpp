#include <iostream>
#include <cmath>
#include <vector>
#include <algorithm>
#include <functional>
using namespace std;
 
int main(){
    int t; // test case
    int n;
    vector<int> a;
    cin >> t;
 
    while (t--){
        a.clear();
        cin >> n;
        for (int i = 0; i < n; i++){
            int temp;
            cin >> temp;
            a.push_back(temp);
        }
        
        int size = a.size();
 
        int ans1 = a[0];
        int n_sub_sum;
        for (int i = 0; i < size; i++){
            for (int j = i; j < size; j++){
                n_sub_sum = 0;
                for (int k = i; k <= j; k++){
                    n_sub_sum += a[k];
                }
 
                ans1 = max(ans1, n_sub_sum);
            }
        }
        cout << ans1 << " ";
 
        
        sort(a.begin(), a.end(), greater<int>());
 
        int sum = 0;
        for (int i = 0; i < size; i++){
            if (a[i] <= 0 && i >= 1)
                break;
 
            sum += a[i];
        }
        cout << sum << endl;
    }
    return 0;
}
