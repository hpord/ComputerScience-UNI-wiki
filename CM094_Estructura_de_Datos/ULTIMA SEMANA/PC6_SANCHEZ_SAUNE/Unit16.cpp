//---------------------------------------------------------------------------

#include <vcl.h>
#pragma hdrstop

#include "Unit16.h"
//---------------------------------------------------------------------------
#pragma package(smart_init)
#pragma resource "*.dfm"
TfrmGrafo *frmGrafo;
//---------------------------------------------------------------------------
__fastcall TfrmGrafo::TfrmGrafo(TComponent* Owner)
	: TForm(Owner)
{
}
//Nuestras variables
TEdit* Cuadro[10][10];
TEdit* Dire[10][10];
int tMax=10;//Cantidad maxima de nodos
int nNodos;//Cantidad de nodos de la lista directorio
class nodo
{
	public:
	class arco; //Contiene el destino del arco y la direccion del siguiente arco
				//El inicio es este nodo (self)
	String nombre; //nombre del nodo
	nodo* sgte; //puntero al siguiente nodo del directorio
	arco* ady; //puntero al primer arco de la lista de arcos del nodo
	nodo* p; //puntero al primer nodo de la lista nodos del directorio
	void insertarNodo(int); //Inserta un nodo al directorio
	//void mostrarGrafo(); //Muestra el grafo
	void insertarArco(String, String, int, int); //Solicita los nombres del nodo inicial y final
						//Si los encuentra llama a agregarArco() pra crear el arco
	void agregarArco(nodo*,nodo*,arco*,int, int); //Crea el arco con los datos enviados por insertarArco()
	//void eliminarNodo();
	//void borrarTodosArcos(nodo*);
	//void mostrarArcos();
	//void eliminarArco();
};
class nodo::arco
{
	public:
	nodo* destino; //puntero al nodo de llegada
	arco* sgte;
};
void nodo::insertarNodo(int i)
{
	nodo* t; //Contador que recorre todo el directorio
	nodo* nuevo=new nodo;//"nuevo" es el nodo que se insertara al directorio
	//cout<<"Ingrese el nombre: ";
	//cin>>nuevo->nombre; //Se asigna un nombre al nuevo nodo
	nuevo->nombre=Cuadro[i][0]->Text;
	nuevo->sgte=NULL; //nuevo no apunta aningun nodo
	nuevo->ady=NULL; //nuevo no apunta a ningun arco
	if(p==NULL) //Si el primer nodo del directorio es NULL
	{
		p=nuevo; //"nuevo" es el primer nodo del directorio (o sea la cabeza)
		Dire[i][0]->Text=reinterpret_cast<int&>(nuevo);
		//cout<<"1er nodo del directorio\n";
	}
	else
	{
		t=p; //t se inicializa al primer nodo del directorio
		while(t->sgte!=NULL) //Verifica si existe un nodo despúes de t
		{
			t=t->sgte; //Si es cierto, avanza al siguiente nodo
		}
		t->sgte=nuevo; //Cuando t apunte a NULL, significa que es el ultimo
						//entonces hacemos que apunte a "nuevo", y asi "nuevo" es el ultimo
		//cout<<"Nodo ingresado\n";
		Dire[i][0]->Text=reinterpret_cast<int&>(nuevo);
		Dire[i-1][0]->Text= Dire[i-1][0]->Text+"//"+ reinterpret_cast<int&>(t->sgte);
	}
}
void nodo::insertarArco(String ini, String fin, int i, int j)
{
	arco* nuevo=new arco(); //"nuevo" es el arco que se insertara y enlaza a los nodos inicio y final
	nodo* aux; //Contador que recorre la lista del directorio hasta encontrar el nodo inicial
	nodo* aux2; //Contador que recorre la lista del directorio hasta encontrar el nodo final

	nuevo->sgte=NULL; //El "nuevo" arco no apunta a ningun arco
	aux=p; //aux se inicializa al primer nodo del directorio
	aux2=p; //aux2 se inicializa al primer nodo del directorio
	nodo* aux3;
	aux3=p;

	while(aux2!=NULL) //Verifica que aun no se llega al final del directorio
	{
		if(aux2->nombre==fin)
		{
			break; //Si encontro el nombre sale de while
		}
		aux2=aux2->sgte; //Avanza al siguiente nodo
	}

	if (aux2==NULL) return; //Si no existe el nodo de nombre "fin"

	while(aux!=NULL) //Verifica que aun no se llega al final del directorio
	{
		if(aux->nombre==ini)
		{
			agregarArco(aux,aux2,nuevo, i, j); //Llama a la funcion agregarArco() que uno los nodos
										//aux y aux2
			return;
		}
		aux=aux->sgte; //Avanza al siguiente nodo
	}
	if (aux==NULL) return;
}
void nodo::agregarArco(nodo* aux,nodo* aux2, arco* nuevo, int i, int j)
{
	arco *q; //Contador que recorre todos los arcos de un nodo del directorio
	nodo* aux3;
	aux3=p;

	if(aux->ady==NULL) //Si el nodo aux no tiene ningun arco
	{
		aux->ady=nuevo; //entonces el primer arco del nodo es "nuevo" (la cabeza)
		nuevo->destino=aux2; //El destino del "nuevo" arco
		while(aux3!=NULL){
			if(aux3->nombre==aux->ady->destino->nombre){
				Dire[i][0]->Text=Dire[i][0]->Text+"//"+reinterpret_cast<int&>(aux3);
		   }
		   aux3=aux3->sgte;
		}
		Dire[i][j]->Text=Dire[i][j]->Text+reinterpret_cast<int&>(aux)+"//"+reinterpret_cast<int&>(aux2);
	}
	else
	{
		q=aux->ady; //si el nodo ya tiene arcos, q se incializa al primer arco
		while(q->sgte!=NULL)
		{
			q=q->sgte; //Mientras sea diferente de NULL avanza
		}
		q->sgte=nuevo; //Coloca el arco "nuevo" al final
		nuevo->destino=aux2; //se fija el destino del "nuevo" arco a aux2

		// Agregamos el arco
		Dire[i][j-1]->Text=Dire[i][j-1]->Text+"//"+reinterpret_cast<int&>(aux2);
		Dire[i][j]->Text=Dire[i][j]->Text+reinterpret_cast<int&>(aux)+"//"+reinterpret_cast<int&>(aux2);

	}
}
//////////////////////////////////
/////////////////////////////////
////////////////////////////////
//---------------------------------------------------------------------------
void __fastcall TfrmGrafo::btnDibujarClick(TObject *Sender)
{
	   int tTop=60;
	   int lLeft=30;
	   int i,j;
	   nNodos=StrToInt(txtNodos->Text);
	   if (nNodos>tMax) {
			return;
	   }
	   //Tabla de datos
	   for (i = 0; i < nNodos; i++) {
			for(j=0;j<nNodos;j++){
				Cuadro[i][j] =new TEdit(this);
				Cuadro[i][j]->Parent=this;
				Cuadro[i][j]->Height=30;
				Cuadro[i][j]->Top=tTop+i*35;
				Cuadro[i][j]->Width=100;
				Cuadro[i][j]->Left=lLeft+j*105;
				Cuadro[i][j]->Font->Color=clBlue;
				Cuadro[i][j]->Alignment=taCenter;
				if(j==0){
					Cuadro[i][j]->Color=clYellow;
				}
			}
	   }
	   //Tabla de direcciones de los datos
	   tTop=nNodos*60;
	   for (i = 0; i < nNodos; i++) {
			for(j=0;j<nNodos;j++){
				Dire[i][j] =new TEdit(this);
				Dire[i][j]->Parent=this;
				Dire[i][j]->Height=30;
				Dire[i][j]->Top=tTop+i*35;
				Dire[i][j]->Width=250;
				Dire[i][j]->Left=lLeft+j*255;
				Dire[i][j]->Font->Color=clBlue;
				Dire[i][j]->Alignment=taCenter;
				if(j==0){
					Dire[i][j]->Color=clYellow;
				}
				Dire[i][j]->Text=IntToStr(i)+","+ IntToStr(j);
			}
	   }
}
//---------------------------------------------------------------------------


void __fastcall TfrmGrafo::btnCrearGrafoClick(TObject *Sender)
{
	String inicio, final;
	nodo* grafo=new nodo;
	//Ingresando nodos
	for (int i = 0; i < nNodos; i++) {
		grafo->insertarNodo(i);
	}


	Dire[nNodos-1][0]->Text=Dire[nNodos-1][0]->Text+"//0";
	for(int fila=0; fila<nNodos; fila++){
	   for(int columna=1; columna<nNodos; columna++){
			inicio = Cuadro[fila][0]->Text;
			final = Cuadro[fila][columna]->Text;
			Dire[fila][columna]->Clear();

			if(final!=NULL){
			   grafo->insertarArco(inicio, final, fila, columna);
			}
	   }
	}
}
//---------------------------------------------------------------------------

