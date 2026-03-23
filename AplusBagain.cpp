#include<iostream>

using namespace std;

int main(){
    int t;
    while (t--)
    {
        int n, temp, d1;
        int sum = 0;
        cin>>n;
        while(temp>0){
            d1 = temp % 10;
            sum += d1;
            temp = temp/10;
        }
        cout<<sum<<endl;
    }
    
}