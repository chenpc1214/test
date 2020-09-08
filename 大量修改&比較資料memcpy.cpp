#include<iostream>
#include<cstring>
using namespace std;
struct stu
{
	char name[40];
	int math;
	int en;
};
//上述先建立名為stu的結構化資料 

int main(void)
{
	stu a,b;  //宣告變數a,b為結構化資料stu的成員 
	char myname[5]= "John";  // 建立字元空間有5個，且名為myname的變數名稱 
	memcpy(a.name,myname,sizeof(myname)); // 使用字串myname初始化結構a的name 
	a.math=99; // 將結構a的math為99 
	a.en = 85; //將結構a的en為85 
	memcpy(&b,&a,sizeof(a)); //拷貝結構 a到b 
	cout << b.name << " " << b.math << " " << b.en << endl;
}
