//---------------------------------------------------------------------------

#include <vcl.h>
#pragma hdrstop

#include "Unit12.h"
//---------------------------------------------------------------------------
#pragma package(smart_init)
#pragma resource "*.dfm"
TForm12 *Form12;
//Mis datos//
#include <ctime>
//////////////////////
////Nodo Generico////
////////////////////
template <typename T> class Nodo
{
private:
T dato;
Nodo <T>* enlace;
public:
Nodo (T t)
{
dato = t;
enlace = 0;
}
Nodo (T p, Nodo<T>* n)
{
dato = p;
enlace = n;
}
///Para modificar
T fijarDatoNodo(T dato)
{
	this->dato=dato;
}
///////
T datoNodo()
{
return dato;
}
Nodo<T>* enlaceNodo()
{
return enlace;
}
void ponerEnlace(Nodo<T>* sgte)
{
enlace = sgte;
}
};
///////////////////
//La clase lista//
/////////////////
class Lista
{
	private:
	Nodo<int>* primero;
	public:
	Lista()
	{
		primero=NULL;
	}
	Nodo<int>* LeerPrimero(){
		return primero;
	}
	void FijarPrimero(Nodo<int>* dato){
		primero=dato;
	}
};
Lista miLista;
//---------------------------------------------------------------------------
__fastcall TForm12::TForm12(TComponent* Owner)
	: TForm(Owner)
{
}
//---------------------------------------------------------------------------
void __fastcall TForm12::FormCreate(TObject *Sender)
{
	lblCurso->Caption="Curso:\nAlgoritmos y Estructura de datos\nCC-FC-UNI";

}
//---------------------------------------------------------------------------

void __fastcall TForm12::rdbInsercionClick(TObject *Sender)
{
	pnlInsercion->Visible=true;
	pnlBusqueda->Visible=false;
	pnlBorrado->Visible=false;
	pnlModificar->Visible=false;
}
//---------------------------------------------------------------------------

void __fastcall TForm12::rdbBusquedaClick(TObject *Sender)
{
	pnlInsercion->Visible=false;
	pnlBusqueda->Visible=true;
	pnlBorrado->Visible=false;
	pnlModificar->Visible=false;
	pnlBusqueda->Top=pnlInsercion->Top;
	pnlBusqueda->Left=pnlInsercion->Left;
}

//---------------------------------------------------------------------------

void __fastcall TForm12::rdbBorradoClick(TObject *Sender)
{
	pnlInsercion->Visible=false;
	pnlBusqueda->Visible=false;
	pnlBorrado->Visible=true;
	pnlModificar->Visible=false;
	pnlBorrado->Top=pnlInsercion->Top;
	pnlBorrado->Left=pnlInsercion->Left;
}
//---------------------------------------------------------------------------

void __fastcall TForm12::rdbModificarClick(TObject *Sender)
{
	pnlInsercion->Visible=false;
	pnlBusqueda->Visible=false;
	pnlBorrado->Visible=false;
	pnlModificar->Visible=true;
	pnlModificar->Top=pnlInsercion->Top;
	pnlModificar->Left=pnlInsercion->Left;
}
//---------------------------------------------------------------------------

void __fastcall TForm12::rdbManualClick(TObject *Sender)
{
	 btnAleatorio->Enabled=false;
	 txtC->Enabled=false;
	 txtLimInf->Enabled=false;
	 txtLimSup->Enabled=false;
	 txtDato->Enabled=true;
}
//---------------------------------------------------------------------------

void __fastcall TForm12::rdbAleatorioClick(TObject *Sender)
{
	 txtDato->Enabled=false;
	 btnAleatorio->Enabled=true;
	 txtC->Enabled=true;
	 txtLimInf->Enabled=true;
	 txtLimSup->Enabled=true;
}
//---------------------------------------------------------------------------

