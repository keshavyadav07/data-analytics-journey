#include<stdio.h>
#include<ctype.h>
#include<string.h>
int main(){
	char str[]="keshav";
	int len=strlen(str);
	printf("%d\n",len);
	printf("before case change :str =%s\n",str);
	for(int i=0;i<len;i++){
		str[i]=toupper(str[i]);
	printf("after case change :str =%s\n",str);
}
	
	return 0;
}
