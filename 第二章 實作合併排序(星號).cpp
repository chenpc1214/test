# include<iostream>
#include<cstdlib>
#include<ctime>
#define MAX 10
using namespace std;
void merge(int *,int,int,int); 
void mergesort(int *,int,int);

void print_sth(int *a, int num)   //功能：顯示出陣列所有的數值 
{
	for(num =0; num<MAX;num++)
	{
		cout << a[num] << " ";
	}
	cout << endl;
}

void mergesort(int *a,int L, int R)  //功能：標示出陣列的中位數
{
	int M;                          //宣告常數M 為整數類型 -----  P.S. M 為中位數之簡稱 
	if( L<R)                        //如果  左邊起始點的 '索引'(L)  小於 右邊終點的  '索引'(R) 
	{
		M = (L+R)/2;                // 找出中位數的索引位置 
		mergesort(a,L,M);           // 將陣列一分為二，找出 左半邊中位數索引位置 
		mergesort(a,M+1,R);         // 找出右半邊 中位數索引位置 
		merge(a,L,M,R);             // 最後合併輸出 
		cout << "L = " << L << endl;// 左邊起始點  
		cout << "M = " << M << endl;// 中位數 
		cout << "R = " << R << endl;// 右邊終點 
		print_sth(a,MAX);            
	  }  
 } 
 
 void merge(int *a,int L,int M, int R)  //功能：排序左右兩邊，最後合併輸出 
 {
 	int left,right, i , tmp[MAX];       //宣告整數變數有  left(左起始點)   right(右邊起點)   i(左邊起始點)   tmp[MAX] (暫時存放陣列值的常數) 
 	
 	left = L;                          // 左邊起點
 	right = M+1;                       // 右邊起點
 	i = L;                             // (固定不變的) 左邊起點
 	
 	while((left <= M) && (right <= R)) // 當 左邊起始點索引 小於等於 中位數索引 '且' 右邊起點索引 小於等於 右邊終點成立  |就繼續執行到錯誤為止| 
 	{
 		if(a[left] < a[right])         // 假如陣列a最左邊的 '值' 小於 最右邊的'值' 
 		{
 			tmp[i]=a[left];            //暫存陣列的tmp 會被附值 a陣列中最左邊的值 
 			i++,left++;                //接著 i+1 ， left也+1 
		 }
		else
		{
		 	tmp[i]=a[right];
		 	i++,right++;
		}
	}
	 
	while (left <= M)                   // 當 最左邊的索引 小於等於 中位數成立 |就執行到錯誤為止| 
	{
	 	tmp[i] = a[left];              // 暫存陣列的tmp 會被附值 a陣列中最左邊的值
	 	i++,left++;                    //接著 i+1 ， left也+1  
	}
	 
	while(right <= R)
	{
	 	tmp[i]=a[right];
	 	i++,right++;
	}
	
	for(i = L; i <=R ; i++)          //最後將暫存在tmp的陣列數值，用for迴圈全部寫回a陣列 
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
	cout <<"還未排序前....." << endl;
	print_sth(list,MAX);
	 
	mergesort(list,0,MAX-1);
	cout <<"排序後....." << endl;
	print_sth(list,MAX); 
 }
