#include <iostream>
#include <malloc.h>
using namespace std;

struct node
{
    int data;
    struct node *next;
    struct node *prev;
} *start = NULL, *cur, *temp, *ptr;

void insertbeg();
void insertend();
void insertspec();
void delbeg();
void delend();
void delspec();
void disp();
int main()
{
    int ch;
    do
    {
        cout << "Main menu" << endl;
        cout << "Press 1 for insertion at beginning" << endl;
        cout << "Press 2 for insertion at end" << endl;
        cout << "Press 3 for insertion at specified" << endl;
        cout << "Press 4 for deletion at beginning" << endl;
        cout << "Press 5 for deletion at end" << endl;
        cout << "Press 6 for deletion at specified position" << endl;
        cout << "Press 8 for exit" << endl;
        cout << "Enter your choice: ";
        cin >> ch;

        switch (ch)
        {
        case 1:
            insertbeg();
            break;
        case 2:
            insertend();
            break;
        case 3:
            insertspec();
            break;
        case 4:
            delbeg();
            break;
        case 5:
            delend();
            break;
        case 6:
            delspec();
            break;
        default:
            cout << "\nwrong choice ";
        }
    } while (ch != 8);

    return 0;
  }
void insertbeg()
{
    ptr = (struct node*)malloc(sizeof(struct node));
    if (ptr == NULL)
    {
        cout << "\nlinked list is full" << endl;
    }
    else
    {
        cout << "Enter the number: ";
        cin >> ptr->data;
        if (start == NULL)
        {
            ptr->next = NULL;
            ptr->prev = NULL; // ???? ?????? ????? ?? ??? 'prev' ?? ??? ???? ?????
            start = ptr;
        }
        else
        {
            ptr->next = start;
            start->prev = ptr; // ???? ?????? ????? ?? ???
            ptr->prev = NULL; // ???? ?????? ????? ?? ???
            start = ptr;
        }
    }
} // '}' ???? ??? ?? ??? ??

void insertend()
{
    ptr = (struct node*)malloc(sizeof(struct node));
    if (ptr == NULL)
    {
        cout << "\nlinked list is full";
    }
    else
    {
        cout << "enter the number";
        cin >> ptr->data;
        ptr->next = NULL;
        if (start == NULL)
        {
            // ???? ?????? ????? ?? ???
            start = ptr;
        }
        else
        {
            temp = start;
            while (temp->add != NULL)
            {
                temp = temp->add;
            }
            temp->next = ptr;
            ptr->prev = temp; // ???? ?????? ????? ?? ???
        }
    }
}

void insertspec()
{
    int pos;
    ptr = (struct node*)malloc(sizeof(struct node));
    if (ptr == NULL)
    {
        cout << "\nlinked list is full";
    }
    else
    {
        cout << "Enter the number";
        cin >> ptr->data;
        cout << "enter position";
        cin >> pos;
        temp = start;
        for (int i = 1; i < pos; i++)
        {
            prev1 = temp;
            temp = temp->add;
        }
       
        prev1->add = ptr;
        ptr->add = temp;
    }
}

void delbeg()
{
    if (start == NULL)
    {
        cout << "\nlinked list is empty";
    }
    else
    {
        cout << "\ndeleted element is " << start->data;
        if (start->add == NULL)
        {
            start = NULL;
        }
        else
        {
            temp = start;
            start = start->add;
            free(temp);
        }
    }
}

void delend()
{
    if (start == NULL)
    {
        cout << "\nlinked list is empty";
    }
    else
    {
        if (start->add == NULL)
        {
            cout << "\ndeleted element is " << start->data
        start = NULL;
    }
    else
    {
        temp = start;
        while (temp->add != NULL)
        {
            prevs = temp;
            temp = temp->add;
        }
        cout << "\ndeleted element is: " << temp->data;
        prevs->add = NULL;
        free(temp);
    }
}

void delspec()
{
    int pos;
    if (start == NULL)
    {
        cout << "\nlinked list is empty";
    }
    else
    {
        cout << "\nenter the position";
        cin >> pos;
        temp = start;
        for (int i = 1; i < pos; i++)
        {
            prevs = temp;
            temp = temp->add;
        }
        prevs->add = temp->add;
        cout << "\ndeleted element is " << temp->data;
        free(temp);
    }
}

void disp()
{
    if (start == NULL)
    {
        cout << "\nll is empty";
    }
    else
    {
        temp = start;
        cout << "\nelement in linked list are: ";
        while (temp != NULL)
        {
            cout << " " << temp->data;
            temp = temp->add;
        }
    }
}
