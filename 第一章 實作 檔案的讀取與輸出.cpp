#include<iostream>
#include<cstdlib>
#include<fstream>
#include<cstring>
using namespace std;
int main(void)
{
	cout << "enter something to file¡G";
	ifstream in ("input.txt");
	ofstream out("output.txt");
	string word;
	while(getline(cin,word))
	{
		cout << word << endl;
	}
}
