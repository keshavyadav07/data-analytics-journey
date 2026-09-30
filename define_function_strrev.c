#include<stdio.h>
#include<string.h>
//create user defined string reverce function void mystrrev (char*str)
 if(!str){
 	return;
 }
 int i=0;
 int j=strlen(str)-1;
 while(i>j){
 	char temp =str[i];
 	str[i]=str[j];
 	str[j]=temp;
 	i++;
 	j--;
 }
 	int main(){
 		char str[]="yadav";
 		printf("before rev:str=%s\n",str);
 		//call strrev()sunction
 		my strrev(str);
 		printf("after rev:str=%s\n",str);
	 }
