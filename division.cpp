#include<iostream>

using namespace std;

int main(){
    int t;
    cin>>t;
    while(t--){
        int i;
        cin>>i;
      
        if(i>=1900){
            cout<<"Division 1"<<endl;
     
        }
        else if(1600<=i){
            cout<<"Division 2"<<endl;
      
        }
        else if(1400<=i){
            cout<<"Division 3"<<endl;
            
        }
        else{
            cout<<"Division 4"<<endl;
            
        }

    }

}