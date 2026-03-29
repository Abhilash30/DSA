#include<iostream>
#include<vector>
using namespace std;

int main(){
    int t;
    cin >> t;
    
    vector<int> h(t), a(t);
    for(int i = 0; i < t; i++){
        cin >> h[i] >> a[i];
    }
    
    int count = 0;
    for(int i = 0; i < t; i++){        
        for(int j = 0; j < t; j++){    
            if(i == j) continue;
           
            if(h[i] == a[j]){
                count++;
            }
        }
    }
    
    cout << count;
}