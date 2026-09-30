#include<iostream>
using namespace std;

int fact(int);
int main(){
	int a,b;
	cout<<"enter no";
	cin>>a;
	cout<<"enter no";
	cin>>b;
}
int fact(int c){
	if(c==1)
	return 1;

 else
	return(c*fact(c-1));
}