void __fastcall TForm12::txtDatoKeyPress(TObject *Sender, System::WideChar &Key)
{
	if(Key==VK_RETURN){
		int x=StrToInt(txtDato->Text);
		miLista.FijarPrimero(new Nodo<int>(x,miLista.LeerPrimero()));
		lstDireccion->Items->Add(reinterpret_cast<int>(miLista.LeerPrimero()));
		lstValor->Items->Add(StrToInt(miLista.LeerPrimero()->datoNodo()));
		lstApunta->Items->Add(reinterpret_cast<int>(miLista.LeerPrimero()->enlaceNodo()));
		txtDato->Text="";
	}
}
//---------------------------------------------------------------------------

void __fastcall TForm12::btnAleatorioClick(TObject *Sender)
{
	int n,i,LimInf,LimSup,x;
	srand(time(NULL));
	n=StrToInt(txtC->Text);
	LimInf=StrToInt(txtLimInf->Text); //10
	LimSup=StrToInt(txtLimSup->Text); //15  dif 5--->0 a 5
	for (i = 1; i <= n; i++) {
		x=rand()%(LimSup-LimInf+1) +LimInf;
		miLista.FijarPrimero(new Nodo<int>(x,miLista.LeerPrimero()));
		lstDireccion->Items->Add(reinterpret_cast<int>(miLista.LeerPrimero()));
		lstValor->Items->Add(StrToInt(miLista.LeerPrimero()->datoNodo()));
		lstApunta->Items->Add(reinterpret_cast<int>(miLista.LeerPrimero()->enlaceNodo()));
	}
}
//---------------------------------------------------------------------------



void __fastcall TForm12::btnVoltearClick(TObject *Sender)
{
	int n,i;
	String direccion,valor,apunta;
	n=lstDireccion->Count;
	for (i = n-1; i >=0; i--) {
		direccion=lstDireccion->Items->Strings[i];
		valor=lstValor->Items->Strings[i];
		apunta=lstApunta->Items->Strings[i];
		lstDireccion->Items->Add(direccion);
		lstValor->Items->Add(valor);
		lstApunta->Items->Add(apunta);
	}
	for (i = 0; i <n; i++) {
		lstDireccion->Items->Delete(0);
		lstValor->Items->Delete(0);
		lstApunta->Items->Delete(0);
	}
}
//---------------------------------------------------------------------------

void __fastcall TForm12::btnLimpiarClick(TObject *Sender)
{
	lstDireccion->Clear();
	lstValor->Clear();
	lstApunta->Clear();
	Nodo<int> *actual;
	actual=miLista.LeerPrimero();
	while((actual!=NULL))// && !encontrado)
	{
	   miLista.FijarPrimero(actual->enlaceNodo());
	delete actual;
	actual=miLista.LeerPrimero();
	}
}
//---------------------------------------------------------------------------

