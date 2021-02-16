#include <bits/stdc++.h>
using namespace std;
int getnumber(string s)
{
    if(s=="12:00 AM")
    return 0;
    if(s[0]=='1' && s[1]=='2' && s[6]=='P')
    {
        return 1200+(((int)(s[3]))*10)+(int)(s[4]);
    }
    
    int ans=0;
    if(s[0]=='1')
    ans=10;
    ans+=(int)(s[1]);
    
    ans*=10;
    ans+=(int)(s[3]);
    ans*=10;
    ans+=(int)(s[4]);
    if(s[6]=='A')
    return ans;
    else
    return ans+1200;
}
int main()
{
	//12:00 AM 11:42 PM
	string s="12:02 AM";
	int num=getnumber(s);
	cout<<num;
	return 0;
}