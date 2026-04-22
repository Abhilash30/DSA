#include<iostream>

using namespace std;

// int gcd(int a, int b){
    // int temp;
    // for(int i = 1; i<a+1; i++){
    //     if(a%i==0 && b%i==0){
    //         temp = i;
    //     }
    // }

//     while(b!=0){
//         int temp = b;
//         b = a%b;
//         a = temp;
//     }
//     return a;    
// }

int main(){
    int t;
    cin>>t;
    while(t--){
        int n;
        //int maxgcd = 0;
        int gcd1 = 0;
        cin>>n;
        // for(int i = 1; i<=n; i++){
        //     for(int j = i+1; j<=n; j++){
        //         gcd1 = max(gcd1, gcd(i,j));
        //     }
        // }

        cout<<n/2<<"\n";
    }
}