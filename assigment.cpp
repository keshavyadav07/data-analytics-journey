1#include<stdio.h>
int main(){
	int a;
	printf("enter the value a=");
	scanf("%d",&a);
	printf("a=%d",a);
	 a=a+4;
	 printf("the value of a+=%d",a);
	 a-=5;
	 printf("\nthe value of a-=%d",a);
	 a*=10;
	 printf("\nthe value of a*=%d",a);
	 a/=2;
	 printf("\nthe value of a/=%d",a);
	 a%=5;
	 printf("\nthe value of a mod=%d\n",a);
		return 0;
}
