#include<iostream>
#include<vector>
using namespace std;

int main(){
    int t;
    cin>>t;
    while(t--){
        int n;
        cin>>n;
        vector<int> a(n);
        bool b1 = false;
        for(int i = 0; i<n; i++){
            cin>>a[i];
        }
        for(int i = 0; i<n; i++){
            if(a[i]==67){
                b1 = true;
            }
        }
        if(b1 == true){
            cout<<"YES"<<endl;
        }else{
            cout<<"NO"<<endl;   
        }
        

    }
}