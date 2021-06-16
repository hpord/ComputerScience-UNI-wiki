#include <vcl.h>
//Clase NodoDoble
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
	private:
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
//Crear una lista doblemente enlazada
#include <iostream>
using namespace std;
void ListaDoble::crearLista(){
	int x;
	cabeza=cola=0;//0 es NULL en Dev-C++
	cout<<"Termina con -1"<<endl;
	do
	{
		cin>>x;
		if (x!=-1)
			insertarCabezaLista(x);
	}while (x!=-1);
}
//Insertar dato por la cabeza
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
//Visualizar ListaDoble
void ListaDoble::visualizar(){
	NodoDoble* indice;
	indice=cabeza;
	cout<<"Atras\tDirDato\t\tDato\tAdelante\n";
	while(indice!=NULL){
	cout<<indice->atrasNodo()<<"\t\t"<<indice<<"\t"<<indice->datoNodo()<<"\t"<<indice->adelanteNodo()<<endl;
	indice=indice->adelanteNodo();
	Sleep(600);
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
//Insertando al final de la lista
void ListaDoble::insertarFinLista(int dato)
{
	NodoDoble* nuevo;
	nuevo=new NodoDoble(dato);
	nuevo->ponerAtras(cola);
	if (cola!=NULL)
		cola->ponerAdelante(nuevo);
	else
		cabeza=cola=nuevo;
	cola=nuevo;
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
//Modificar dato
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
int main()
{
	ListaDoble miLista;
	miLista.crearLista();
	miLista.modificar(7,777);
	//miLista.insertarAntes(8,888);
	//miLista.insertarCabezaLista(5000);
	//miLista.insertarDespues(5,1000);
	//miLista.insertarDespues(45,8000);
	miLista.visualizar();
	return 0;
}
