#include<iostream>
#include<cstdlib>
#include<sstream>
#include<cstring> 
#include<cctype>
using namespace std;
int main(void)
{
	string ch,tmp;                                                             //　宣告變數ｃｈ　和　ｔｍｐ　為字串類別 
	cout << "please enter a string for transformation:";　　　　　　　　　　　　　　　　　　　　 
	getline(cin,ch);　　　　　　　　　　　　　　　　　　　　　　　　　　　　　// 使用ｇｅｔｌｉｎｅ　方法吸收多餘的空白符號（在這不能用ｃｉｎ方法）　 
	
	cout << endl;　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　//  輸入空行 
	
	for (int i = 0 ; i<= ch.length() ; i++)　　　　　　　　　　　　　　　　　// 利用ｆｏｒ迴圈檢視，字串物件ｃｈ，並呼叫 length方法，制定最高迴圈次數 
	{
		if(isalpha(ch[i]))　　　　　　　　　　　　　　　　　　　　　　　　　// 調用在ｃｃｔｙｐｅ　 中的ｉｓａｌｐｈａ方法，進行判斷依據 
		{
			ch[i] = tolower(ch[i]);　　　　　　　　　　　　　　　　　　　　// 判斷為Ｔｒｕｅ　轉換為英文小寫 
		}
		else
		{
			ch[i] =  ' ';　　　　　　　　　　　　　　　　　　　　　　　　 //斷為Ｆａｌｓｅ　以空白取代 
		}
	}
	stringstream ss(ch);　　　　　　　　　　　　　　　　　　　　　　　　 // 宣告 ｓｓ　為 ｓｔｒｉｎｇｓｔｒｅａｍ 物件，並以物件ｃｈ進行初始化 
	while(ss >> tmp)                                                    //　將ｓｓ物件輸入ｔｍｐ，接著會以空白字元（ｔｍｐ），為ｃｈ字串進行切割 
	{
		cout << tmp << endl;                                           //最後輸出結果 
	}
}
