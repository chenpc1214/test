#include <iostream>
#include <ctime>
#include <cstdlib>
#define Size 10
using namespace std;
void printA(int *a,int s){
  for(int i=0;i<s;i++){
    cout << a[i] << " ";
  }
  cout << endl;
}
int main() {
  int A[Size],insert;
  srand(time(NULL));
  for (int i=0;i<Size;i++){
    A[i]=rand()%1000+1;
  }
  cout << "排序前" << endl;
  printA(A,Size);
  int j;
  for(int i=1;i<Size;i++){
    insert = A[i];
    for(j=i-1;j>=0;j--){
      if(insert < A[j]) {
        A[j+1]=A[j];
      }else {
        break;    
      }
    }
    A[j+1]=insert;
    cout << "外層迴圈執行" << i <<"次結果為" << endl;
    printA(A,Size);
  }
  cout << "排序後" << endl;
  printA(A,Size); 
}
