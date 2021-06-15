//---------------------------------------------------------------------------

#include <vcl.h>
#pragma hdrstop

#include "Unit6.h"
//---------------------------------------------------------------------------
#pragma package(smart_init)
#pragma resource "*.dfm"
TORDENAMIENTO *ORDENAMIENTO;

void intercambiar(int &, int &);
void ordIntercambio(int [], int );
void ordSeleccion(int [], int);
void ordInsercion(int [], int);
void ordBurbuja(int [], int);
int *lista;
int n;
//---------------------------------------------------------------------------
__fastcall TORDENAMIENTO::TORDENAMIENTO(TComponent* Owner)
	: TForm(Owner)
{
}
//---------------------------------------------------------------------------


void __fastcall TORDENAMIENTO::btnSalirClick(TObject *Sender)
{
    ORDENAMIENTO->Close();
}
//---------------------------------------------------------------------------

void __fastcall TORDENAMIENTO::btnAnadirClick(TObject *Sender)
{
    lstLista->Items->Add(txtNumero->Text);
}


void __fastcall TORDENAMIENTO::txtNumeroKeyPress(TObject *Sender, System::WideChar &Key)

{
	if (Key == VK_RETURN) {
	 btnAnadirClick(Sender);
	 txtNumero->Text="";
	}
}
void intercambiar(int &x, int &y){
	int aux=x;
	x=y;
	y=aux;
}

//---------------------------------------------------------------------------

void __fastcall TORDENAMIENTO::btnLimpiarClick(TObject *Sender)
{
	lstLista->Clear();
	lstListaOrd->Clear();
}
//---------------------------------------------------------------------------

void __fastcall TORDENAMIENTO::btnIntercambioClick(TObject *Sender)
{
	btnCrearClick(Sender);
	ordIntercambio(lista, n);
	lstListaOrd->Clear();
	for (int i = 0; i < n; i++) {
		lstListaOrd->Items->Add(lista[i]);
	}
}
//---------------------------------------------------------------------------

void __fastcall TORDENAMIENTO::btnCrearClick(TObject *Sender)
{
	n=lstLista->Items->Count;
	lista = new int[n];
	for (int i=0; i < n; i++) {
		lista[i] = StrToInt(lstLista->Items->Strings[i]);
	}

}


//---------------------------------------------------------------------------

void __fastcall TORDENAMIENTO::btnSeleccionClick(TObject *Sender)
{
  btnCrearClick(Sender);
  ordSeleccion(lista, n);
  lstListaOrd->Clear();
	for (int i = 0; i < n; i++) {
		lstListaOrd->Items->Add(lista[i]);
	}
}
//---------------------------------------------------------------------------

void __fastcall TORDENAMIENTO::btnInsercionClick(TObject *Sender)
{
  btnCrearClick(Sender);
  ordInsercion(lista, n);
  lstListaOrd->Clear();
	for (int i = 0; i < n; i++) {
		lstListaOrd->Items->Add(lista[i]);
	}
}
//---------------------------------------------------------------------------

void __fastcall TORDENAMIENTO::btnBurbujaClick(TObject *Sender)
{
  btnCrearClick(Sender);
  ordBurbuja(lista, n);
  lstListaOrd->Clear();
	for (int i = 0; i < n; i++) {
		lstListaOrd->Items->Add(lista[i]);
	}
}

//---------------------------------------------------------------------------
void ordIntercambio(int a[], int n){
	int i, j;
	for (i=0; i < n-1; i++) {
		for (j = i+1; j < n; j++) {
			 if(a[i]>a[j]){
			 intercambiar(a[i], a[j]);
			 }
		}
	}
 }

 void ordSeleccion(int a[], int n){

	int indiceMenor, i, j;
	for (i = 0; i < n-1; i++) {
		 indiceMenor = i;
		 for (j = i+1; j < n; j++) {
			if (a[j]<a[indiceMenor]) {
				indiceMenor=j;
			}

		 }
		 if (i!=indiceMenor) {
				intercambiar(a[i], a[indiceMenor]);
			}
	}
}

void ordInsercion(int a[], int n){
	int i, j, aux;

	for (i = 1; i < n; i++) {
		j=i;
		aux=a[i];

		while(j>0 && aux < a[j-1]){
			a[j] = a[j-1];
			j--;
		}
		a[j]=aux;
	}

}

void ordBurbuja(int a[], int n){
	bool interruptor = true;
	int pasada, j;
	for (pasada = 0; pasada < n-1 && interruptor; pasada++) {
		interruptor = false;
		for (j = 0; j < n-pasada-1; j++) {
			if (a[j] > a[j+1]) {
			   interruptor = true;
			   intercambiar(a[j], a[j+1]);
			}
		}
	}
}
//---------------------------------------------------------------------------

