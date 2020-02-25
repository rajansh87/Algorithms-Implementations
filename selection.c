#include<stdio.h>
#include<stdlib.h>
#include<time.h>
int selectionsort(int *,int);
int selectionsort(int *arr,int n)
{
    int i,j,temp;
for(i=0;i<n;i++)
        for(j=i+1;j<n;j++)
        {
            if(*(arr+i)>*(arr+j))
            {
                temp=*(arr+j);
                *(arr+j)=*(arr+i);
                *(arr+i)=temp;
            }
        }
    return 0;
}
int main()
{
    int *arr,n,i;
    double t;
    printf("Enter no. of elements\n");
    scanf("%d",&n);
    clock_t start,end;
    start=clock();
    arr=(int *)malloc(n*sizeof(int));

    for(i=0;i<n;i++)
        {arr[i]=(rand()%n+1);}
    selectionsort(arr,n);
    end=clock();

    t=((double)end-start)/CLOCKS_PER_SEC;
    printf("Time is :%lf ",t);

   /* printf("Sorted elements are\n");
    for(i=0;i<n;i++)
        printf("%d\n",*(arr+i));*/
return 0;
}
