#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include<iostream>
using namespace std;
void Table(int a[][99], int k) {
  int i, j, s, t, m = 1;
  int n=pow(2,k);
  for (i = 1; i <= n; i++){
  
    a[1][i] = i;}

  for (s = 1; s <= k; s++) {
    n = n / 2;
    for (t = 1; t <= n; t++) {

      for (i = m + 1; i <= 2 * m; i++) {

        for (j = m + 1; j <= 2 * m; j++) {
          a[i][j + (t - 1) * m * 2] = a[i - m][j + (t - 1) * m * 2 - m];
          a[i][j + (t - 1) * m * 2 - m] = a[i - m][j + (t - 1) * m * 2];
        }
      }
    }
    m = m * 2;
  }
}

int main() {
	int opt;
  cout<<"Ingrese opcion:"<<endl;
  cout<<"1) 2^k"<<endl;
  cout<<"2) impar"<<endl;
  cin>>opt;
 if(opt==1){
 int n,i,j,k;
         printf("Ingresa el k:");
    cin>>k;
  int table[99][99];
    n=pow(2,k);
  Table(table, k);
  for (i = 1; i <= n; i++) {
    for (j = 1; j <= n; j++)
      printf("%d ", table[i][j]);
    cout<<endl;
  }}
  else{
  	int n,i,j,k;
         printf("Please enter k:");
    scanf("%d",&k);
  int table[99][99];
    n=pow(2,k);
  Table(table, k);
  for (i = 1; i <= n-1; i++) {
    for (j = 1; j <= n; j++){
	if(table[i][j]==n){
		cout<<0;
	}
	else{
		cout<<table[i][j];
	}
     }
    cout<<endl;
  }}
  return 0;
}
