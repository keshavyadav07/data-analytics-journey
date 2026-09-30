#include<iostream>
using namespace std;
class emplayee{
	
	string name;
	string id;
	string company;
	float basic ;
	float da;
	float If;
	float net_salary;
	
	public:
		void get_details(){
			cout<<"\n enter the name of the employe :";
			cin>>name;
			cout<<"\n enter the the employe id :";
			cin>>id;
			cout<<"\n enter the name of the company :";
			cin>>company;
			cout<<"\n enter the basic of the employe :";
			cin>>basic;
		}
		void netsalary(){
			da=0.52*basic;
			If=0.32*(basic+ da);
			net_salary=(basic+ da )-If;
		}
		void showdetails(){
			cout<<"\n name :"<<name<<endl;
			cout<<"\n id :"<<id<<endl;
			cout<<"\n company :"<<company<<endl;
			cout<<"\ndecariness allowance :"<<da<<endl;
			cout<<"\n income tax :"<<If<<endl;
			cout<<"\n net_salary :"<<net_salary<<endl;
		}
};
int main(){
	emplayee emp;
	cout<<"\n name :- keshav yadav \n";
	cout<<"\n branch :- cse";
	cout<<"\n roll no :- 0832cs241102 ";
	cout<<"\n section :- B";
	emp.get_details();
	emp.netsalary();
	emp.showdetails();
	
	
}
