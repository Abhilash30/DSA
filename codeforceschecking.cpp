#include<iostream>
#include<string>
#include<vector>
using namespace std;

int main(){
    char a;
    int t;
    cin>>t;
    string s = "codeforces";
    vector<string> ans(t);
   
    
    for(int i = 0; i<t;i++){
    cin>>a;
    for(int i = 0;i<s.length(); i++){
        if(a==s[i]){
            ans.push_back("YES");
            break;
        }else{
            ans.push_back("NO");
            break;
        }
    }
    }



}