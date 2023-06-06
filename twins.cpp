#include<iostream>
#include<cmath>
using namespace std;
const int MAX =  20000000;
bool s[MAX];
int tw[MAX];
void SIEVE(){
    for (int j=0; j<MAX; j++){
        s[j] = true;
    }
    s[0] = false;
    s[1] = false;
    for (int i=2; i<sqrt(MAX)+1; i+=1){
        if (s[i]){
            for (int j=i*i; j< MAX; j+=i){
                s[j] = false;
            }
        }
}
}


int main(){
    int n;
    int p=0;
    SIEVE();
    for (int i=0;i<MAX; i++){
        if (s[i]&&s[i+2]){
            tw[p] = i;
            p+=1;
        }
    }
    while(cin>>n){
        cout<<"("<<tw[n-1]<<", "<<tw[n-1]+2<<")"<<endl;
    }
}