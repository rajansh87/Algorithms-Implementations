#include<bits/stdc++.h>
using namespace std;
void ref()
{
    map<int,int>dic;
    dic[1]=5;
    dic[2]=10;
    dic[3]=15;
    dic.erase(2);
    if(dic.find(1)!=dic.end())   //find
        cout<<"Found"<<endl;
    else
        cout<<"NOT Found"<<endl;

    cout<<dic[1]<<" "<<dic[3]<<endl;  //print
    cout<<(dic.begin())->first<<endl;   //min key
    cout<<(dic.rbegin())->first<<endl;    //max key
    for(map<int,int>::iterator i=dic.begin();i!=dic.end();i++)   //loop
        cout<<(i->second);   //i->first is key and i->second is value
    cout<<(dic.upper_bound(1))->first<<endl;    //just greater than the given key
    cout<<(dic.lower_bound(1))->first<<endl;  //just lower then given key
    cout<<dic.size()<<endl;//size

}
int main()
{
    int q;
    cin>>q;
    while(q--)
    {
        int t,v;
        cin>>t>>v;
        if(t==1)
        {
            //add
        }
        else if(t==2)
        {
            //del
        }
        else
        {
            //print

        }


    }

return 0;
}
