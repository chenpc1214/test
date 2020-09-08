#include<iostream>
using namespace std;
int main(){
  int fri[50001],visit[50001],count,n,next;
  while(cin>>n){
    count=0;
    for(int i=0;i<n;i++){
      cin>> fri[i];
      visit[i]=0;
    }
    for(int i=0;i<n;i++){
      if (visit[i]==0){//沒有拜訪過 
        if (fri[i]==i) {//好朋友只有自己 
          count++;
          visit[i]=1;
        }else{
          next=i;
          do{
            visit[next]=1;
            next=fri[next];
          }while(visit[next]==0);
          count++;
        } 
      }
    }
    cout<<count<<endl;
  }
} 
