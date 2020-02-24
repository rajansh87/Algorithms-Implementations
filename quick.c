#include <stdio.h>
#include <stdlib.h>
#include<conio.h>
#include<time.h>
void swap(int *x,int *y)
{
   int temp;
   temp = *x;
   *x = *y;
   *y = temp;
}

int choose_pivot(int i,int j )
{
   return((i+j) /2);
}

void quicksort(int list[],int m,int n)
{
   int key,i,j,k;
   if( m < n)
   {
      k = choose_pivot(m,n);
      swap(&list[m],&list[k]);
      key = list[m];
      i = m+1;
      j = n;
      while(i <= j)
      {
         while((i <= n) && (list[i] <= key))
                i++;
         while((j >= m) && (list[j] > key))
                j--;
         if( i < j)
                swap(&list[i],&list[j]);
      }
	  // swap two elements
      swap(&list[m],&list[j]);
	  // recursively sort the lesser list
      quicksort(list,m,j-1);
      quicksort(list,j+1,n);
   }
}
void printlist(int list[],int n)
{
   int i;
   for(i=0;i<n;i++)
      printf("%d\t",list[i]);
}

void main()
{
   int list[100000],n;
double t;
   int i = 0;
	printf("Enter no. of elements\n");
	scanf("%d",&n);
	clock_t start,end;
    start=clock();
   for(i = 0; i <n; i++ )
{
	    list[i]=(rand()%n+1);
   }



   quicksort(list,0,n-1);
end=clock();

    t=((double)end-start)/CLOCKS_PER_SEC;
    printf("Time is :%lf ",t);
  /*
   printf("The list after sorting using quicksort algorithm:\n");
   printlist(list,n);*/
}
