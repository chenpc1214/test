#include<iostream>
#include<cstdlib>
#include<algorithm>
#include<ctime>
#define MAX 10
using namespace std;

bool cmp(int i,int j)
{
	return(i>j);
}

bool cmp2(int i,int j)
{
	return(j>i);
}

void print_sth(int*a,int s)
{
	for(int i =0;i<s;i++)
	{
		cout << a[i] << " ";
	}
	cout << endl;
}

int main(void)
{
	int list[MAX];
	srand(time(NULL));
	
	for(int i =0;i < MAX; i++)
	{
		list[i] = rand()%10+1;
	}
	cout << "排序前.." << endl;
	print_sth(list,MAX);
	
	cout << "sorted(begin,last)排序後..." << endl;
	sort(list,list+MAX);
	print_sth(list,MAX);
	
	cout << endl;
	
	for(int j = 0;j<MAX;j++)
	{
		list[j] =  rand()%100+1;
	}
	
	cout << "排序前.." << endl;
	print_sth(list,MAX);
	
	cout << "sorted(begin,last,cmp)排序後..." << endl;
	sort(list,list+MAX,cmp);
	print_sth(list,MAX);
	
	cout << endl;
	
	for(int k = 0;k<MAX;k++)
	{
		list[k] =  rand()%100+1;
	}
	
	cout << "排序前.." << endl;
	print_sth(list,MAX);
	
	cout << "sorted(begin,last,cmp2)排序後..." << endl;
	sort(list,list+MAX,cmp2);
	print_sth(list,MAX);
	 
}
