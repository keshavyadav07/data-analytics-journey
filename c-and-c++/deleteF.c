#include<stdio.h>
int main(){
	if(remove("mydatafile.txt")==0){
		printf("deleted successfully");
	}
	else{
		printf("unable to delete the file");
	}
	return 0;
}
