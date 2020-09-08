#include<iostream>
using namespace std;
long long int mutiple(int);
int main(void)
{
	int k;
	long long int j;
	
	cout << "number:";
	
	while(cin>> k)
	{
		j = mutiple(k);
		cout << "result :" << j;
		
		cout << endl;
	}
}

long long int mutiple(int x)
{
	if(x==0||x==1)
	{
		return 1;
	}
	else
	{
		return x*mutiple(x-1);
	}
}


for (int i = 0; i < ListNumber; i++)
{
	tmp = tmp * list[i];
}

cout << tmp;

}
