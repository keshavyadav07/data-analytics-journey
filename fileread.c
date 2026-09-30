#include<stdio.h>
#include<stdlib.h>
void main(){
	FILE *fp;
	char ch;
	fp = fopen("mydocument.txt","r");
	while(1){
		ch = fgetc(fp);
		if(ch== EOF){
			exit(1);
		}
		printf("%c",ch);
	}
	fclose(fp);
}
