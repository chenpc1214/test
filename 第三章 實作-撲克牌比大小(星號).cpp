#include <iostream>
#include <string>
#include <cstring>
#include <algorithm>
#include <sstream> 
using namespace std;
int f[13],s[13];
int PokerToNum(string s){
  int suit,num;
  switch(s[1]){
    case 'A':
	  num=12;
	  break;
    case 'K':
	  num=11;
	  break;
    case 'Q':
	  num=10;
	  break;
    case 'J':
	  num=9;
	  break;
	  case 'T':
	  num=8;
	  break;
	  default:
	  num=s[1]-'2';
	  break;
  }
  switch(s[0]){
    case 'C':
	  suit=0;
	  break;
    case 'D':
	  suit=1;
	  break;
    case 'H':
	  suit=2;
	  break;
    case 'S':
	  suit=3;
	  break;
  }
  return (suit*13+num);
}
bool IsSF(int *poker){
  if ((poker[4]-poker[0])==4){
    if ((poker[0]>=0)&&(poker[4]<13)) return true;
    if ((poker[0]>=13)&&(poker[4]<26)) return true;
    if ((poker[0]>=26)&&(poker[4]<39)) return true;
    if ((poker[0]>=39)&&(poker[4]<52)) return true;
  }
  return false;
}
bool IsF(int *poker){
  if ((poker[0]>=0)&&(poker[4]<13)) return true;
  if ((poker[0]>=13)&&(poker[4]<26)) return true;
  if ((poker[0]>=26)&&(poker[4]<39)) return true;
  if ((poker[0]>=39)&&(poker[4]<52)) return true;
  return false;
}
int fL(int *poker){
  if (IsSF(poker)) return 9;
  for(int i=0;i<13;i++) {
	  if (f[i]==4) return 8; 
  }
  for(int i=0;i<13;i++) {
	  if (f[i]==2) {
	    for(int j=i+1;j<13;j++) {
        if (f[j]==3) return 7; 
	    }
	  }
	  if (f[i]==3) {
	    for(int j=i+1;j<13;j++) {
        if (f[j]==2) return 7; 
	    }
	  }
  }
  if (IsF(poker)) return 6;  
  for(int i=0;i<9;i++) {
	  if ((f[i]==1)&&(f[i+1]==1)&&(f[i+2]==1)&&(f[i+3]==1)&&(f[i+4]==1)) {
      return 5; 
	  }
  }
  for(int i=0;i<13;i++) {
	  if (f[i]==3) {
      return 4; 
	  }
  }
  for(int i=0;i<13;i++) {
	  if (f[i]==2) {
	    for(int j=i+1;j<13;j++) {
        if (f[j]==2) return 3; 
	    }
	  }
  }
  for(int i=0;i<13;i++) {
        if (f[i]==2) return 2;  
  }
  return 1;
}
int sL(int *poker){
  if (IsSF(poker)) return 9; 
    for(int i=0;i<13;i++) {
	    if (s[i]==4) return 8; 
    }
    for(int i=0;i<13;i++) {
	    if (s[i]==2) {
	    for(int j=i+1;j<13;j++) {
        if (s[j]==3) return 7; 
	    }
	  }
	  if (s[i]==3) {
	    for(int j=i+1;j<13;j++) {
        if (s[j]==2) return 7;
	    }
	  }
  }
  if (IsF(poker)) return 6;
  for(int i=0;i<9;i++) {
	  if ((s[i]==1)&&(s[i+1]==1)&&(s[i+2]==1)&&(s[i+3]==1)&&(s[i+4]==1)) {
      return 5; 
	  }
  }
  for(int i=0;i<13;i++) {
	  if (s[i]==3) {
      return 4; 
	  }
  }
  for(int i=0;i<13;i++) {
	  if (s[i]==2) {
	    for(int j=i+1;j<13;j++) {
        if (s[j]==2) return 3; 
	    }
	  }
  }
  for(int i=0;i<13;i++) {
    if (s[i]==2) return 2; 
  }
  return 1;
}
int winloss(int level){
  int fh,sh;
  if (level==9) {  
    for(int i=12;i>3;i--){
	    if (f[i]==1) {
		    fh=i;
		    break;
	    }
	  }
    for(int i=12;i>3;i--){
	    if (s[i]==1) {
		    sh=i;
	  	  break;
	    }
	  }
	  if (fh>sh) return 1;
	  if (fh<sh) return -1;
  }
  if (level==8) {  
    for(int i=12;i>=0;i--){
	    if (f[i]==4) {
		    fh=i;
		    break;
	    }
	  }
    for(int i=12;i>=0;i--){
	    if (s[i]==4) {
		    sh=i;
		    break;
	    }
	  }
	  if (fh>sh) return 1;
	  if (fh<sh) return -1;
  }
  if (level==7) { 
    for(int i=12;i>=0;i--){
	    if (f[i]==3) {
		    fh=i;
		    break;
	    }
	  }
    for(int i=12;i>=0;i--){
	    if (s[i]==3) {
		    sh=i;
		    break;
	    }
	  }
	  if (fh>sh) return 1;
	  if (fh<sh) return -1;
  }
  if (level==6) { 
    for(int i=12;i>=0;i--){
	    if ((f[i]==1)&&(s[i]==0)) {
		    return 1;
	    }
	    if ((f[i]==0)&&(s[i]==1)) {
		    return -1;
	    }
	  }
  }
  if (level==5) { 
    for(int i=12;i>=0;i--){
	    if (f[i]==1) {
		    fh=i;
		    break;
	    }
	  }
    for(int i=12;i>=0;i--){
	    if (s[i]==1) {
		    sh=i;
		    break;
	    }
	  }
	  if (fh>sh) return 1;
	  if (fh<sh) return -1;
  }
  if (level==4) {
    for(int i=12;i>=0;i--){
	    if (f[i]==3) {
		    fh=i;
		    break;
	    }
	  }
    for(int i=12;i>=0;i--){
	    if (s[i]==3) {
		    sh=i;
		    break;
	    }
    }
	  if (fh>sh) return 1;
	  if (fh<sh) return -1;
  }
  if (level==3) { 
    for(int i=12;i>=0;i--){
	    if ((f[i]==2)&&(s[i]<2)) {
		    return 1;
	    }
	    if ((f[i]<2)&&(s[i]==2)) {
		    return -1;
	    }
	  }
  }
  if (level==2) { 
    for(int i=12;i>=0;i--){
	    if ((f[i]==2)&&(s[i]<2)) {
		    return 1;
	    }
	    if ((f[i]<2)&&(s[i]==2)) {
		    return -1;
	    }
	  }
  }
  if (level==1) { 
    for(int i=12;i>=0;i--){
	    if ((f[i]==1)&&(s[i]==0)) {
		    return 1;
	    }
	    if ((f[i]==0)&&(s[i]==1)) {
		    return -1;
	    }
	  }
  }
}
int main(){
  int fp[5],sp[5],fLevel,sLevel;
  string line,str;
  int result;
  while(getline(cin,line)){
	  istringstream iss(line);
	  memset(s,0,sizeof(s));
	  memset(f,0,sizeof(f));
	  for(int i=0;i<5;i++){
	    iss >> str;
	    fp[i]=PokerToNum(str);
  	}
	  for(int i=0;i<5;i++){
	    iss >> str;
	    sp[i]=PokerToNum(str);
	  }
	  for(int i=0;i<5;i++){
	    f[fp[i]%13]++;
	  }
	  for(int i=0;i<5;i++){
	    s[sp[i]%13]++;
	  }
	  sort(fp,fp+5);
	  sort(sp,sp+5);
	  fLevel=fL(fp);
	  sLevel=sL(sp);
	  if (fLevel > sLevel) cout << "第一位玩家獲勝"<<endl;
	  else if (fLevel < sLevel) cout << "第二位玩家獲勝"<<endl;
	  else {
      result=winloss(fLevel);
	    if (result == 1) cout << "第一位玩家獲勝"<<endl;
	    if (result == -1) cout << "第二位玩家獲勝"<<endl;
	  }
  }
}
