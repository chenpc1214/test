#include<iostream>
using namespace std;
long long int mutipl(int);

int main(void)
{
	int ans,num;
	
	while(cin >> num)
	{
		ans=mutipl(num);
		cout << "result=" << ans;
	}
	return 0;
}

long long int mutipl(int x)
{
	if (x==0 || x==1)
	{
		return 1;
	}
	else
	{
		return x*mutipl(x-1);
	}
}
