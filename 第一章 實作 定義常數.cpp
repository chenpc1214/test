#include<iostream> 
#include<cstdlib>
#include<cmath>
#include<iomanip>
#define MAX 100
using namespace std;
int main(void)
{
	int list[MAX];
	const double PI=acos(-1.0);   // �`�N: �ŧiPI��������I�B�I�� �A�B��CMATH���Y�ɤ���ACOS��J -1.0�ƭ�
	for(int i =0;i<MAX;i++)
	{
		list[i]=i;  // �`�N:�N�j�餤��i�ȵ���list�}�C���ҹ������O�����m
		cout << list[i] << " "; 
	 } 
	 cout << endl;
	 cout << setprecision(15)<<PI << endl; //�]�w��X��ǫר�p���I�H�U15�� 
}
