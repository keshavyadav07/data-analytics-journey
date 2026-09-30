






















































#include<stdio.h>
int main(){
	
	  for(int i=1; i<100; i++){
		if(i>10 || i<20){
			continue;
		}
		printf("%d\n",i);
	}
	return 0;
}
