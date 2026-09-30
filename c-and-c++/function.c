#include<stdio.h>
 void doublearray(int myarr[],int n){
 	for(int i=0; i<n; i++){
 		myarr[i]= myarr[i]*2;
	 }
 }
int main(){
	 int arr[5]={2,4,6,8,10};
	 printf("before calling function\n");
	 for(int i=0; i<5; i++){
	 	printf("%d\n",arr[i]);
	 }
	 int size=sizeof(arr)/sizeof(arr[0]);
	 doublearray(arr,size);
	 printf("after calling funtion\n");
	 for(int i=0;i<5;i++){
	 	printf("%d",arr[i]);
	 }
	 	return 0;
}
