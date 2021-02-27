//---------------------------------------------------------------------------

#include <vcl.h>
#pragma hdrstop

#include "Unit7.h"
//---------------------------------------------------------------------------
#pragma package(smart_init)
#pragma resource "*.dfm"
TfrmOrdenamiento *frmOrdenamiento;
void ordBurbuja(int [], int[] , int);
void ordBurbujaLetras(int [], String [], int [], int);
void intercambiar(int &, int &);
String Aleatorios [5][6];
int primerosNumeros [6];
String primerasLetras [6];
//---------------------INDICE------------------------------------------------
//AUTOR: SÁNCHEZ SAUÑE CRISTHIAN WIKI
//
//0.- LLENADO DE LOS LISTBOX CON NÚMEROS ALEATORIOS
//1.- ORDENAMIENTO SIN TENER EN CUENTA LA LETRA
//2.- ORDENAMIENTO TENIENDO EN CUENTA LA LETRA
//3.- MÉTODOS DE ORDENAMIENTO USADOS
//
//NOTA: Incluso sin tener en cuenta la letras, el algoritmo de la
//burbuja da un arreglo ya ordenado como si se hubiesen tenido en cuenta las letras.
//Razón por la que todas las opciones que da el botón 'Ordenar por 1er Número' ya no
//necesitan ser ordenados por la letra, tenemos que forzar un caso de prueba.
//      "DESCOMENTE EL CASO FORZADO DE PRUEBA PARA PROBAR EL SEGUNDO BOTÓN"
//-----------------------------------------------------------------------------


//---------------------------------------------------------------------------
__fastcall TfrmOrdenamiento::TfrmOrdenamiento(TComponent* Owner)
	: TForm(Owner)
{
}
//---------------------------------------------------------------------------
void __fastcall TfrmOrdenamiento::btnSalirClick(TObject *Sender)
{
   frmOrdenamiento->Close();
}



//---------------------------------------------------------------------------
// 0.- LLENADO DE LOS LISTBOX CON NÚMEROS ALEATORIOS
//---------------------------------------------------------------------------

void __fastcall TfrmOrdenamiento::btnGenerarClick(TObject *Sender)
{
  //Limpiamos la lista
  lbA1->Clear();
  lbA2->Clear();
  lbA3->Clear();
  lbA4->Clear();
  lbA5->Clear();
  lbA6->Clear();

  // Primer caso de prueba (COMENTAR PARA PROBAR EL SEGUNDO BOTÓN
  Aleatorios[0][0] = "A";
  Aleatorios[0][1] = "B";
  Aleatorios[0][2] = "C";
  Aleatorios[0][3] = "D";
  Aleatorios[0][4] = "E";
  Aleatorios[0][5] = "F";

  //Segundo caso de prueba (DESCOMENTAR PARA USAR EL SEGUNDO BOTÓN)
  //Aleatorios[0][0] = "B";
  //Aleatorios[0][1] = "A";
  //Aleatorios[0][2] = "F";
  //Aleatorios[0][3] = "E";
  //Aleatorios[0][4] = "C";
  //Aleatorios[0][5] = "F";


  // Creando los números aleatorios
  for (int i=1; i < 5; i++) {
	 for (int j=0; j < 6; j++) {
		 Aleatorios[i][j] = (String)(rand()%(5-0+1)+0);
	 }
  }

  // Guardando en los listBox
  for (int i=0; i < 5; i++) {
		 lbA1->Items->Add(Aleatorios[i][0]);
		 lbA2->Items->Add(Aleatorios[i][1]);
		 lbA3->Items->Add(Aleatorios[i][2]);
		 lbA4->Items->Add(Aleatorios[i][3]);
		 lbA5->Items->Add(Aleatorios[i][4]);
		 lbA6->Items->Add(Aleatorios[i][5]);
	 }
  }


// ---------------------------------------------------------------------------
//1. ORDENAMIENTO SIN TENER EN CUENTA LA LETRA
// ---------------------------------------------------------------------------


