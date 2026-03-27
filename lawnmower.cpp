#include<iostream>
#include<cmath>
using namespace std;

int main(){
    int t;
    cin>>t; 
    while(t--){
        int n, w;
        cin>>n>>w;
        int must_keep = ceil(n/w);
        int answer = n - must_keep;
        cout<<answer<<endl;
    }

}