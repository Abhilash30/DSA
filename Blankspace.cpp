#include<iostream>
#include<vector>
#include<string>
using namespace std;

int main(){
    int t;
    int n;
 
    vector<int> ans(t);
    cin>>t;
    for(int i; i<t; i++){
        cin>>n;
        vector<int> arr(n);
        int count = 0;
        for(int j = 0; j<n; j++){
            if(arr[j] != arr[j+1]){
                count += 1;
            }
        }
        ans[i] = count;
    }
    for(int i; i<t; i++){
        cout<<ans[i]<<endl;
    }
}