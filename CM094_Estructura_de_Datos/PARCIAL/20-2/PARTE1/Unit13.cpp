//---------------------------------------------------------------------------

#include <vcl.h>
#pragma hdrstop

#include "Unit13.h"
//---------------------------------------------------------------------------
#pragma package(smart_init)
#pragma resource "*.dfm"
TfrmListaDoble *frmListaDoble;
/*
Datos: Sanchez Sauñe Cristhian Wiki
ELIMINAR: Zambrano Altamirano Fernando Alonso
boton insertarDespues: Villarroel Lajo Gerald Takeshi
Insertar Datos Antes: Ronald Nicolas Saenz Chuqui
Modificar: Vilchez Diaz Vicente Jesus
*/
class NodoDoble
{
	private:
	int dato;
	NodoDoble* adelante; //A la derecha
	NodoDoble* atras; //A la izquierda
	public:
	NodoDoble(int t)
	{
		dato=t;
		adelante=atras=0;
	}
	int datoNodo(){return dato;}
	void fijarDato(int a){dato=a;}//Fija el dato
	NodoDoble* adelanteNodo(){return adelante;}
	NodoDoble* atrasNodo(){return atras;}
	void ponerAdelante(NodoDoble* a){adelante=a;}
	void ponerAtras(NodoDoble* a){atras=a;}
};
//Clase Lista Doble
class ListaDoble
{
	public:
	NodoDoble* cabeza;
	NodoDoble* cola;
	public:
	ListaDoble()
	{
		cabeza=cola=0;
	}
	void crearLista();////
	void visualizar();////
	void insertarCabezaLista(int);////
	void insertarFinLista(int);////
	void insertarDespues(int,int);////
	void insertarAntes(int,int);////
	void eliminar(int);
	void modificar(int,int);
};
ListaDoble miLista;
void ListaDoble::insertarCabezaLista(int dato){
	NodoDoble* nuevo;
	nuevo=new NodoDoble(dato);
	nuevo->ponerAdelante(cabeza);
	if (cabeza!=NULL)
		cabeza->ponerAtras(nuevo);
	else
		cola=nuevo;
	cabeza=nuevo;
}
void ListaDoble::modificar(int datoAntiguo, int dato)
{
	// Bucle de búsqueda del antiguo
	NodoDoble* indice;
	bool encontrado = false;
	indice = cabeza;
	while ((indice != NULL) && (!encontrado))
	{
	encontrado = (indice -> datoNodo() == datoAntiguo);
	if (!encontrado)
	indice = indice -> adelanteNodo();
	}
	//Reemplaza el dato
	if(indice != NULL)
	{
		indice->fijarDato(dato);
	}
}
//Insertando despues de un nodo
void ListaDoble::insertarDespues(int datoAnterior,int dato)
{
	NodoDoble* nuevo;
	NodoDoble* anterior;
	nuevo=new NodoDoble(dato);
	//Busqueda del anterior
	NodoDoble* indice;
	bool encontrado=false;
	indice=cabeza;
	while((indice!=NULL) && (!encontrado)){
		encontrado=(indice->datoNodo()==datoAnterior);
		if (!encontrado)
			indice=indice->adelanteNodo();
	}
	//Inserta el dato despues de datoAnterior
	if (indice!=NULL)
	{
		anterior=indice;
		nuevo->ponerAdelante(anterior->adelanteNodo());
		if (anterior->adelanteNodo()!=NULL)
			anterior->adelanteNodo()->ponerAtras(nuevo);
		else
			cola=nuevo;
		anterior->ponerAdelante(nuevo);
		nuevo->ponerAtras(anterior);
	}
}
//Insertando antes de un dato
void ListaDoble::insertarAntes(int datoPosterior,int dato)
{
	NodoDoble* nuevo;
	NodoDoble* posterior;
	nuevo =new NodoDoble(dato);
	//Busqueda del posterior
	NodoDoble* indice;
	bool encontrado=false;
	indice=cabeza;
	while ((indice!=NULL)&&(!encontrado))
	{
		encontrado=(indice->datoNodo()==datoPosterior);
		if (!encontrado)
			indice=indice->adelanteNodo();
	}
	//insertar dato antes de datoPosterior
	if (indice!=NULL)
	{
		posterior=indice;
		nuevo->ponerAdelante(posterior);
		if (posterior->atrasNodo()!=NULL)
			posterior->atrasNodo()->ponerAdelante(nuevo);
		else
			cabeza=nuevo;
		nuevo->ponerAtras(posterior->atrasNodo());
		posterior->ponerAtras(nuevo);
	}
}
//Eliminar
void ListaDoble::eliminar(int dato)
{
	NodoDoble* indice;
	indice=cabeza;
    bool flag=false;
    while((indice!=NULL)&&(!flag)){
        flag=(indice->datoNodo()==dato);
        if(!flag) indice=indice->adelanteNodo();
    }
    if(indice!=NULL){
		if(indice==cabeza){
            indice->adelanteNodo()->ponerAtras(NULL);
		} else if(indice==cola){
            indice->atrasNodo()->ponerAdelante(NULL);
        } else {
            indice->atrasNodo()->ponerAdelante(indice->adelanteNodo());
            indice->adelanteNodo()->ponerAtras(indice->atrasNodo());
        }
        delete indice;
	}
}
//---------------------------------------------------------------------------
__fastcall TfrmListaDoble::TfrmListaDoble(TComponent* Owner)
	: TForm(Owner)
{
}
//---------------------------------------------------------------------------

void __fastcall TfrmListaDoble::btnModificarClick(TObject *Sender)
{
	miLista.modificar(StrToInt(txtNum->Text),StrToInt(txtDatoN->Text));
	btnVisClick(Sender);

}
//---------------------------------------------------------------------------

void __fastcall TfrmListaDoble::btnInsertarDClick(TObject *Sender)
{
	miLista.insertarDespues(StrToInt(txtNum->Text),StrToInt(txtDatoN->Text));
	btnVisClick(Sender);
}
//---------------------------------------------------------------------------

void __fastcall TfrmListaDoble::btnVisClick(TObject *Sender)
{
        NodoDoble* indice;
	lstAtras->Clear();
	lstDirDato->Clear();
	lstDato->Clear();
	lstAdelante->Clear();
	indice= miLista.cabeza;
	while(indice!=NULL){
		lstAtras->Items->Add(reinterpret_cast<int>(indice->atrasNodo()));
		lstDirDato->Items->Add(reinterpret_cast<int>(indice));
		lstDato->Items->Add(IntToStr(indice->datoNodo()));
		lstAdelante->Items->Add(reinterpret_cast<int>(indice->adelanteNodo()));
		indice=indice->adelanteNodo();
	}
}
//---------------------------------------------------------------------------

void __fastcall TfrmListaDoble::btnInsertarAClick(TObject *Sender)
{
	miLista.insertarAntes(StrToInt(txtNum->Text),StrToInt(txtDatoN->Text));
	btnVisClick(Sender);
}
//---------------------------------------------------------------------------


void __fastcall TfrmListaDoble::txtDatoKeyPress(TObject *Sender, System::WideChar &Key)

{
	if (Key == VK_RETURN ) {

			miLista.insertarCabezaLista(StrToInt(txtDato->Text));
			txtDato->Clear();
	}
	btnVisClick(Sender);
}
//---------------------------------------------------------------------------

void __fastcall TfrmListaDoble::btnEliminarClick(TObject *Sender)
{
	miLista.eliminar(StrToInt(txtNum->Text));
    btnVisClick(Sender);
}
//---------------------------------------------------------------------------

