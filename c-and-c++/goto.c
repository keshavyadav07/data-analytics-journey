#include<stdio.h>
int main(){
	int id,password;
	keshav:
	printf("enter the value of id:");
	scanf("%d",&id);
	printf("enter the value of password:");
	scanf("%d",&password);
	if(id==1000 && password==1234){
		printf("login successully\n");
	}
	else{
		printf("incorrect please again\n");
		goto keshav;
	}
	
	return 0;
}
