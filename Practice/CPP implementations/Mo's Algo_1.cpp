#include<bits/stdc++.h>
using namespace std;
#define ll long long int
#define loop1 for(i=0;i<n;i++)
#define loop2 for(j=0;j<n;j++)
#define loopi(a,b) for(i=a;i<b;i++)
#define loopj(a,b) for(j=a;j<b;j++)
#define rloopi(a,b) for(i=a;i>b;i--)
#define rloopj(a,b) for(j=a;j>b;j--)
#define test long long int t;cin>>t;while(t--)
#define loopvar(var,a,b) for(var=a;var<b;var++)
#define rloopvar(var,a,b) for(var=a;var>b;var--)
#define mod 1000000007
bool checkPrime(ll n)
{
    if(n<=1){return false;}
    if(n<=3){return true;}
    if(n%2==0 || n%3==0){return false;}
    for(ll i=5;i*i<=n;i=i+6){if(n%i==0 || n%(i+2)==0){return false;}}
    return true;
}
struct Query
{
    int L,R;
};
int blocksize;
bool compare(Query x,Query y)
{
    if(x.L/blocksize!=y.L/blocksize)
        return x.L/blocksize<y.L/blocksize;
    return x.R<y.R;
}
ll i,j;
void printQuerySums(int a[],int n,Query q[],int m)
{
    blocksize=(int)sqrt(n);
    sort(q,q+m,compare);
    int cL=0,cR=0,cS=0;
    loopi(0,m)
    {
        int L=q[i].L,R=q[i].R;
        while(cL<L)
        {
            cS-=a[cL];
            cL++;
        }
        while(cL>L)
        {
            cS+=a[cL-1];
            cL--;
        }
        while(cR<=R)
        {
            cS+=a[cR];
            cR++;
        }
        while(cR>R+1)
        {
            cS-=a[cR-1];
            cR--;
        }
        cout<<"Sum in the range ["<<L<<","<<R<<"] is "<<cS<<endl;
    }

}
void solve()
{
    int a[]={1,1,2,1,3,4,5,2,8};
    int n=sizeof(a)/sizeof(a[0]);
    Query q[]={{0,4},{1,3},{2,4}};
    int m=sizeof(q)/sizeof(q[0]);
    printQuerySums(a,n,q,m);
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();

    /*test
    {
        solve();
    }*/
    //solve();
    /*ll testcase=1;
    test
    {
        cout<<"Case #"<<testcase<<": ";
        solve();
        cout<<endl;

        testcase++;
    }*/
    return 0;
}
