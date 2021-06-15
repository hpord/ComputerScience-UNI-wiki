#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int max(int,int);
int *multiplicamatriz(int *,int **,int); // Función recursiva que multiplica matrices
int *suma(int *,int **,int); // suma de matrices
int *resta(int *,int **,int);// Resta de matrices
void libera(int **,int); // Libera memoria

int main()
{
   int *mapa1,mapa2,*sol;
   int f1,c1,f2,c2,a,b,m,m1;

   scanf(" %d %d",&f1,&c1); // Tamaño de la primera matriz
   scanf(" %d %d",&f2,&c2); // Tamaño de la segunda matriz
   m1=max(f1,max(c1,max(f2,c2)));

   for(m=1;m<m1;m*=2); // El tamaño de las matrices cuadradas a multiplicar
   //debe ser de la forma 2k, si no se completan con ceros.

   mapa1=(int **)malloc(sizeof(int *)*m); // Se crea la primera matriz
   for(a=0;a<m;a++)
   {
      mapa1[a]=(int *)malloc(sizeof(int)*m);
      memset(mapa1[a],0,sizeof(int)*m);
    }
   for(a=0;a<f1;a++) // Se cogen los datos de la primera matriz.
      for(b=0;b<c1;b++)
         scanf(" %d",&mapa1[a][b]);

   mapa2=(int **)malloc(sizeof(int *)*m); // Se crea la sedunda matriz.
   for(a=0;a<m;a++)
   {
      mapa2[a]=(int *)malloc(sizeof(int)*m);
      memset(mapa2[a],0,sizeof(int)*m);
    }
   for(a=0;a<f2;a++) // Se cogen los datos de la segunda matriz.
      for(b=0;b<c2;b++)
         scanf(" %d",&mapa2[a][b]);

   sol=multiplicamatriz(mapa1,mapa2,m); // Se multiplican.

   for(a=0;a<f1;a++) // Se imprime el resultado.
   {
      for(b=0;b<c2;b++)
         printf("%d ",sol[a][b]);
      printf("\n");
    }

   return(0);
 }

int max(int a,int b)
{
   return((a>b)?a:b);
 }

int **multiplicamatriz(int **mapa1,int **mapa2,int num)
{
   int *sol,M[8],f1,f2,aux,*aux2;
   int *A[2][2],B[2][2],*C[2][2];
   int a,q,w,r;

   sol=(int **)malloc(sizeof(int *)*num);
   for(a=0;a<num;a++)
      sol[a]=(int *)malloc(sizeof(int)*num);

   if(num==1)
   {
      sol[0][0]=mapa1[0][0]*mapa2[0][0];
      return(sol);
    }
// Crear las submatrices de A y B.
   for(q=0;q<2;q++)
   {
      for(w=0;w<2;w++)
      {
         A[q][w]=(int *)malloc(sizeof(int *)(num/2));
         for(a=0;a<num/2;a++)
         {
            A[q][w][a]=(int )malloc(sizeof(int)(num/2));
            for(r=0;r<num/2;r++)
               A[q][w][a][r]=mapa1[a+(num/2)*q][r+(num/2)*w];
          }

         B[q][w]=(int *)malloc(sizeof(int *)(num/2));
         for(a=0;a<num/2;a++)
         {
            B[q][w][a]=(int )malloc(sizeof(int)(num/2));
            for(r=0;r<num/2;r++)
             B[q][w][a][r]=mapa2[a+(num/2)*q][r+(num/2)*w];
          }
       }
    }
// Hallar las matrices M.
   f1=resta(A[0][1],A[1][1],num/2);
   f2=suma(B[1][0],B[1][1],num/2);
   M[1]=multiplicamatriz(f1,f2,num/2);
   libera(f1,num/2);
   libera(f2,num/2);

   f1=suma(A[0][0],A[1][1],num/2);
   f2=suma(B[0][0],B[1][1],num/2);
   M[2]=multiplicamatriz(f1,f2,num/2);
   libera(f1,num/2);
   libera(f2,num/2);

   f1=resta(A[0][0],A[1][0],num/2);
   f2=suma(B[0][0],B[0][1],num/2);
   M[3]=multiplicamatriz(f1,f2,num/2);
   libera(f1,num/2);
   libera(f2,num/2);

   f1=suma(A[0][0],A[0][1],num/2);
   f2=B[1][1];
   M[4]=multiplicamatriz(f1,f2,num/2);
   libera(f1,num/2);

   f1=A[1][1];
   f2=resta(B[0][1],B[1][1],num/2);
   M[5]=multiplicamatriz(f1,f2,num/2);
   libera(f2,num/2);

   f1=A[1][1];
   f2=resta(B[1][0],B[0][0],num/2);
   M[6]=multiplicamatriz(f1,f2,num/2);
   libera(f2,num/2);

   f1=suma(A[1][0],A[1][1],num/2);
   f2=B[0][0];
   M[7]=multiplicamatriz(f1,f2,num/2);
   libera(f1,num/2);

// Hallar las submatrices de C.

   C[0][0]=suma(M[1],M[2],num/2);
   aux=C[0][0];
   C[0][0]=resta(C[0][0],M[4],num/2);
   aux2=C[0][0];
   C[0][0]=suma(C[0][0],M[6],num/2);
   libera(aux,num/2);
   libera(aux2,num/2);

   C[0][1]=suma(M[4],M[5],num/2);

   C[1][0]=suma(M[6],M[7],num/2);

   C[1][1]=resta(M[2],M[3],num/2);
   aux=C[1][1];
   C[1][1]=suma(C[1][1],M[5],num/2);
   aux2=C[1][1];
   C[1][1]=resta(C[1][1],M[7],num/2);
   libera(aux,num/2);
   libera(aux2,num/2);

   for(a=1;a<=7;a++)
      libera(M[a],num/2);
// Unir las submatrices de matrices C en sol.
   for(q=0;q<num;q++)
      for(w=0;w<num;w++)
         sol[q][w]=C[q/(num/2)][w/(num/2)][q%(num/2)][w%(num/2)];
// Liberar las submatrices de A, B y C.
   for(q=0;q<2;q++)
      for(w=0;w<2;w++)
      {
         libera(A[q][w],num/2);
         libera(B[q][w],num/2);
         libera(C[q][w],num/2);
       }

   return(sol);
 }

int **suma(int **mapa1,int **mapa2,int num)
{ // sumar mapa1 y mapa2.
   int a,b;
   int **sol;
   sol=(int **)malloc(sizeof(int *)*num);
   for(a=0;a<num;a++)
   {
      sol[a]=(int *)malloc(sizeof(int)*num);
      for(b=0;b<num;b++)
         sol[a][b]=mapa1[a][b]+mapa2[a][b];
    }
   return(sol);
 }

int **resta(int **mapa1,int **mapa2,int num)
{ // Restar mapa2 de mapa1.
   int **sol;
   int a,b;
   sol=(int **)malloc(sizeof(int *)*num);
   for(a=0;a<num;a++)
   {
      sol[a]=(int *)malloc(sizeof(int)*num);
      for(b=0;b<num;b++)
         sol[a][b]=mapa1[a][b]-mapa2[a][b];
    }
   return(sol);
 }

void libera(int **mapa,int num)
{
   int a;
   for(a=0;a<num;a++) // Liberar la tabla dinámica de 2D.
      free(mapa[a]);
   free(mapa);
 }
