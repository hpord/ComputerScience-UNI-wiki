#include <stdio.h>
#include <stdlib.h>
#define TRUE 1
#define FALSE 0


int check(int fila, int reinas[], int n);

void imprimirT(int reinas[], int n);

void colocarReina(int fila, int reinas[], int n);

void mostrarAyuda(char * programa);

void main(int argc, char * argv[]) {
  int * reinas;
  int nreinas;
  int i;

  printf("Ingrese el numero de reinas:");
  scanf("%d", & nreinas);
  printf("\n");
  if (argc == 2)
    nreinas = atoi(argv[1]);

  if (nreinas > 0) {

    reinas = (int * ) malloc(nreinas * sizeof(int));

    for (i = 0; i < nreinas; i++)
      reinas[i] = -1;

    colocarReina(0, reinas, nreinas);

    free(reinas);

  } else {
    mostrarAyuda(argv[0]);
  }
}
int check(int fila, int reinas[], int n) {
  int i;

  for (i = 0; i < fila; i++)
    if ((reinas[i] == reinas[fila]) ||
      (abs(fila - i) == abs(reinas[fila] - reinas[i])))
      return FALSE;

  return TRUE;
}

void imprimirT(int reinas[], int n) {
  int i, j;

  for (i = 0; i < n; i++) {

    for (j = 0; j < n; j++) {

      if (reinas[i] == j)
        printf("R ");
      else
        printf("0 ");
    }

    printf(" %d %d\n", i, reinas[i]);

  }

  printf("\n");
}

void colocarReina(int fila, int reinas[], int n) {
  int ok = FALSE;

  if (fila < n) {

    for (reinas[fila] = 0; reinas[fila] < n; reinas[fila]++) {

      if (check(fila, reinas, n)) {

        colocarReina(fila + 1, reinas, n);
      }
    }

  } else {

    imprimirT(reinas, n);
  }

}

void mostrarAyuda(char * programa) {
  printf("No hay matriz");

}
