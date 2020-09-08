#include <iostream>
#include <algorithm>
#include <ctime>
#include <cstdlib>
#define Size 40
using namespace std;
typedef struct _node{
  int chi;
  int eng;
  int math;        
}Node;
bool cmp(Node a,Node b){
  if ((a.chi==b.chi)&&(a.eng==b.eng)) return a.math>b.math;
  if (a.chi==b.chi) return a.eng>b.eng;
  else return a.chi>b.chi; 
}
int main(){
  Node stu[Size];
  srand(time(NULL));
  for (int i=0;i<Size;i++){ 
    stu[i].chi=rand()%40+60;
    stu[i].eng=rand()%40+60;
    stu[i].math=rand()%40+60;
  }
  sort(stu,stu+Size,cmp);
  for(int i=0;i<Size;i++){
    cout<<stu[i].chi<<" "<< stu[i].eng<<" "<<stu[i].math<<endl;        
  }
}
