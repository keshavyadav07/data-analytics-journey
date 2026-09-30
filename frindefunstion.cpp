#include<iostream>
using namespace std;

class marks{
	int num;
	friend void totalmarks(marks const& o1,marks const& o2, marks const& o3,marks const& o4);
	public:
		marks(int num=0){
			this->num=num;
		}
		void show(){
			cout<<"marks="<<num<<endl;
		}
};
void totalmarks(marks const& o1,marks const& o2, marks const& o3,marks const& o4){
	cout<<"total marks="<<(o1.num+o2.num+o3.num+o4.num)<<endl;
}
int main(){
	cout<<"keshav yadav\n friend function\n date :-8/12/2025\n time 9:34"<<endl;
	marks hindi(90),dsa(88),oopm(75),maths;
	totalmarks(hindi,dsa,oopm,maths);
}
