#include<iostream>
using namespace std;
class time{
    int hours,mintues;
    public:
    time(int h=0,int m=0){
    hours=h ; mintues=m;
    }
    time operator+(time const& obj){
        cout<<"operator+"<<endl;
        time response;
        response.hours=hours+obj.hours;
        response.mintues=mintues+obj.mintues;
        return response;
    }
    time operator-(time const& obj){
        cout<<"operator-n"<<endl;
        time response;
        response.hours=hours-obj.hours;
        response.mintues=mintues-obj.mintues;
        return response;
    }
    time operator*(time const& obj){
        cout<<"operator*"<<endl;
        time response;
        response.hours=hours*obj.hours;
        response.mintues=mintues*obj.mintues;
        return response;
    }
    time operator/(time const& obj){
        cout<<"operator/"<<endl;
        time response;
        response.hours=hours/obj.hours;
        response.mintues=mintues/obj.mintues;
        return response;
    }
    time operator<(time const& obj){
        cout<<"operator<"<<endl;
        time response;
        response.hours=hours<obj.hours;
        response.mintues=mintues<obj.mintues;
        return response;
    }
    time operator>(time const& obj){
        cout<<"operator>"<<endl;
        time response;
        response.hours=hours>obj.hours;
        response.mintues=mintues>obj.mintues;
        return response;
    }
    time operator>=(time const& obj){
        cout<<"operator>="<<endl;
        time response;
        response.hours=hours>=obj.hours;
        response.mintues=mintues>=obj.mintues;
        return response;
    }
    time operator<=(time const& obj){
        cout<<"operator<="<<endl;
        time response;
        response.hours=hours<=obj.hours;
        response.mintues=mintues<=obj.mintues;
        return response;
    }
    time operator==(time const& obj){
        cout<<"operator=="<<endl;
        time response;
        response.hours=hours==obj.hours;
        response.mintues=mintues==obj.mintues;
        return response;
    }
    time operator&&(time const& obj){
        cout<<"operator&&"<<endl;
        time response;
        response.hours=hours&&obj.hours;
        response.mintues=mintues&&obj.mintues;
        return response;
    }
    time operator||(time const& obj){
        cout<<"operator||"<<endl;
        time response;
        response.hours=hours||obj.hours;
        response.mintues=mintues||obj.mintues;
        return response;
    }
    time operator&(time const& obj){
        cout<<"operator&"<<endl;
        time response;
        response.hours=hours&obj.hours;
        response.mintues=mintues&obj.mintues;
        return response;
    }
    time operator|(time const& obj){
        cout<<"operator|"<<endl;
        time response;
        response.hours=hours|obj.hours;
        response.mintues=mintues|obj.mintues;
        return response;
    }
    time operator<<(time const& obj){
        cout<<"operator<<"<<endl;
        time response;
        response.hours=hours<<obj.hours;
        response.mintues=mintues<<obj.mintues;
        return response;
    }
    time operator>>(time const& obj){
        cout<<"operator>>"<<endl;
        time response;
        response.hours=hours>>obj.hours;
        response.mintues=mintues>>obj.mintues;
        return response;
    }
    time operator^(time const& obj){
        cout<<"operator^"<<endl;
        time response;
        response.hours=hours^obj.hours;
        response.mintues=mintues^obj.mintues;
        return response;
    }
    time operator%(time const& obj){
        cout<<"operator%"<<endl;
        time response;
        response.hours=hours%obj.hours;
        response.mintues=mintues%obj.mintues;
        return response;
    }
    void showdetails(){
        cout<<"Hours:"<<hours<<" Mintues:"<<mintues<<endl;
    }
};
int main(){
    cout<<"keshav yadav \n time 3:10"<<endl;
    time t1(2,15),t2(1,30);
    t1.showdetails();
    t2.showdetails();
    time t3=t1+t2;
    t3.showdetails();
    time t4=t1-t2;
    t4.showdetails();
     time t5=t1*t2;
    t5.showdetails();
     time t6=t1/t2;
    t6.showdetails();
     time t7=t1<t2;
    t7.showdetails();
     time t8=t1>t2;
    t8.showdetails();
     time t9=t1>=t2;
    t9.showdetails();
     time t10=t1<=t2;
    t10.showdetails();
     time t11=t1==t2;
    t11.showdetails();
     time t12=t1&&t2;
    t12.showdetails();
     time t13=t1||t2;
    t13.showdetails();
     time t14=t1&t2;
    t14.showdetails();
     time t15=t1|t2;
    t15.showdetails();
     time t16=t1<<t2;
    t16.showdetails();
     time t17=t1>>t2;
    t17.showdetails();
     time t18=t1^t2;
    t18.showdetails();
     time t19=t1%t2;
    t19.showdetails();
}