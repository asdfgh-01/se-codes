// AMANDA SALDANHA 9574
#include<stdio.h>
int search(int arr[], int ele, int n)
{
    for(int i=0; i<n; i++)
    {
        if(arr[i]==ele)
            return i;
    }
}
int main()
{
    int n, x, ele, arr[100];
    printf("enter the size of your array :");
    scanf("%d",&n);
    printf("enter the elements of your array :");
	for(int i=0; i<n; i++)
		scanf("%d",&arr[i]);
    printf("enter the element you wish to search :");
    scanf("%d",&ele);
    x = search(arr, ele, n);
    if(x<n)    
        
        printf("element found at index %d!\n",x);
    else
        printf("element not found!\n");
}