void __fastcall TfrmOrdenamiento::btnOrdenarNumClick(TObject *Sender)
{

  //Limpiamos la lista
  lbB1->Clear();
  lbB2->Clear();
  lbB3->Clear();
  lbB4->Clear();
  lbB5->Clear();
  lbB6->Clear();

  for (int i = 0; i < 6; i++) {
	   primerosNumeros[i] = StrToInt(Aleatorios[1][i]);
  }

  int indices[6];

	for (int i = 0; i < 6; i++) {
	  indices[i]=i;
	}
	ordBurbuja(primerosNumeros, indices, 6);

  // Guardando en los listBox
  for (int i=0; i < 5; i++) {
		 lbB1->Items->Add(Aleatorios[i][indices[0]]);
		 lbB2->Items->Add(Aleatorios[i][indices[1]]);
		 lbB3->Items->Add(Aleatorios[i][indices[2]]);
		 lbB4->Items->Add(Aleatorios[i][indices[3]]);
		 lbB5->Items->Add(Aleatorios[i][indices[4]]);
		 lbB6->Items->Add(Aleatorios[i][indices[5]]);
	 }
  }


// ---------------------------------------------------------------------------
//2. ORDENAMIENTO TENIENDO EN CUENTA LA LETRA
// ---------------------------------------------------------------------------

void __fastcall TfrmOrdenamiento::btnOrdenarLetraClick(TObject *Sender)
{
//Limpiamos la lista
  lbB1->Clear();
  lbB2->Clear();
  lbB3->Clear();
  lbB4->Clear();
  lbB5->Clear();
  lbB6->Clear();


  //Obtenemos los primeros números sin ordenar e inicializamos los índices
  int indices [6], indicesLetras[6], primerosNumerosOrdenados[6];
  for (int i = 0; i < 6; i++) {
	   primerosNumeros[i] = StrToInt(Aleatorios[1][i]);
	   indices[i]=i;
  }

  //Ordenamos los primeros números, para luego pasarlos como argumento a
  // "ordBurbujaLetras"
  ordBurbuja(primerosNumeros, indices, 6);

  //Obtenemos los primeros números ya ordenados, las primeras letras sin ordenar y
  //hacemos una copia de índices en indiceLetras (para no tener problemas después)
  for (int i = 0; i < 6; i++) {
	   primerosNumerosOrdenados[i] = StrToInt(Aleatorios[1][indices[i]]);
	   primerasLetras[i] = Aleatorios[0][indices[i]];
	   indicesLetras[i] = indices[i];
  }

  // Ordenamos en función de las letras, para lo cual le pasamos los
  // primeros números ya ordenados como base, para empezar a hacer las comparaciones
  ordBurbujaLetras(primerosNumerosOrdenados, primerasLetras, indicesLetras, 6);

  // Guardando en los listBox
  for (int i=0; i < 5; i++) {
		 lbB1->Items->Add(Aleatorios[i][indicesLetras[0]]);
		 lbB2->Items->Add(Aleatorios[i][indicesLetras[1]]);
		 lbB3->Items->Add(Aleatorios[i][indicesLetras[2]]);
		 lbB4->Items->Add(Aleatorios[i][indicesLetras[3]]);
		 lbB5->Items->Add(Aleatorios[i][indicesLetras[4]]);
		 lbB6->Items->Add(Aleatorios[i][indicesLetras[5]]);
	 }
  }



//----------------------------------------------------------------------
//3. MÉTODOS DE ORDENAMIENTO USADOS
//----------------------------------------------------------------------

void intercambiar(int &x, int &y){
	int aux=x;
	x=y;
	y=aux;
}

 void intercambiarLetras(String &x, String &y){
	String aux=x;
	x=y;
	y=aux;
}

void ordBurbuja(int a[], int indices[], int n){
	bool interruptor = true;
	int pasada, j;
	for (pasada = 0; pasada < n-1 && interruptor; pasada++) {
		interruptor = false;
		for (j = 0; j < n-pasada-1; j++) {
			if (a[j] > a[j+1]) {
			   interruptor = true;
			   intercambiar(a[j], a[j+1]);
			   intercambiar(indices[j], indices[j+1]);
			}
		}
	}
}

void ordBurbujaLetras(int a[], String letras[], int indicesLetras[], int n){
	bool interruptor = true;
	int pasada, j;
	for (pasada = 0; pasada < n-1 && interruptor; pasada++) {
		interruptor = false;
		for (j = 0; j < n-pasada-1; j++) {
			if(a[j] == a[j+1]){      //en caso tengan la misma cantidad, pasamos
									 // a ordenar en funcion de sus letras
			  if (letras[j] > letras[j+1]) { //Comparamos dos String (letras) en función
											 //de su valor ASCII
				 interruptor = true;
				 //Intercambiamos la posición de las filas ordenadas en función de las letras,
				 //Previamente ya obtuvimos el orden sin tomar en cuenta las letras
				 intercambiar(indicesLetras[j], indicesLetras[j+1]);
			  }
			}
		}
	}
}

//---------------------------------------------------------------------------
