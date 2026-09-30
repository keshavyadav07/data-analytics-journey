#include<stdio.h>
int main(){
	int size;
	printf("enter the size:");
	scanf("%d",&size);
	 int my[size];
	 printf("------insert array value-----\n");
	 for(int i=0;i<size;i++){
	 	printf("enter value of my[%d]=",i);
	 	scanf("%d",&my[i]);
	 }
	 printf("enter thr value of my[%d]=",size);
		for(int i =0; i<size;i++){
			printf("{");
				printf("%d",my[i]);
				if(i<size-1){
					printf(",");
				}
			}
			printf("}");
	   printf("};");
	
	
}
