#include<iostream>
using namespace std;

int main()
{
    cout<<"name :- keshav yadav \n roll no:-0832cs241102"<<endl;    
    int list[100], i, j, n, temp;

    cout << "enter the number";
    cin >> n;

    cout << "enter the array is first array";
    for(i = 1; i <= n; i++)
        cin >> list[i];

    for(i = 2; i <= n; i++)
    {
        temp = list[i];
        j = i - 1;

        while((temp < list[j]) && (j >= 1))
        {
            list[j + 1] = list[j];
            j--;
        }
        list[j + 1] = temp;
    }

    cout << "after sorting are";
    for(i = 1; i <= n; i++)
        cout << endl << list[i];
}