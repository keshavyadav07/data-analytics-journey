#include<iostream>
using namespace std;
class operators{
	int typeofoperators,a,b ;
	public:
		void myoperator(){
		
		cout<<"enter operators type:\n press 1 for unary operator \n press 2 for arithmetic operator \n press 3 for rational operator \n press 4 for bitwise operator "<<endl;
		cin>>typeofoperators;
		if(typeofoperators==1){
			cout<<"enter the of a: "<<endl;
			cin>>a;
			cout<<"preincrement(++a)="<<++a<<endl;
			cout<<"postincrement(a++)="<<a++<<endl;
			cout<<"predecrement(--a)="<<--a<<endl;
			cout<<"postdecrement(a--)="<<a--<<endl;
		}
		else if(typeofoperators==2){
			cout<<"enter the value a and b:"<<endl;
			cin>>a>>b;
			cout<<"a+b="<<a+b<<endl;
			cout<<"a-b="<<a-b<<endl;
			cout<<"a*b="<<a*b<<endl;
			cout<<"a/b="<<a/b<<endl;
			cout<<"a%b="<<a%b<<endl;
		}
	else if(typeofoperators==3){
		cout<<"enter the value a and b:"<<endl;
			cin>>a>>b;
			cout<<"a<b="<<(a<b)<<endl;
			cout<<"a>b="<<(a>b)<<endl;
			cout<<"a<=b="<<(a<=b)<<endl;
			cout<<"a>=b="<<(a>=b)<<endl;
			cout<<"a!=b="<<(a!=b)<<endl;
	}
	else if(typeofoperators==4){
		cout<<"enter the binary number(0/1)"<<endl;
		cout<<"enter the value a and b :"<<endl;
		cin>>a>>b;
		cout<<"a&b"<<(a&b)<<endl;
		cout<<"a|b"<<(a|b)<<endl;
		cout<<"a^b"<<(a^b)<<endl;
		cout<<"~a="<<(~a)<<"~b="<<(~b)<<endl;
	}
}
};
int main(){
	cout<<"name :- keshav yadav \n time 11:00pm\n program_name:-opertors.cpp\n";
	operators o1;
	o1.myoperator();
	
}
