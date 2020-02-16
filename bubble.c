#include<stdio.h>
#include<stdlib.h>
#include<time.h>
int main()
{
    int i,j,temp,n;
    int *p;
    double t;
    printf("Enter value of n: ");
    scanf("%d",&n);
    clock_t start,end;
    start=clock();

    p=(int*)malloc(n*sizeof(int));

    for(i=0;i<n;i++)
        {p[i]=(rand()%n+1);}
    for(i=0;i<n;i++)
    {
        for(j=i+1;j<n;j++)
        {
            if(p[i]>p[j])
            {
                temp=p[i];
                p[i]=p[j];
                p[j]=temp;
            }
        }
    }
    end=clock();

    t=((double)end-start)/CLOCKS_PER_SEC;
    printf("Time is :%lf ",t);
   /* printf("sorted array is :\n");
    for(i=0;i<n;i++)
        printf("%d\n",p[i]);
    free(p);*/


    return 0;
}
