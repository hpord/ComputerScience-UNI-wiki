//---------------------------------------------------------------------------

#include <vcl.h>
#pragma hdrstop
#include<cmath>
#include <string>
using namespace std;

#include "Unit7.h"
//---------------------------------------------------------------------------
#pragma package(smart_init)
#pragma resource "*.dfm"
TfrmIndirectos *frmIndirectos;
void intercambiar(int & , int&);
void ordShell(int [],int);
void ordQuicksort(int [], int,int);
void concatenar(int[],int[],int,int[]);
int *lista;
int *izq;
int *der;
int n;
/////
int* listaAB;
int* temporal;
void mezclaLista(int[],int,int,int);
void ordMerge(int [],int , int );
void ordHeap(int [], int);
void ordRadix(int [], int);
//---------------------------------------------------------------------------
__fastcall TfrmIndirectos::TfrmIndirectos(TComponent* Owner)
	: TForm(Owner)
{
}
//---------------------------------------------------------------------------
void __fastcall TfrmIndirectos::btnSalirClick(TObject *Sender)
{
    frmIndirectos->Close();
}
//---------------------------------------------------------------------------
void __fastcall TfrmIndirectos::btnLimpiarClick(TObject *Sender)
{
    lstLista->Clear();
	lstListaO->Clear();
}
//---------------------------------------------------------------------------
void __fastcall TfrmIndirectos::txtNKeyPress(TObject *Sender, System::WideChar &Key)

{
	if (Key==VK_RETURN) {
		   lstLista->Items->Add(txtN->Text);
		   txtN->Text="";
	}
}
//---------------------------------------------------------------------------
void __fastcall TfrmIndirectos::btnCrearClick(TObject *Sender)
{
    n=lstLista->Items->Count;
	lista=new int[n];
	for (int i=0; i < n; i++) {
	   lista[i]=StrToInt(lstLista->Items->Strings[i]);
	}
}
//---------------------------------------------------------------------------
void __fastcall TfrmIndirectos::btnShellClick(TObject *Sender)
{
	btnCrearClick(Sender);
	ordShell(lista,n);
	lstListaO->Clear();
	for (int i=0; i < n; i++) {
	   lstListaO->Items->Add(lista[i]);
	}
}
void intercambiar(int &x,int &y)
{
	int aux=x;
	x=y;
	y=aux;
}
void ordShell(int a[], int n)
{
	int salto,i,j,k;
	bool desorden;
	salto=n/2;
	desorden=true;
	while (desorden) {
		if (salto==1) desorden=false;
		for (j = 0; j < n ; j++) {
			for (i = j; i < n & (i+salto)<n; i++) {
				if(a[i]>a[i+salto])
				{
					intercambiar(a[i],a[i+salto]);
					if (salto==1) desorden=true;
				}
			}
		}
		salto=salto/2;
		if (salto==0) {
			salto=1;
		}
	 }
}
void ordQuicksort(int a[], int primero, int ultimo)
{
   int i, j, central;
   double pivote;
   central = (primero + ultimo)/2;
   pivote = a[central];
   i = primero;
   j = ultimo;
   do {
		while (a[i] < pivote) i++;
		while (a[j] > pivote) j--;
		if (i <= j)
		{
			intercambiar(a[i], a[j]);
			i++;
			j--;
		}
	}while (i <= j);
	if (primero < j)
		ordQuicksort(a, primero, j);
	if (i < ultimo)
		ordQuicksort(a, i, ultimo);
}
//---------------------------------------------------------------------------
void __fastcall TfrmIndirectos::btnQuickSortClick(TObject *Sender)
{
	btnCrearClick(Sender);
	ordQuicksort(lista,0,n-1);
	lstListaO->Clear();
	for (int i=0; i < n; i++) {
	   lstListaO->Items->Add(lista[i]);
	}
}
//---------------------------------------------------------------------------

void __fastcall TfrmIndirectos::btnMezclarClick(TObject *Sender)
{
	int nA, nB, i,j;
	nA=mmoA->Lines->Count;
	nB=mmoB->Lines->Count;
	n=nA+nB;
	listaAB=new int[nA+nB];
	for (i = 0; i < nA; i++) {
	   listaAB[i]=StrToInt(mmoA->Lines->Strings[i]);
	}
	for (j = 0; j< nB; j++) {
	   listaAB[j+i]=StrToInt(mmoB->Lines->Strings[j]);
	}
	//Llama a la funcion Mezclar
	mezclaLista(listaAB,0,nA-1,nA+nB-1);
	void mezclaLista(int a[],int Izq,int Centro,int Der);
	for (i = 0; i < nA+nB; i++) {
		 mmoAB->Lines->Add(listaAB[i]);
	}
}
void mezclaLista(int a[],int Izq,int Centro,int Der)
{
	temporal=new int [n];
	int i,j,k;
	i=k=Izq;
	j=Centro+1;
	//Compara y copia el menor al temporal
	while(i<=Centro && j<=Der)
	{
		if (a[i]<=a[j]) {
		   temporal[k]=a[i];
		   k++;
		   i++;
		}else{
		   temporal[k]=a[j];
		   k++;
		   j++;
		}
	}
	//Lo que sobra se copia al final del temporal
	while (i<=Centro)
	{
		temporal[k++]=a[i++];
	}
		while (j<=Der)
	{
		temporal[k++]=a[j++];
	}
	//Copia el temporal al vector a
	for(k=Izq; k<=Der;k++)
		a[k]=temporal[k];
}
//---------------------------------------------------------------------------

