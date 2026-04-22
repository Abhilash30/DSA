#include<iostream>
#include<vector>
using namespace std;
int main(){
    int t;
    cin>>t;
    while(t--){
    int n;
    cin>>n;
    vector<int> array(n);
    for(int i = 1; i<n; i++){
        if(i%2!=0){
            array[i-1] += i;
        }else{
            array[i-1] += i;
        }

    }

}
}


