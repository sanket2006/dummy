#include <bits/stdc++.h>
using namespace std;
int main()
{
	int t;
	cin>>t;
	for(int z=0;z<t;z++)
	{
		int a,b,n,temp;
		cin>>a>>b>>n;
		for(int i=0;i<n;i++)
		{
			temp=a;
            a=b-a;
            b=b+temp;
		}
		cout<<a<<" "<<b<<endl;
	}
}