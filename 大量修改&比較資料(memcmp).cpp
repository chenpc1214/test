#include<iostream>
#include<cstring>
using namespace std;
int main(void)
{
	char a[] = "i love c++";
	char b[] = "i love Java";
	int x;
	x = memcmp(a,b,sizeof(a));
	if(x>0)
	{
		cout << a << "�j��" << b << endl; 
	}
	else if (x<0)
	{
		cout << a << "�p��" << b << endl; 
	}
	else
		cout << a << "����" << b << endl; 
}
