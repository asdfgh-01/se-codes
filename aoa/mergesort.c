// AMANDA SALDANHA 9574
#include<stdio.h>
void merge(int arr[100], int low, int mid, int high)
{
	int n1, n2, i, j, k;
	n1 = mid-low +1;
	n2 = high-mid;
	int L[n1],R[n2];
	for(i=0; i<n1; i++)
		L[i]=arr[i+low];
	for(j=0; j<n2; j++)
		R[j]=arr[j+mid+1];
	i=0;
	j=0;
	for(k=low; (i<n1 && j<n2); k++)
	{
		if(L[i]<R[j])
		{
			arr[k]=L[i];
			i++;
		}
		else
		{
			arr[k]=R[j];
			j++;
		}	
	}
	while(i<n1)
		arr[k++]=L[i++];
	while(j<n2)
		arr[k++]=R[j++];
}
void merge_sort(int arr[100], int low, int high)
{
	if(low<high)
	{
		int mid = (low+high)/2;
		merge_sort(arr, low, mid);
		merge_sort(arr, mid+1, high);
		merge(arr, low, mid, high);
		for(int j=low; j<=high; j++)
			printf("%d\t",arr[j]);
		printf("\n");
	}
}
int main()
{
	int n, arr[100];
	printf("enter the size of your array :");
	scanf("%d",&n);
	printf("enter the elements of your array :");
	for(int i=0; i<n; i++)
		scanf("%d",&arr[i]);
	int low = 0, high = n-1;
	printf("ITERATIONS :\n");
	merge_sort(arr, low, high);
	printf("SORTED ARRAY :\n");
	for(int j=0; j<n; j++)
		printf("%d\t",arr[j]);
	printf("\n");
}
