#include<iostream>
using namespace std;
class datatype{
	string name;
	char sex;
	int age;
	float salary;
	bool boolvalue;
	
	public:
		
		void details(){
			cout<<"enter the name,sex,age,salary,boolvalue"<<endl;
			cin>>name>>sex>>age>>salary>>boolvalue;
			
			cout<<"---------details-------------"<<endl;
			cout<<"name="<<name<<"\nsex="<<sex<<"\nage"<<age<<"\nsalary"<<salary<<"\nboolvalue"<<boolvalue;
		}
};
int main(){
	cout<<"name :- keshav yadav \n time 11:20pm\n program_name:-datatype.cpp\n";
	datatype dt1;
	dt1.details();
}
