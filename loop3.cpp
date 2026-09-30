#include<stdio.h>
int main(){
	for(int i=1;i<=10;i++){
		int j=0;
		while(j<5){
			printf(" * ");
	//	printf(" %d ",i);
		//printf(" %d ",j);
		//printf(" %c ",i=i+65);
			j++;
		}
		printf("\n");
	}

	for(int u=1;u<=5;u++){
		for(int v=0;v<u;v++){
			printf(" 16 ");
		}
		printf("\n");
	}
}
