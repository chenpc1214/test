#include<iostream>
#include<cstdlib>
#include<cstring>
using namespace std;

void print_sth(int *a,int num)
{
	for(int i=0;i<num;i++)
	{
		cout << a[i] << " ";
	}
	cout << endl;
}

int main(void)
{
	int n,t,now,ans;
	int arr[200],time[200],ser[600];
	
	while(cin>>t)
	{
		cin >> n;
		for(int i=0;i<n;i++)
		{
			cin >> arr[i]>> time[i];
		}
		memset(ser,0,sizeof(ser));
		now = -1;
		ans = 0;
		for(int i=0;i<n;i++)
		{
			if (now>=t*60) break;
			
			if (arr[i]>=now)
			{
				for(int j=arr[i];j<arr[i]+time[i];j++)
				{
					if(j >=t*60)
					{
						ser[j]=1;
					}
				}
				now = arr[i]+time[i];
			}
			else
			{
				for(int j=now;j<now+time[i];j++)
				{
					if(j>=t*60) break;
					ser[j] = 1;
				}
				now = now+time[i];
			}
		}
		for(int i =0;i<t*60;i++)
		{
			if(ser[i]==0)
			{
				ans++;
			}
		}
		cout << ans << endl;
	}
} 
