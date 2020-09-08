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
//  上述程式碼的主要功能「顯示陣列內容」 

int main(void)
{
	int list[MAX],tmp;  //宣告變數類型為整數的list陣列 ，以及tmp 
	srand(time(NULL));  //初始化電腦開機後的「固定值」(基本上是從1900年1月1日開始取) 
	
	for (int i=0; i<MAX; i++)
	{
		list[MAX] = rand()%1000+1;
	}
	
	// 上述for迴圈目的在於為了list的變數陣列 「填上1~1000隨機數字」
	 
	cout << "排序前的陣列資料:" << endl;
	printA(list,MAX);  //印出還未排序過的陣列資料 
	
	for (int x = MAX-1; x>1; x--)
	{
		for(int y =0 ;y<MAX ; y++)
		{
			if (list[y] > list[y+1]) //如果   前者(list[y])  比  後者(list[y+1])大  
			{
				tmp = list[y];       //呼叫原先做好的箱子變數tmp，將數值最大者放入箱中 
				list[y]=list[y+1];  // 數值較小的數字  佔走  數值較大者的位置  
				list[y+1] = tmp;   // 原先數值小的位置，再從tmp取出，由它取代原先數值較小者 
			}
		}
		cout <<"外層迴圈第"<<MAX-x<<"次的結果為"<< endl;
		printA(list,MAX);
	}
	cout << "排序後" << endl;
	printA(list,MAX); 
}

