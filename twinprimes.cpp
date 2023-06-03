#include <algorithm>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <deque>
#include <fstream>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <vector>
#define max 20000000

using namespace std;

long long int prime[max],thprime[max];

void GenPrime()
{
    long long int i,j,m,k=0,t;
    m=(long long int)sqrt(max);
    memset(prime, 1, sizeof(prime));
    memset(thprime, 0, sizeof(thprime));
    prime[0]=prime[1]=0;
    for(i=2;i<=m;i++)
    {
        if(prime[i])
        {
            if(prime[i+2])
                thprime[k++]=i;
            for(j=i+i;j<max;j+=i)
                prime[j]=0;
        }

    }
    t=max/13;
    t*=12;
    for(i=m+1;i<=t;i++)
    {
        if(prime[i] && prime[i+2] )
            thprime[k++]=i;
    }
}
int main()
{
    long long int n;
    GenPrime();
    //freopen("in.txt","r",stdin);
    while(scanf("%lld",&n)==1)
    {
        printf("(%lld, %lld)\n",thprime[n],thprime[n]+2);
    }
    return 0;
}