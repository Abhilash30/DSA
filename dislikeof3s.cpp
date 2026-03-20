#include<iostream>
#include<vector>
using namespace std;

bool addtolist(int x){
    if (x % 3 == 0) return false;

    if (x % 10 == 3) return false;
    return true;
}

int main(){
    int t;
    cin >> t;

    vector<int> ans;

    while(t--){
        int n;
        cin >> n;

        int count = 0;
        int num = 1;

        while(true){
            if(addtolist(num)){
                count++;
                if(count == n){
                    ans.push_back(num);
                    break;
                }
            }
            num++;   
        }
    }

    for(int i = 0; i < ans.size(); i++){
        cout << ans[i] << endl;
    }
}