#include<iostream>
#include<string>
using namespace std;

int main(){
    int t;
    cin >> t;

    while(t--){
        string c;
        cin >> c;

     

        if(c=="abc"||c=="bac"||c=="acb"||c=="cba"){
            cout<<"YES"<<"\n";

        }else{
            cout<<"NO"<<"\n";
        }

        // bool yes = false;

        // for(int i = 0; i < 3; i++){
        //     for(int j = i; j < 3; j++){
        //         string temp = c;
        //         swap(temp[i], temp[j]);

        //         if(temp == a){
        //             yes = true;
        //         }
        //     }
        // }

        // if(yes){
        //     cout << "YES\n";
        // }else{
        //     cout << "NO\n";
        // }
    }
}