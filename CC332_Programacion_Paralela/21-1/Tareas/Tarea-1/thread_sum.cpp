#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

#define MAX_NO_OF_THREADS 8
#define MAX_NO_OF_ELEMENTS 16

typedef struct arg_data {
    int thread_number;
} arg_data;

// Compartimos los datos en cada hilo para que trabajen concurrentemente
// sobre el arreglo que va a ser sumado
static int arr[MAX_NO_OF_ELEMENTS];
// Variable suma que almacenará la suma total
static long long int sum;

void* worker_sum(void* arg) {
    arg_data* current_thread_data = (arg_data*)arg;

    printf("\nEl hilo actual es el nro. : %d\n", current_thread_data->thread_number);

    int endpart = (current_thread_data->thread_number) * (MAX_NO_OF_ELEMENTS / MAX_NO_OF_THREADS);
    int startpart = endpart - (MAX_NO_OF_ELEMENTS / MAX_NO_OF_THREADS);

    printf("Aqui sumaremos desde %d hasta %d\n", arr[startpart], arr[endpart - 1]);

    long long int current_thread_sum = 0;
    for (int i = startpart; i < endpart; i++) {
        current_thread_sum += arr[i];
    }
    sum += current_thread_sum;

    return NULL;
}

int main() {
    // el arreglo consistira de los MAX_NO_OF_ELEMENTS primeros enteros,
    // desde 1 hasta MAX_NO_OF_ELEMENTS
    for (int i = 0; i < MAX_NO_OF_ELEMENTS; i++) arr[i] = i + 1;

    // objetos pthread
    pthread_t id[MAX_NO_OF_THREADS];

    // data argumento para enviar en las funciones worker
    arg_data arg_arr[MAX_NO_OF_THREADS];

    // numero total de hilos que crearemos
    int no_of_threads = MAX_NO_OF_THREADS;
    printf("\nCreando %d hilos...\n", no_of_threads);

    clock_t start, end;
    double cpu_time_taken;

    start = clock();

    int thread_no = 1;

    //creando los hilos hijo
    for (thread_no = 1; thread_no <= MAX_NO_OF_THREADS; thread_no++) {
        arg_arr[thread_no - 1].thread_number = thread_no;
        pthread_create(&id[thread_no - 1], NULL, worker_sum, &arg_arr[thread_no - 1]);
    }

    //uniendo los hilos uno por uno
    for (int i = 1; i <= MAX_NO_OF_THREADS; i++) pthread_join(id[i - 1], NULL);

    end = clock();
    cpu_time_taken = ((double)(end - start)) / CLOCKS_PER_SEC;

    printf("\nTodos los hilos hijo han finalizado su trabajo...\n");

    printf("Suma total: %lld\n", sum);

    printf("EL tiempo total para sumar todos los numeros es de %lf seg\n", cpu_time_taken);

    return 0;
}
