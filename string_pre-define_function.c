#include<stdio.h>
#include<string.h>
int main(){
	//cout number of charavter using strlen()
	char firstname[]="keshav";
	char lastname[]="yadav";
	//find string length
	printf("length of fistname=%ld",strlen(firstname));
	printf("length of lastname=%ld",strlen(lastname));
	//cocatinate two string->strcat()
	printf("cocatinate string is %s\n",strcat(firstname,lastname));
	printf("cocatinate string is %s\n",strcat(firstname));
	//strcpy()copy one string to another string
	char bck[20];
	strcpy (bck,fistname);
	printf("bck value is %s\n",bck);
	//strcmp()-compare two string if return 0 so buth string are same and atherwise different value
	char str1[]="INDORE";
	char str2[]="Indore";
	char str3[]="iNDORE";
	char str4[]="INDORE";
	printf("strcmp(str1,str2)=%d\n",strcmp(str1,str2));
	printf("strcmp(str2,str3)=%d\n",strcmp(str2,str3));
	printf("strcmp(str3,str4)=%d\n",strcmp(str3,str4));
	printf("strcmp(str1,str4)=%d\n",strcmp(str1,str4));
	
	return 0;
}
