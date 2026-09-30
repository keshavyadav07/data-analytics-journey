
#include <iostream>
 #define maxsize 5
using namespace std;

void insert();
void deletee();
void display();

int queue[maxsize];
int rear = -1, front = -1; // Corrected the 'int' duplication
int no; // Added missing variable 'no'

int main()
 
{
	cout<<"name:- Keshav Yadav"<<endl;
 cout<<"roll no:- 0832cs241102"<<endl;
 cout<<"branch:-CS'B'"<<endl;
    int ch;
    do
    {
        cout << "Main menu" << endl;
        cout << "Press 1 to insert element" << endl;
        cout << "Press 2 to delete element" << endl;
        cout << "Press 3 to display elements" << endl;
        cout << "Press 4 for exit" << endl;
        cout << "Enter your choice" << endl;
        cin >> ch;

        switch (ch)
        {
        case 1:
            insert();
            break;
        case 2:
            deletee();
            break;
        case 3:
            display();
            break;
        case 4:
            break;
        }
    } while (ch != 4);

    return 0;
}

void insert()
{
    if (rear == maxsize - 1)
    {
        cout << "\nqueue is full";
    }
    else
    {
        cout << "\nEnter the element: ";
        cin >> no;

        if (rear == -1)
        {
            rear = front = 0;
        }
        else
        {
            rear++;
        }
        queue[rear] = no;
    }
}

void deletee()
{
    if (front == -1)
    {
        cout << "\nQueue is empty";
    }
    else
    {
        cout << "\nDeleted element is " << queue[front];
        if (front == rear)
        {
            front = rear = -1;
        }
        else
        {
            front++;
        }
    }
}

void display()
{
    int i; // Added missing loop variable declaration
    if (rear == -1)
    {
        cout << "\nQueue is empty";
    }
    else
    {
        // This is based on the logic from the image
        for (i = front; i <= rear; i++)
        {
            cout << " " << queue[i]; // Added missing 'cout <<'
        }
    }
}
