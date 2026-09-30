qe#include<iostream>
using namespace std;
class fun
{
	public:
	void area(int);
	void area(int,int);
	void area(float,int,int);
};
void fun::area(int a){
	cout<<"Area of circle:" << 3.14 * a*a;
}
void fun::area(int a, int b){
	cout<<"Area of rectangle:" <<a*b;
}
void fun::area(float t,int a,int b){
	cout<<"Area of triangle:" << t * a*b;
}
int main()
{
	char ch;
	int choice;
	int a,b,r;
	fun obj;
	cout<<"name:-keshav yadav\n";
	cout<<"roll no:-0832cs241102\n";
	do
	{
		cout<<"\nFunction overloading";
		cout<<"\n.Area of circle\n2.Area of Rectangle\n3.Area of Triangle\n4.Exit\n5";
		cout<<"Enter your choice :";
		cin>>choice;
		switch (choice)
		{
			case 1:
			cout<<"Enter Radius of the circle";
			cin>>r;
			obj.area(r);
			break;
			case 2:
			cout<<"Enter sides of Rectangle:";
			cin>> a>>b;
			obj.area(a,b);
			break;
			case 3:
			cout<<"Enter sides of Triangle:";
			cin>> a>>b;
			obj.area(0.5,a,b);
			break;
			case 4:
			exit(0);
		}
		cout<<"\nDo u want to continue[y/Y]";
		cin>>ch;
		
	
	}
	while(ch=='y' ||  ch=='Y');
	
return 0;
}
