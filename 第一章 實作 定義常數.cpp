#include<iostream> 
#include<cstdlib>
#include<cmath>
#include<iomanip>
#define MAX 100
using namespace std;
int main(void)
{
	int list[MAX];
	const double PI=acos(-1.0);   // 注意: 宣告PI為倍精度點浮點數 ，且用CMATH標頭檔中的ACOS輸入 -1.0數值
	for(int i =0;i<MAX;i++)
	{
		list[i]=i;  // 注意:將迴圈中的i值給予list陣列中所對應的記憶體位置
		cout << list[i] << " "; 
	 } 
	 cout << endl;
	 cout << setprecision(15)<<PI << endl; //設定輸出精準度到小數點以下15位 
}
