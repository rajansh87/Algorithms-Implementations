#include <bits/stdc++.h>
using namespace std;
void heapify(int arr[], int n, int i)
{
    int largest = i;
    int l = 2*i + 1;
    int r = 2*i + 2;
    if (l < n && arr[l] > arr[largest])
        largest = l;
    if (r < n && arr[r] > arr[largest])
        largest = r;
    if (largest != i)
    {
        swap(arr[i], arr[largest]);
        heapify(arr, n, largest);
    }
}
void heapSort(int arr[], int n)
{
    for (int i = n / 2 - 1; i >= 0; i--)
        heapify(arr, n, i);

    for (int i=n-1; i>=0; i--)
    {
        swap(arr[0], arr[i]);
        heapify(arr, i, 0);
    }
}
void printArray(int arr[], int n)
{
    for (int i=0; i<n; ++i)
        cout << arr[i] << " ";
    cout << "\n";
}
int main()
{
    int p;
    cin>>p;
    while(p--){
    double t;
    int n;
    cout<<"\nenter no. of elements : ";
    cin>>n;
    int arr[n];
    int i;
    clock_t start,end;
    start=clock();
    for(i=0;i<n;i++)
    {
        arr[i]=(rand()%n+1);
    }

    heapSort(arr, n);

    //cout << "Sorted array is \n";
   // printArray(arr, n);
    end=clock();

    t=((double)end-start)/CLOCKS_PER_SEC;
    printf("\n\n\tTime is :%lf ",t);
    }
    return 0;
}