void __fastcall TForm12::btnInsertarClick(TObject *Sender)
{
	int dato=StrToInt(txtDatoIns->Text);
	if (rdbCabeza->Checked) {
		Nodo<int>* nuevo;
		nuevo=new Nodo<int>(dato);
		nuevo->ponerEnlace(miLista.LeerPrimero());
		miLista.FijarPrimero(nuevo);
	}else if (rdbCola->Checked) {
		//Nodo<int>* ultimo=this->ultimo();
		//Halla el ultimo
		Nodo<int>* ultimo=miLista.LeerPrimero();
		while(ultimo->enlaceNodo()!=NULL)
		{
			ultimo=ultimo->enlaceNodo();
		}
		//Fin Halla el ultimo
		ultimo->ponerEnlace(new Nodo<int>(dato));
	}else if (rdbInsertarA->Checked) {
		Nodo<int>* nuevo;
		Nodo<int>* antesDelNodo;
		nuevo = new Nodo<int>(dato);
		bool encontro=false;
		int datoPos=StrToInt(txtDatoRef->Text);
		Nodo<int>* indice;
		antesDelNodo=NULL;
		/////
		for (indice=miLista.LeerPrimero();indice!=NULL;indice=indice->enlaceNodo())
		{
			if (datoPos==indice->datoNodo()) {
				encontro=true;
				//Cuando continua completa los listbox de pnlCoincidencia
				break;//Escapo cuando encuentro al primero
			}
			antesDelNodo=indice;
		}
		/////
		if (antesDelNodo==NULL) {
			nuevo->ponerEnlace(miLista.LeerPrimero());
			miLista.FijarPrimero(nuevo);
		} else if (encontro)
		{
			nuevo->ponerEnlace(antesDelNodo->enlaceNodo());
			antesDelNodo->ponerEnlace(nuevo);
		}

	}else{
		Nodo<int>* nuevo;
		Nodo<int>* anterior;
		nuevo = new Nodo<int>(dato);
		int datoAnt=StrToInt(txtDatoRef->Text);
			Nodo<int>* indice;
		anterior=NULL;//Por si acaso no lo encuentra
		for (indice=miLista.LeerPrimero();indice!=NULL;indice=indice->enlaceNodo())
		{
			if (datoAnt==indice->datoNodo()) {
				anterior=indice;
				//Cuando continua completa los listbox de pnlCoincidencia
				break;//Escapo cuando encuentro al primero
			}
		}
		/////
		if (anterior!=NULL) {
			nuevo->ponerEnlace(anterior->enlaceNodo());
			anterior->ponerEnlace(nuevo);
		}
	}
	//Revisualiza la lista
	lstDireccion->Clear();
	lstValor->Clear();
	lstApunta->Clear();
	Nodo<int>* indice;
	for(indice=miLista.LeerPrimero(); indice!=NULL;indice=indice->enlaceNodo())
	{
		lstDireccion->Items->Add(reinterpret_cast<int&>(indice));
		lstValor->Items->Add(StrToInt(indice->datoNodo()));
		lstApunta->Items->Add(reinterpret_cast<int>(indice->enlaceNodo()));
	}
}
//---------------------------------------------------------------------------


void __fastcall TForm12::rdbCabezaClick(TObject *Sender)
{
	if(rdbCabeza->Checked){
		btnInsertar->Visible=true;
		lblInsertar->Visible=false;
		txtDatoRef->Visible=false;
	}

}
//---------------------------------------------------------------------------

void __fastcall TForm12::rdbColaClick(TObject *Sender)
{
	if(rdbCola->Checked){
		btnInsertar->Visible=true;
		lblInsertar->Visible=false;
		txtDatoRef->Visible=false;
	}
}
//---------------------------------------------------------------------------

void __fastcall TForm12::rdbInsertarAClick(TObject *Sender)
{
	if(rdbInsertarA->Checked){
		btnInsertar->Visible=true;
		lblInsertar->Visible=true;
		txtDatoRef->Visible=true;
		lblInsertar->Caption="Antes";
	}
}
//---------------------------------------------------------------------------

void __fastcall TForm12::rdbInsertarDClick(TObject *Sender)
{
	if(rdbInsertarD->Checked){
		btnInsertar->Visible=true;
		lblInsertar->Visible=true;
		txtDatoRef->Visible=true;
		lblInsertar->Caption="Después";
	}
}
//---------------------------------------------------------------------------






void __fastcall TForm12::btnBusquedaClick(TObject *Sender)
{
	int dato=StrToInt(cboDato->Text);
	Nodo<int>* indice;
	for (indice=miLista.LeerPrimero();indice!=NULL;indice=indice->enlaceNodo())
	{
		if (dato==indice->datoNodo()) {
			txtDireccion->Text=reinterpret_cast<int>(indice);
			txtValor->Text=StrToInt(indice->datoNodo());
			txtApunta->Text=reinterpret_cast<int>(indice->enlaceNodo());
			//Cuando continua completa los listbox de pnlCoincidencia
			break;//Escapo cuando encuentro al primero
		}
	}
}
//---------------------------------------------------------------------------


