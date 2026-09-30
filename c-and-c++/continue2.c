#include<stdio.h>
int main(){
	
	int start,end;
	printf("enter the value start=");
	scanf("%d\n",&start);
	printf("enter the value end=");
	scanf("%d\n",&end);
	
	for(int i=start; i<=end; i++){
		if(i%4==0){
			continue;
		}
		printf("value of i=%d\n",i);
	}
}