void __fastcall TfrmIndirectos::btnMergeClick(TObject *Sender)
{
	btnCrearClick(Sender);
	ordMerge(lista,0,n-1);
	lstListaO->Clear();
	for (int i=0; i < n; i++) {
	   lstListaO->Items->Add(lista[i]);
	}
}
void ordMerge(int a[],int Izq, int Der)
{
  int Centro;
  if (Izq<Der) {
	 Centro=(Izq+Der)/2;
	 ordMerge(a,Izq,Centro);
	 ordMerge(a,Centro+1,Der);
	 mezclaLista(a,Izq,Centro,Der);
  }
}
//---------------------------------------------------------------------------

void __fastcall TfrmIndirectos::btnHeapClick(TObject *Sender)
{
	btnCrearClick(Sender);
	ordHeap(lista, n);
	lstListaO->Clear();
	for (int i=0; i < n; i++) {
	   lstListaO->Items->Add(lista[i]);
	}
}

void ordHeap(int a[], int n){

   // Ultimo padre i=(n-1)/2 , donde n es el número de elementos
   //Hijo izquierdo(i) = 2i + 1
   //Hijo derecho(i) = 2i + 2

   bool interruptor = true;
   int i, hd, hi, c=0;

   while(n>1){
	   bool interruptor = true;
	   i = ((n-1)/2); //posición del primer padre
	   while(interruptor){ // Realiza una pasada


			if (i<0) {
				   interruptor=false;     //Termina la pasada
				   intercambiar(a[0], a[n-1]); //al terminar intercambiar el primer con el último elemento
			}else{
				//si todavia hay padres a la izquierda entonces continua
				hi=2*i+1;//Indice del hijo izquierdo
				hd=2*i+2;//Indice del hijo derecho
				if (hi<n) { //si tiene hijo izquierdo
					if (hd<n) { // Si tiene el hijo derecho
						if (a[hd]>a[i] && a[hd]>=a[hi]) {
							intercambiar(a[i], a[hd]);
						}else if (a[hi]>a[i] && a[hi]>=a[hd]) {
							intercambiar(a[i], a[hi]);
							  }
					}else{ // No tiene hijo derecho, pero si izquierdo
						if (a[hi]>a[i]) {
							intercambiar(a[i], a[hi]);
						}
					}
				}

			}
			i--;
	   }
	   n--;
   }


}
//---------------------------------------------------------------------------

void __fastcall TfrmIndirectos::btnRadixClick(TObject *Sender)
{
	btnCrearClick(Sender);
	ordRadix(lista, n);
	lstListaO->Clear();
	for (int i=0; i < n; i++) {
	   lstListaO->Items->Add(lista[i]);
	}
}

void ordRadix(int a[], int n){

	//Vec.resize(10);
	int indices[10] {}, contador[10][25] {} ;
	int temp , m=0;

	int pasadas=0;

	//Obtenemos la cantidad de digitos (pasadas) de el mayor elemento de nuestro arreglo
	for (int i = 0, temporal; i < n; i++) {
		 temporal = log10(a[i]) + 1;     //Obtenemos la cantidad de digitos de un número
		 if (temporal>pasadas) {
			pasadas=temporal;
		 }
	}


	for(int i=0;i<pasadas;i++){   // for sobre las pasadas
		int indices[10] {}, contador[10][25] {} ; //Inicializamos los arreglos a cero

		for(int j=0;j<n;j++){
			  temp= (int)(a[j]/pow(10,i))%10;  //Seleccionaremos la fila temporal a la que vamos a añadir
			  //Añadimos elementos una fila, y aumentamos el contador de acuerdo a la fila a la que
			  //le añadimos
			  contador[temp][indices[temp]] = a[j];
			  indices[temp]+=1;
		}


        //Ahora actualizaremos el vector por cada pasada que se itere
	   for(int k=0;k<10;k++)
	   {
		 //Nos centraremos en solo las filas de la matriz en las que hemos apilado elementos
		 if(indices[k]!=0){
			for(int l=0;l<indices[k];l++){
				//intercambiamos los vectores
				intercambiar(a[m], contador[k][l]);
				m++;

			}
		 }
	   }

		m=0; //reiniciamos el contador para la siguiente pasada
	}
}
//---------------------------------------------------------------------------

