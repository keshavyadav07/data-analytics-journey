#include<stdio.h>
int main(){
	//create a outerarraysize and innerarraysize
	int outarray,innarray;
	printf("enter the value of outarray and innarray:");
	scanf("%d%d",&outarray,&innarray);
	//define 2D array
	int my[outarray][innarray];
	//insert arry element
	for(int i=0; i<outarray; i++){
		for(int j=0; j<innarray; j++){
			printf("enter thr value of my[%d][%d]=",i,j);
			scanf("%d",&my[i][j]);
		}
	}
	//show 2d array value
		printf("enter thr value of my[%d][%d]=",outarray,innarray);
		for(int i =0; i<outarray;i++){
			printf("{");
			for(int j=0;j<outarray;j++){
				printf("%d",my[i][j]);
				if(J<innarray-1){
					printf(",");
				}
			}
			printf("}");
			if(i<outarray-1){
				printf(",")
			}
		}
	 printf("};");
	
}
