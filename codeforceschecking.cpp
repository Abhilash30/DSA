#include<iostream>
#include<string>
#include<vector>
using namespace std;

// int main(){
//     char a;
//     int t;
//     cin>>t;
//     string s = "codeforces";
//     vector<string> ans(t);
   
    
//     for(int i = 0; i<t;i++){
//     cin>>a;
//     for(int i = 0;i<s.length(); i++){
//         if(a==s[i]){
//             ans.push_back("YES"); //push back pushes empty string back and adds text ahead so no can do direct assignment better
//             break; // LOGIC IS WRONG AS ALL CHARACTERS DONT GET COMPARED 
//         }else{
//             ans.push_back("NO");
//             break;
//         }
//     }
//     }

int main(){
    char a;
    int t;
    cin>>t;
    string s = "codeforces";
    vector<string> ans(t);
   
    
    for(int i = 0; i<t;i++){
    cin>>a;
   
    ans[i] = "NO";
    for(int j = 0;j<s.length(); j++){
        if(a==s[j]){
            ans[i] = "YES";
            break;
        }
    }
    }
    
    
    for(int i = 0; i<t; i++){
        cout<<ans[i]<<endl;
    }

} 

//WORKING LOGIC - not fast enough