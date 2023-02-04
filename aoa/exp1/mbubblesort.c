#include <stdio.h>
void swap(int* x, int* y)
{
    int temp = *x;
    *x = *y;
    *y = temp;
}

void bs(int arr[100], int n)
{
    int flag = 1;
    for(int i = 0; i< n-1 && flag ==1; i++)
    {
        flag = 0;
        for(int j = 0; j<n-i-1; j++)
        {
            if(arr[j]>arr[j+1])
            swap(&arr[j],&arr[j+1]);
            flag = 1;
        }
        for(int a = 0; a<n;a++)
        {
            printf("%d      ",arr[a]);
        }    
        printf("\n");
    }
}


int main()
{
    int a[100];
    int n;
    printf("enter number of elements:");
    scanf("%d",&n);
    for(int w=0;w<n;w++)
    {
        printf("enter the elements: ");
        scanf("%d",&a[w]);
    }    
    bs(a,n);

    for(int i = 0; i<n;i++)
    {
        printf("%d      ",a[i]);
    }
    printf("\n");
    return 0;
}