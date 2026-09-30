#include <iostream>
#include <cstdlib>
using namespace std;

struct node {
    int data;
    node *add;
};

node *start = NULL, *ptr, *temp, *prev;

void insert_beg();
void insert_end();
void insert_spec();
void del_beg();
void del_end();
void del_spec();
void dis();

int main() {
	cout<<" name:-keshav yadav"<<endl;
	cout<<"roll no:-0832cs241102"<<endl;
    int ch;
    do {
        cout << "\n---- MAIN MENU ----\n";
        cout << "1. Insert at beginning\n";
        cout << "2. Insert at end\n";
        cout << "3. Insert at specific position\n";
        cout << "4. Delete at end\n";
        cout << "5. Delete at beginning\n";
        cout << "6. Delete at specific position\n";
        cout << "7. Display\n";
        cout << "8. Exit\n";
        cout << "Enter your choice: ";
        cin >> ch;

        switch (ch) {
            case 1: insert_beg(); break;
            case 2: insert_end(); break;
            case 3: insert_spec(); break;
            case 4: del_end(); break;
            case 5: del_beg(); break;
            case 6: del_spec(); break;
            case 7: dis(); break;
            case 8: cout << "Exiting..."; break;
            default: cout << "Invalid choice!";
        }

    } while (ch != 8);

    return 0;
}

void insert_beg() {
    ptr = (node*)malloc(sizeof(node));
    if (ptr == NULL) cout << "\nMemory full";
    else {
        cout << "Enter data: ";
        cin >> ptr->data;
        ptr->add = start;
        start = ptr;
    }
}

void insert_end() {
    ptr = (node*)malloc(sizeof(node));
    if (ptr == NULL) cout << "\nMemory full";
    else {
        cout << "Enter data: ";
        cin >> ptr->data;
        ptr->add = NULL;

        if (start == NULL) start = ptr;
        else {
            temp = start;
            while (temp->add != NULL) temp = temp->add;
            temp->add = ptr;
        }
    }
}

void insert_spec() {
    int pos;
    ptr = (node*)malloc(sizeof(node));
    if (ptr == NULL) cout << "\nMemory full";
    else {
        cout << "Enter data: ";
        cin >> ptr->data;
        cout << "Enter position: ";
        cin >> pos;

        if (pos == 1) {
            ptr->add = start;
            start = ptr;
        } else {
            temp = start;
            for (int i = 1; i < pos - 1 && temp != NULL; i++) temp = temp->add;

            if (temp == NULL) cout << "Position out of range";
            else {
                ptr->add = temp->add;
                temp->add = ptr;
            }
        }
    }
}

void del_beg() {
    if (start == NULL) cout << "\nList empty";
    else {
        temp = start;
        cout << "Deleted: " << temp->data;
        start = start->add;
        free(temp);
    }
}

void del_end() {
    if (start == NULL) cout << "List empty";
    else if (start->add == NULL) {
        cout << "Deleted: " << start->data;
        free(start);
        start = NULL;
    }
    else {
        temp = start;
        while (temp->add->add != NULL) temp = temp->add;
        cout << "Deleted: " << temp->add->data;
        free(temp->add);
        temp->add = NULL;
    }
}

void del_spec() {
    int pos;
    if (start == NULL) cout << "List empty";
    else {
        cout << "Enter position: ";
        cin >> pos;

        if (pos == 1) del_beg();
        else {
            temp = start;
            for (int i = 1; i < pos - 1 && temp != NULL; i++) temp = temp->add;

            if (temp == NULL || temp->add == NULL) cout << "Position out of range";
            else {
                node *del = temp->add;
                cout << "Deleted: " << del->data;
                temp->add = del->add;
                free(del);
            }
        }
    }
}

void dis() {
    if (start == NULL) cout << "List empty";
    else {
        temp = start;
        cout << "Elements: ";
        while (temp != NULL) {
            cout << temp->data << " ";
            temp = temp->add;
        }
    }
}
