#include<iostream>
#include<vector>
using namespace std;

static int count = 0;

void sortit(int n, vector<int> arr){
    if(arr[0]+1==arr[1]){
            count += 1;
    }
    for(int i = 0; i<n-1; i++){
        if(arr[i]+1 == arr[i+1]){
            count += 1;
        }
    }
}




int main(){
    int t;
    cin>>t;
    while(t--){
        int n;
        cin>>n;
        vector<int> arr(n);
        for(int i = 0; i<n-1; i++){
            cin>>arr[i];
        }
        sortit(n, arr);
        cout<<count<<endl;
    }
}