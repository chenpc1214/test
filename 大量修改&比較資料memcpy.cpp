#include<iostream>
#include<cstring>
using namespace std;
struct stu
{
	char name[40];
	int math;
	int en;
};
//�W�z���إߦW��stu�����c�Ƹ�� 

int main(void)
{
	stu a,b;  //�ŧi�ܼ�a,b�����c�Ƹ��stu������ 
	char myname[5]= "John";  // �إߦr���Ŷ���5�ӡA�B�W��myname���ܼƦW�� 
	memcpy(a.name,myname,sizeof(myname)); // �ϥΦr��myname��l�Ƶ��ca��name 
	a.math=99; // �N���ca��math��99 
	a.en = 85; //�N���ca��en��85 
	memcpy(&b,&a,sizeof(a)); //�������c a��b 
	cout << b.name << " " << b.math << " " << b.en << endl;
}
