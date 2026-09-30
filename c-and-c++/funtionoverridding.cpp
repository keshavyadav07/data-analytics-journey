#include<iostream>
using namespace std;
class base{
    public:
    //virtual function
    virtual void show(){
        cout<<"this is base class funtion"<<endl;
    }
};
class derived : public base{
    public:
    void show(){
        cout<<"this is derived class funtion "<<endl;
    }
};
int main(){
    //create derived class obj
    derived objd;
    objd.show();
    base* ptrbase;
    ptrbase = &objd;
    ptrbase->show();
}