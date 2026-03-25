#include<iostream>

using namespace std;
int main(){
    int t;
    cin>>t;
    while(t--){
        int n = 3;
        bool yes = false;
        int a[n];
        for(int i = 0; i<n; i++){
            cin>>a[i];
        }

        if(a[0] + a[1] >= 10){
            yes = true;
        }
        if(a[1]+a[2] >= 10){
             yes = true;
        }
        if(a[0] + a[2]>= 10){
                yes = true;
               
        }
        
        if(yes){
            cout<<"YES"<<endl;
        }else{
            cout<<"NO"<<endl;
        }
       
        
    }

}