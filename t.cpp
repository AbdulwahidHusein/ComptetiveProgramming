#include<iostream>
#include<cmath>
#include<vector>
using namespace std;
const int MAX =  20000000;

vector<bool> SIEVE(int max){
    vector<bool> sieve;
    for (int j=0; j<max; j++){
        sieve[j] = true;
    }
    sieve[0] = false;
    sieve[1] = false;
    for (int i=2; i<sqrt(max)+1; i+=1){
        if (sieve[i]){
            for (int j=i*i; j< max; j+=i){
                sieve[j] = false;
            }
            
        }
}
return sieve;
}


int main(){
    int n;
    int count = 0;
    int index = 0;
    while(cin>>n){
        vector<bool> sieve_array = SIEVE(n);
        while (count<n){
            if (sieve_array[index] && sieve_array[index+2])count++;
            index++;
        }
        cout<<"("<<index-1<<", "<<index+1<<")"<<endl;
        index=0;
        count=0;
    }
}