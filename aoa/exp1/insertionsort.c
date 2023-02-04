#include <stdio.h>
void main()
{
    int arr[100];
    int n;
    printf("enter number of elements:");
    scanf("%d",&n);
    for(int w=0;w<n;w++)
    {
        printf("enter the elements: ");
        scanf("%d",&arr[w]);
    }    
    for(int i= 1;i<n;i++)
    {
        int j;
        int key = arr[i];
        j=i-1;
        while(j>=0 && arr[j]>key)
        {
            arr[j+1] = arr[j];
            j--;
        }
        arr[j+1]=key;
        for(int a = 0; a<n;a++)
        {
            printf("%d      ",arr[a]);
        }    
        printf("\n");
    }

    for(int i = 0; i<n;i++)
    {
        printf("%d      ",arr[i]);
    }
    printf("\n");
}