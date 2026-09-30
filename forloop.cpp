#include<stdio.h>
int main(){
	int num;
	printf("enter the value num");
	scanf("%d",&num);
	for(int i=1;i<=500;i++){
		
		printf("%d*%d =%d\n",num,i,num*i);
		
		
	}
}
