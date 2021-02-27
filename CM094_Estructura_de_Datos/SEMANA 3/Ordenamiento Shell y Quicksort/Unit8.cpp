//---------------------------------------------------------------------------

#include <vcl.h>
#pragma hdrstop

#include "Unit8.h"
//---------------------------------------------------------------------------
#pragma package(smart_init)
#pragma resource "*.dfm"
TfrmOrdenacionV2 *frmOrdenacionV2;
void shell(int, int []);
void Quicksort(int [],int , int  );
int n, *lista;
//---------------------INDICE------------------------------------------------
//AUTOR: SÁNCHEZ SAUÑE CRISTHIAN WIKI
//
//1.- LLENADO DEL VECTOR, BOTÓN AGREGAR, LIMPIAR LISTAS Y SALIR
//2.- BOTÓN ORDENAMIENTO SHELL Y QUICKSORT
//3.- MÉTODOS DE ORDENAMIENTO USADOS



//---------------------------------------------------------------------------
__fastcall TfrmOrdenacionV2::TfrmOrdenacionV2(TComponent* Owner)
	: TForm(Owner)
{
}
//---------------------------------------------------------------------------


//----------------------------------------------------------------------
//1.- LLENADO DEL VECTOR, BOTÓN AGREGAR. LIMPIAR LISTAS Y SALIR
//----------------------------------------------------------------------
void __fastcall TfrmOrdenacionV2::btnSalirClick(TObject *Sender)
{
   frmOrdenacionV2->Close();
}
//---------------------------------------------------------------------------
void __fastcall TfrmOrdenacionV2::bntLimpiarClick(TObject *Sender)
{
   lbLista->Clear();
   lbListaOrdenada->Clear();
}
//---------------------------------------------------------------------------
void __fastcall TfrmOrdenacionV2::btnAgregarClick(TObject *Sender)
{
  if(txtNumero->Text != ""){
	  lbLista->Items->Add(txtNumero->Text);
	  txtNumero->Text="";
	  txtNumero->SetFocus();
	}
}
//---------------------------------------------------------------------------

void __fastcall TfrmOrdenacionV2::txtNumeroKeyPress(TObject *Sender, System::WideChar &Key)

{
	if (Key == VK_RETURN) {
		 btnAgregarClick(Sender);
	}
}
//---------------------------------------------------------------------------
void __fastcall TfrmOrdenacionV2::btnCrearClick(TObject *Sender)
{
	n=lbLista->Items->Count;
	lista = new int[n];
	for (int i=0; i < n; i++) {
		lista[i] = StrToInt(lbLista->Items->Strings[i]);
	}

}
//---------------------------------------------------------------------------


//----------------------------------------------------------------------
//2.- BOTÓN ORDENAMIENTO SHELL Y QUICKSORT
//----------------------------------------------------------------------
void __fastcall TfrmOrdenacionV2::btnShellClick(TObject *Sender)
{
	btnCrearClick(Sender);
	shell( n , lista);
	lbListaOrdenada->Clear();
	for (int i = 0; i < n; i++) {
		lbListaOrdenada->Items->Add(lista[i]);
	}
}

//---------------------------------------------------------------------------
void __fastcall TfrmOrdenacionV2::btnQuicksortClick(TObject *Sender)
{

	btnCrearClick(Sender);
	Quicksort(lista, 0, n-1 );
	lbListaOrdenada->Clear();
	for (int i = 0; i < n; i++) {
		lbListaOrdenada->Items->Add(lista[i]);
	}
}

//---------------------------------------------------------------------------


//----------------------------------------------------------------------
//3. MÉTODOS DE ORDENAMIENTO USADOS
//----------------------------------------------------------------------

void shell( int n , int v[ ] )
{
   int i , j , k , salto, aux ;
   bool fin ;

   salto = n ;
   while ( salto>0 )
   {
	  salto = salto/2 ;
      do
      {
         fin = true ;
		 k  = n-salto ;
         for ( i = 0 ; i < k ; i++ )
         {
            j = i + salto ;
			if ( v[i] < v[j] ){
				aux = v[i] ;
				v[i] = v[j] ;
				v[j] = aux ;
				fin = false ;
             }
          }
       }
	   while ( !fin ) ;
    }
}

//---------------------------------------------------------------------------
void Quicksort(int A[],int izq, int der )
{
int i, j, x , aux;
i = izq;
j = der;
x = A[ (izq + der) /2 ];
    do{
        while( (A[i] < x) && (j <= der) )
        {
            i++;
        }

        while( (x < A[j]) && (j > izq) )
        {
            j--;
        }

        if( i <= j )
        {
            aux = A[i]; A[i] = A[j]; A[j] = aux;
            i++;  j--;
        }

    }while( i <= j );

    if( izq < j )
		Quicksort( A, izq, j );
	if( i < der )
		Quicksort( A, i, der );
}

//---------------------------------------------------------------------------
