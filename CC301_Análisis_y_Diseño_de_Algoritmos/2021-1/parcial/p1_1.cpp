#include <stdio.h>
#include <iostream>
#include <stdlib.h>
using namespace std;
int merge(int arr1[], int arr2[], int arr3[], int m, int n) {
  int i, j, k;
  i = j = k = 0;
  for (i = 0; i < m && j < n;) {
    if (arr1[i] < arr2[j]) {
      arr3[k] = arr1[i];
      k++;
      i++;
    } else {
      arr3[k] = arr2[j];
      k++;
      j++;
    }
  }
  while (i < m) {
    arr3[k] = arr1[i];
    k++;
    i++;
  }
  while (j < n) {
    arr3[k] = arr2[j];
    k++;
    j++;
  }
}
int main() {
//dimensiones
	int n=4,m=5,q=5;
	//elementos
	int arr1[m]={1,3,7};
	int arr2[n]={2,4,5,6};
	//int arr3[q]={5,8,10,11};
	//array resultante
  	int arr3[m + n+q];
  	int i;
  	
  	merge(arr1, arr2, arr3, m, n);
  	cout<<"Array 1 :"<<endl;
  		for(int i=0;i<n-1;i++){
		cout<<arr1[i]<<" ";
	}
	cout<<endl;
  	cout<<"Array 2 : "<<endl;
  		for(int i=0;i<m-1;i++){
		cout<<arr2[i]<<" ";
	}
	cout<<endl;
	cout<<"Lista merge ordenada:"<<endl;
	for(int i=0;i<n+m-2;i++){
		cout<<arr3[i]<<" ";
	}
	cout<<endl;
	return 0;
	

}
