#include<iostream>
#include<cstdlib>
#include<ctime>
#define MAX 10
using namespace std;

void printA(int *a,int s)
{
	for (int i=0;i<s;i++)
	{
		cout << a[i] << " ";
	}
	cout << endl;
}
//  �W�z�{���X���D�n�\��u��ܰ}�C���e�v 

int main(void)
{
	int list[MAX],tmp;  //�ŧi�ܼ���������ƪ�list�}�C �A�H��tmp 
	srand(time(NULL));  //��l�ƹq���}���᪺�u�T�w�ȡv(�򥻤W�O�q1900�~1��1��}�l��) 
	
	for (int i=0; i<MAX; i++)
	{
		list[MAX] = rand()%1000+1;
	}
	
	// �W�zfor�j��ت��b�󬰤Flist���ܼư}�C �u��W1~1000�H���Ʀr�v
	 
	cout << "�Ƨǫe���}�C���:" << endl;
	printA(list,MAX);  //�L�X�٥��ƧǹL���}�C��� 
	
	for (int x = MAX-1; x>1; x--)
	{
		for(int y =0 ;y<MAX ; y++)
		{
			if (list[y] > list[y+1]) //�p�G   �e��(list[y])  ��  ���(list[y+1])�j  
			{
				tmp = list[y];       //�I�s������n���c�l�ܼ�tmp�A�N�ƭȳ̤j�̩�J�c�� 
				list[y]=list[y+1];  // �ƭȸ��p���Ʀr  ����  �ƭȸ��j�̪���m  
				list[y+1] = tmp;   // ����ƭȤp����m�A�A�qtmp���X�A�ѥ����N����ƭȸ��p�� 
			}
		}
		cout <<"�~�h�j���"<<MAX-x<<"�������G��"<< endl;
		printA(list,MAX);
	}
	cout << "�Ƨǫ�" << endl;
	printA(list,MAX); 
}

