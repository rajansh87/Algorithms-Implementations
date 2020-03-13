#include <stdio.h>
#define NUM_LINE 2
#define NUM_STATION 5

int min(int a, int b) { return a < b ? a : b; }

int carAssembly(int a[][NUM_STATION], int t[][NUM_STATION], int *e, int *x)
{
    int T1[NUM_STATION], T2[NUM_STATION], i;

    T1[0] = e[0] + a[0][0];
    T2[0] = e[1] + a[1][0];

    for (i = 1; i < NUM_STATION; ++i)
    {
        T1[i] = min(T1[i-1] + a[0][i], T2[i-1] + t[1][i] + a[0][i]);
        T2[i] = min(T2[i-1] + a[1][i], T1[i-1] + t[0][i] + a[1][i]);
    }
    printf("%d\t%d\n",T1[NUM_STATION-1] + x[0],T2[NUM_STATION-1] + x[1]);
    return min(T1[NUM_STATION-1] + x[0], T2[NUM_STATION-1] + x[1]);
}

int main()
{
    int a[][NUM_STATION] = {{7, 9, 3, 4, 8},
                {8, 5, 6, 4, 5}};
    int t[][NUM_STATION] = {{0, 2, 1, 2, 2},
                {0, 2, 3, 1, 3}};
    int e[] = {2, 4}, x[] = {3, 6};

    printf("%d", carAssembly(a, t, e, x));

    return 0;
}
