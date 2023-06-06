#include<iostream>
#include<cmath>
#include<vector>
using namespace std;
const int MAX =  20000000;
int tw[100000];
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
    int p = 0;
    vector<bool> sieve_array = SIEVE(MAX);
    for (int l=0; l<100010; l++){
        if (sieve_array[l] && sieve_array[l+2]){
            tw[p] = l;
            tw[p+1] = l+2;
            p+=2;
        }
    }
    int n;
    int count = 0;
    int index = 0;
    while(cin>>n){
        cout<<"("<<tw[index-1]<<", "<<tw[index]<<")"<<endl;
        index=0;
        count=0;
    }
}