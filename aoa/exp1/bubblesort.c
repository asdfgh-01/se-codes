#include <stdio.h>
void swap(int* x, int* y)
{
    int temp = *x;
    *x = *y;
    *y = temp;
}

void bs(int arr[100], int n)
{
    for(int i = 0; i<= n-2; i++)
    {
        for(int j = 0; j<=n-2-i; j++)
        {
            if(arr[j]>arr[j+1])
            swap(&arr[j],&arr[j+1]);
        }
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
        printf("%d ",a[i]);
    }
    printf("\n");
    return 0;
}