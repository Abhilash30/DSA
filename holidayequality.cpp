#include<iostream>
#include<algorithm>
using namespace std;

int main(){
   
        int n;
        cin>>n;
        int a[n];
        for(int i = 0; i<n; i++){
            cin>>a[i];
        }
        auto max = max_element(a, a+n);
        int sum = 0;
        for(int i = 0; i<n; i++){
            if(a[i]<*max){
                sum += *max - a[i];
            }
        }
        cout<<sum<<"\n";
    
}