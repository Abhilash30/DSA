#include<iostream>

using namespace std;

int main(){
    int y;
    int w;
    cin>>y;
    cin>>w;
    if(y>w){
        return y/6;
    }else if (y<w)
    {
        return w/6;
    }else{
        return 1;  
    }
    

}