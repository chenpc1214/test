# include<iostream>
#include<cstdlib>
#include<ctime>
#define MAX 10
using namespace std;
void merge(int *,int,int,int); 
void mergesort(int *,int,int);

void print_sth(int *a, int num)   //�\��G��ܥX�}�C�Ҧ����ƭ� 
{
	for(num =0; num<MAX;num++)
	{
		cout << a[num] << " ";
	}
	cout << endl;
}

void mergesort(int *a,int L, int R)  //�\��G�ХܥX�}�C�������
{
	int M;                          //�ŧi�`��M ��������� -----  P.S. M ������Ƥ�²�� 
	if( L<R)                        //�p�G  ����_�l�I�� '����'(L)  �p�� �k����I��  '����'(R) 
	{
		M = (L+R)/2;                // ��X����ƪ����ަ�m 
		mergesort(a,L,M);           // �N�}�C�@�����G�A��X ���b�䤤��Ư��ަ�m 
		mergesort(a,M+1,R);         // ��X�k�b�� ����Ư��ަ�m 
		merge(a,L,M,R);             // �̫�X�ֿ�X 
		cout << "L = " << L << endl;// ����_�l�I  
		cout << "M = " << M << endl;// ����� 
		cout << "R = " << R << endl;// �k����I 
		print_sth(a,MAX);            
	  }  
 } 
 
 void merge(int *a,int L,int M, int R)  //�\��G�Ƨǥ��k����A�̫�X�ֿ�X 
 {
 	int left,right, i , tmp[MAX];       //�ŧi����ܼƦ�  left(���_�l�I)   right(�k��_�I)   i(����_�l�I)   tmp[MAX] (�Ȯɦs��}�C�Ȫ��`��) 
 	
 	left = L;                          // ����_�I
 	right = M+1;                       // �k��_�I
 	i = L;                             // (�T�w���ܪ�) ����_�I
 	
 	while((left <= M) && (right <= R)) // �� ����_�l�I���� �p�󵥩� ����Ư��� '�B' �k��_�I���� �p�󵥩� �k����I����  |�N�~��������~����| 
 	{
 		if(a[left] < a[right])         // ���p�}�Ca�̥��䪺 '��' �p�� �̥k�䪺'��' 
 		{
 			tmp[i]=a[left];            //�Ȧs�}�C��tmp �|�Q���� a�}�C���̥��䪺�� 
 			i++,left++;                //���� i+1 �A left�]+1 
		 }
		else
		{
		 	tmp[i]=a[right];
		 	i++,right++;
		}
	}
	 
	while (left <= M)                   // �� �̥��䪺���� �p�󵥩� ����Ʀ��� |�N�������~����| 
	{
	 	tmp[i] = a[left];              // �Ȧs�}�C��tmp �|�Q���� a�}�C���̥��䪺��
	 	i++,left++;                    //���� i+1 �A left�]+1  
	}
	 
	while(right <= R)
	{
	 	tmp[i]=a[right];
	 	i++,right++;
	}
	
	for(i = L; i <=R ; i++)          //�̫�N�Ȧs�btmp���}�C�ƭȡA��for�j������g�^a�}�C 
	{
		a[i] = tmp[i];
	}
 }
 
 int main(void)
 {
 	int list[MAX];
 	srand(time(NULL));
 	for(int i=0; i<MAX ; i++)
 	{
 		list[i] = rand()%1000+1;
	}
	cout <<"�٥��Ƨǫe....." << endl;
	print_sth(list,MAX);
	 
	mergesort(list,0,MAX-1);
	cout <<"�Ƨǫ�....." << endl;
	print_sth(list,MAX); 
 }
