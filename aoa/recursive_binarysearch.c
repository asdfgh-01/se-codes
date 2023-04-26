//amanda saldanha 9574
#include <stdio.h>
int rec_binary_search(int a[],int low,int high,int x)
{
    int mid;
    if(low==high)
    {
        if(a[low]==x)
            return low;
        else
            return -1;
    }
    else
    {
        mid=(low+high)/2;
            if(x==a[mid])
                return mid;
            else if(x<a[mid])
                return (rec_binary_search (a,low,mid-1,x));
            else if(x>a[mid])
                return (rec_binary_search (a,mid+1,high,x));
    }   
}
int main()
{
    int a[50];
    int n, low, high, ele, x;
    printf("enter number of elements:");
    scanf("%d",&n);
    for(int w=0;w<n;w++)
    {
        printf("enter the elements: ");
        scanf("%d",&a[w]);
    }
    printf("enter element to be searched:");
    scanf("%d",&ele);
    low = 0;
    high = n-1;
    if(rec_binary_search(a,low,high,ele)==-1)
        printf("the element is not present in the array!");
    else
        printf("the element is present in the array!");
    return 0;
}
