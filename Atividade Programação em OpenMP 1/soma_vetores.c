#include <stdio.h>
#include <stdlib.h>
#include <omp.h>
#include <time.h>

#define N 10 // Tamanho dos vetores

// Função que calcula a soma dos elementos de um vetor
int calculaArray(int *array, int size) {
    int soma = 0;
    for (int i = 0; i < size; i++) {
        soma += array[i];
    }
    return soma;
}

void mostrarValoresArray(int *array, int size) {
    printf("Array: ");
    for (int i = 0; i < size; i++) {
        printf("%d ", array[i]);
    }
    printf("\n");
}

int main() {
    int *array1 = (int*)malloc(N * sizeof(int)); 
    int *array2 = (int*)malloc(N * sizeof(int));
    int i;
    int processo1, processoOpenMP1, processo2, processoOpenMP2, resultFinal, resultFinalOpenMP2;
    clock_t start_time, end_time;

    srand(1); // Seed aleatória
    for (i = 0; i < N; i++) {
        array1[i] = rand() % 100;
        array2[i] = rand() % 100;
    }

    printf("Array1 antes da soma:\n");
    mostrarValoresArray(array1, N);
    printf("Array2 antes da soma:\n");
    mostrarValoresArray(array2, N);
   
    // Medindo o tempo para a versão sem OpenMP
    start_time = clock();
    processo1 = calculaArray(array1, N);
    processo2 = calculaArray(array2, N);
    end_time = clock();
    resultFinal = processo1 + processo2;
    printf("Versão sem OpenMP: soma da thread 1 (%d), com a thread 2 (%d) = %d\n", processo1, processo2, resultFinal);
    printf("Tempo de processamento COM OpenMP: %f segundos\n", (double)(end_time - start_time) / CLOCKS_PER_SEC);

    // Medindo o tempo para a versão com OpenMP
    start_time = clock();
    #pragma omp parallel sections
    {
        #pragma omp section
        {
            processoOpenMP1 = calculaArray(array1, N);
        }
        #pragma omp section
        {
            processoOpenMP2 = calculaArray(array2, N);
        }
    }
    end_time = clock();
    resultFinal = processoOpenMP1 + processoOpenMP2;
    printf("Versão OpenMP: soma da thread 1 (%d), com a thread 2 (%d) = %d\n", processoOpenMP1, processoOpenMP2, resultFinalOpenMP2);
    printf("Tempo de processamento SEM OpenMP: %f segundos\n", (double)(end_time - start_time) / CLOCKS_PER_SEC);
    
    free(array1);
    free(array2);
    return 0;
}
