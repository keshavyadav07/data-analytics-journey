#include <iostream>
using namespace std;

class bus{
    string busname;
    string busnumber;

public:
    void addbusInfo(){
        cout << "Enter bus name and number: ";
        cin >> busname >> busnumber;
    }

    void showbusInfo(){
        cout << "Bus name=" << busname << " and number=" << busnumber << endl;
    }
};

class driver : public bus{
    string DriverName;
    long int phonenumber;

public:
    void addDInfo(){
        cout << "Enter DriverName and PhoneNumber: ";
        cin >> DriverName >>phonenumber;
    }

    void showDInfo(){
        cout << "DriverName=" << DriverName << " and PhoneNumber=" << phonenumber << endl;
    }
};

class manager : public driver{
    string managerName;
    string managerID;

public:
    void addmanagerInfo(){
        cout << "Enter managerName and managerID: ";
        cin >> managerName >> managerID;
    }

    void showmanagerInfo(){
        cout << "managerName=" << managerName << " and managerID=" << managerID << endl;
    }
};

int main(){
     cout<<"keshav yadav \n time 10:35"<<endl;
    

    //create class object for student class
    bus b1;
    b1.addbusInfo();
    b1.showbusInfo();

    //create class object for teacher class
    driver d1;
    d1.addDInfo();
    d1.showDInfo();
    d1.addbusInfo();
    d1.showbusInfo();
    //create class object for teacher class
    manager m1;
    m1.addmanagerInfo();
    m1.showmanagerInfo();
    m1.addDInfo();
    m1.showDInfo();
    m1.addbusInfo();
    m1.showbusInfo();

    return 0;
}