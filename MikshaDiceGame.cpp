#include<iostream>
#include<vector>
using namespace std;

int main(){
    int t;
    cin>>t;
    int M_count = 0;
    vector<int> ans(t*2);
    vector<string> ans1(t);
        
    for(int i = 0; i<t; i++){
        cin>>ans[i];
        cin>>ans[i+1];
        if(ans[i]>ans[i+1]){
            M_count += 1;
        }else if(ans[i+1]>ans[i]){
            M_count -= 1;
        }
        if(M_count>0){
            ans1[i] = "Mishka";
        }else if(M_count == 0){
            ans1[i] = "Chris";
        }else{
            ans1[i] = "Friendship is magic!^^";
        }
    }

    for(int i = 0; i<t; i++){
        cout<<ans1[i]<<endl;
    }
}
    
