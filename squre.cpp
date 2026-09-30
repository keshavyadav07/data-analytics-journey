#include<iostream>
using namespace std;

void title()
{
	//cout<<"\n Experiment No. 05"<<endl;
	cout<<" Name : keshav yadav"<<endl;
	cout<<" Enroll. No. : 0832CS241102"<<endl;
	//cout<<" Class : III-C (C2)"<<endl<<endl;
}

class square
{
	public:
		int side;
		void sq_input()
		{
			cout<<" Enter Sides of Square :  ";
			cin>>side;
		}
};
class rectangle
{
	public:
		int len,br;
		void rec_input()
		{
			cout<<"\n Enter length of rectangle : ";
			cin>>len;
			
			cout<<" Enter breadth of rectangle : ";
			cin>>br;
		}
};
class area: public square, public rectangle
{
	public:
		void sq_output()
		{
			cout<<" Area of a square is : "<<side*side;
			cout<<endl;
		}
		void rec_output()
		{
			cout<<" Area of a rectangle is : "<<len*br;
			cout<<endl;
		}
};
int main()
{
	title();
	area sq,rec;
	sq.sq_input();
	sq.sq_output();
	rec.rec_input();
	rec.rec_output();
	return 0;
}
