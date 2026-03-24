#include<iostream>

using namespace std;

int d(int a){
    int temp = a;
    int d1;
    int sum = 0;
    while (temp>0)
    {
        d1 = temp%10;
        sum += d1;
        temp = temp/10;
    }
    return sum;
    
}

int main(){
    int t;
    
    cin>>t;
    while(t--){
        int x,y;
        int count = 0;
        cin>>x;
    
        for(int y = x+1; y<x+130; y++){
            if(x==y - d(y)){
                count++;
            }
        }
        cout<<count<<endl;
    }
}