void __fastcall TForm12::btnBorrarClick(TObject *Sender)
{
	int dato=StrToInt(cboDatoB->Text);
	Nodo<int> *actual,*anterior;
	bool encontrado;
	actual=miLista.LeerPrimero();
	anterior=NULL;
	encontrado=false;
	//busca el nodo a eliminar y al anterior
	while((actual!=NULL) && !encontrado)
	{
		encontrado=(actual->datoNodo()==dato);
		if (!encontrado) {
			anterior=actual;
			actual=actual->enlaceNodo();
		}
	}
	//Borrando el nodo
	if (actual!=NULL)
	{
	   if(actual==miLista.LeerPrimero())
	   {
		   miLista.FijarPrimero(actual->enlaceNodo());
	   }
	   else
	   {
		   anterior->ponerEnlace(actual->enlaceNodo());
	   }
	}
	delete actual;
	///Escribiendo en los textbox
	txtDireccionB->Text=reinterpret_cast<int>(actual);
	txtValorB->Text=StrToInt(actual->datoNodo());
	txtApuntaB->Text=reinterpret_cast<int>(actual->enlaceNodo());
	//Revisualiza la lista
	lstDireccion->Clear();
	lstValor->Clear();
	lstApunta->Clear();
	Nodo<int>* indice;
	for(indice=miLista.LeerPrimero(); indice!=NULL;indice=indice->enlaceNodo())
	{
		lstDireccion->Items->Add(reinterpret_cast<int&>(indice));
		lstValor->Items->Add(StrToInt(indice->datoNodo()));
		lstApunta->Items->Add(reinterpret_cast<int>(indice->enlaceNodo()));
	}

}
//---------------------------------------------------------------------------

void __fastcall TForm12::btnModificarClick(TObject *Sender)
{
    int dato=StrToInt(cboDatoM->Text);
	int nuevo=StrToInt(txtNuevo->Text);
	Nodo<int>* indice;
	 for (indice=miLista.LeerPrimero();indice!=NULL;indice=indice->enlaceNodo())
	 {
		if (dato==indice->datoNodo()) {
		  indice->fijarDatoNodo(nuevo);
		  break;
		}
	 }
     //Visualizar la lista completa en el listbox
	lstDireccion->Clear();
	lstValor->Clear();
	lstApunta->Clear();
	for(indice=miLista.LeerPrimero(); indice!=NULL;indice=indice->enlaceNodo())
	{
		lstDireccion->Items->Add(reinterpret_cast<int>(indice));
		lstValor->Items->Add(IntToStr(indice->datoNodo()));
		lstApunta->Items->Add(reinterpret_cast<int>(indice->enlaceNodo()));
	}
}
//---------------------------------------------------------------------------

void __fastcall TForm12::cboDatoMEnter(TObject *Sender)
{
//Completando el ComboBox
	cboDatoM->Clear();
	int n,i;
	String direccion,valor,apunta;
	n=lstValor->Count;
	for (i=0; i<n; i++) {
		valor=lstValor->Items->Strings[i];
		cboDatoM->Items->Add(valor);
	}
}
//---------------------------------------------------------------------------

void __fastcall TForm12::cboDatoBEnter(TObject *Sender)
{
//Completando el Combo Box
	cboDatoB->Clear();
	int i,n;
	String valor;
	n=lstValor->Count;
	for (i = 0; i < n; i++) {
		valor=lstValor->Items->Strings[i];
		cboDatoB->Items->Add(valor);
	}
}
//---------------------------------------------------------------------------

void __fastcall TForm12::cboDatoEnter(TObject *Sender)
{
//Completando el Combo Box
	cboDato->Clear();
	int i,n;
	String valor;
	n=lstValor->Count;
	for (i = 0; i < n; i++) {
		valor=lstValor->Items->Strings[i];
		cboDato->Items->Add(valor);
	}
}
//---------------------------------------------------------------------------

