#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define MAX_NO_OF_ELEMENTS 16

static long long int sum;
static int arr[MAX_NO_OF_ELEMENTS];

int main() {
    for (int i = 0; i < MAX_NO_OF_ELEMENTS; i++)
        arr[i] = i + 1;

    clock_t start, end;
    double cpu_time_taken;

    start = clock();

    // sumando

    for (int i = 0; i < MAX_NO_OF_ELEMENTS; i++)
        sum += arr[i];

    end = clock();
    cpu_time_taken = ((double)(end - start)) / CLOCKS_PER_SEC;

    printf("La suma total es: %lld\n", sum);

    printf("El tiempo total es %lf\n seg", cpu_time_taken);

    return 0;
}
