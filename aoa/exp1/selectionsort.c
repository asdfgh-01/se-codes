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
    for(int i= 0;i<n-1;i++)
    {
        int index = i;
        for(int j = i+1; j<n;j++)
        {
            if(arr[j]<arr[index])
            {
                index = j;
            }
        }
        int temp = arr[i];
        arr[i]=arr[index];
        arr[index]=temp;

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