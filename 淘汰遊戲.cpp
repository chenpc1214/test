#include<iostream>
#include<cstring>
#define MAX 101
using namespace std;

print_sth(bool *a , int num)
{
	for (int i=0;i<num;i++)
	{
		cout << a[i] << " " ;
	}
	cout << endl;
}

int main(void)
{
	bool a[MAX];
	int n,p,leave,c,i;
	string x;
	
	while(cin>>x){
		cout << "請輸入人數:" ;cin >> n;
	    cout << "請輸入淘汰間格:";cin >>p;
		leave = 0;
		i=2;
		memset(a,0,sizeof(a));
		while(leave<(n-1)){
			c=0;
			while(c<p){
				if (a[i]==0){
					c++;
					if (i<n) i++;
					else i=1;
				}else{
					if (i<n) i++;
					else i =1;
				}
			}
			while(a[i]==1){
				if(i<n) i++;
				else i=1;
			}
			a[i]=1;
			leave++;
		}
		for(int j=1;j<=n;j++){
			if(a[j]==0){
				cout << "索引位置=" <<  j << endl;
		print_sth(a,n);
				break;
			}
		}
	}
		
}
