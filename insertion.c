#include<stdio.h>
#include<stdlib.h>
#include<time.h>
int insertionsort(int*,int);
int insertionsort(int *arr,int n)
{
    int i,j,temp;
for(i=1;i<n;i++)
    {
        temp=*(arr+i);
        j=i-1;
        while(temp<*(arr+j)&&j>=0)
        {
            *(arr+(j+1))=*(arr+j);
            j--;
        }
        *(arr+(j+1))=temp;
    }
    return 0;
}
int main()
{
    int *arr,i,n;
    double t;
    printf("Enter the no. of elements\n");
    scanf("%d",&n);
    clock_t start,end;
    start=clock();
    arr=(int*)malloc(n*sizeof(int));

    for(i=0;i<n;i++)
        {arr[i]=(rand()%n+1);}
    insertionsort(arr,n);
    end=clock();

    t=((double)end-start)/CLOCKS_PER_SEC;
    printf("Time is :%lf ",t);

   /* printf("Sorted array is\n");
    for(i=0;i<n;i++)
        printf("%d\n",*(arr+i));*/
    return 0;
}
