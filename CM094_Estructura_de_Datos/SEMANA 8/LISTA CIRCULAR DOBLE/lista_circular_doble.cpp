#include <vcl.h>
#include <stdio.h>
#include <iostream>
using namespace std;

//La clase NodoCircular
class NodoCircular
{
	private:
		int dato;
		NodoCircular* enlace; // Es el nodo que ira delante, el siguiente
	public:
		NodoCircular (int t){
			dato = t;
			enlace = this; // se apunta a sí mismo

		}

		int datoNodo(){ // devuelve el dato
			return dato;
		}

		void fijarDato(int a){ // fija el dato
			dato=a;
		}

		NodoCircular* enlaceNodo(){ // devuelve nodo al que apunta
			return enlace;
		}

		void ponerEnlace(NodoCircular* sgte){
			enlace = sgte; // enlaza con el nodo sgte
		}


};
//La clase ListaCircular
class ListaCircularDoble{

	private:
		NodoCircular* acceso;
	public:
		ListaCircularDoble() // Constructor
		{
			acceso=0; // Al principio la lista esta vacia
		}
		void crearLista();
		void visualizar();
		void insertarAcceso(int);

		void insertarDespues(int,int);
		void insertarAntes(int,int);
		void eliminar(int);
		void modificar(int,int);
};

//Crear una lista circular
void ListaCircularDoble::crearLista()
{
	int x;
	acceso=NULL; //Inicializa la lista
	cout << "Termina con -1" << endl;
	do
	{
		cin >> x;
		if (x != -1)
		{
			insertarAcceso(x);
		}
	}while (x != -1);
};

//Inserta un dato
void ListaCircularDoble::insertarAcceso(int dato)
{
	NodoCircular* nuevo;
	nuevo = new NodoCircular (dato);
	if (acceso != 0 )
	{
		nuevo -> ponerEnlace(acceso -> enlaceNodo());
		acceso -> ponerEnlace(nuevo); //Cierra el circulo
	}
	acceso = nuevo; //Ahora nuevo es el acceso
};

//Visualiza la lista
void ListaCircularDoble::visualizar()
{
	NodoCircular* indice;
	if (acceso != 0)
	{
		indice = acceso -> enlaceNodo(); // siguiente nodo al de acceso
		cout<<"DirDelDato"<<"\t"<<"Dato"<<"\t"<<"Siguiente"<<endl;
		do {
			cout <<indice<< "\t" <<indice->datoNodo()<<"\t"<<indice->enlaceNodo()<<endl;
			indice = indice -> enlaceNodo();
		}while(indice != acceso -> enlaceNodo());
	}
};


//%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
// Aqui comienza mi trabajo

 //Insertando despues de un nodo
void ListaCircularDoble::insertarDespues(int datoAnterior,int dato)
{
	NodoCircular* nuevo;
	NodoCircular* anterior;
	nuevo=new NodoCircular(dato);
	//Busqueda del anterior
	NodoCircular* indice;
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
void ListaCircularDoble::insertarAntes(int datoPosterior,int dato)
{
	NodoCircular* nuevo;
	NodoCircular* posterior;
	nuevo =new Circular(dato);
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

// Eliminar
   //Borrado de un nodo
 void ListaCircularDoble::eliminar(int dato)
 {
	NodoCircular *actual,*anterior;
	bool encontrado;
	actual=primero;
	anterior=NULL;
	encontrado=false;
	//busca el nodo a eliminar y al anterior
	while((actual!=NULL) && !encontrado){
		encontrado=(actual->datoNodo()==dato);
		if (!encontrado) {
			anterior=actual;
			actual=actual->enlaceNodo();
		}
	}
	//Borrando el nodo
	if (actual!=NULL){
	   if(actual==primero){
		   primero-actual->enlaceNodo();
	   }else{
		   anterior->ponerEnlace(actual->enlaceNodo());
       }
	}
	delete actual;
 }



//Modificar dato
void ListaCircularDoble::modificar(int datoAntiguo, int dato)
{
	// Bucle de búsqueda del antiguo
	NodoDoble* indice;
	bool encontrado = false;
	indice = cabeza;
	while ((indice != NULL) && (!encontrado)){
		encontrado = (indice -> datoNodo() == datoAntiguo);
		if (!encontrado){
			indice = indice -> adelanteNodo();
		}
	}
	//Reemplaza el dato
	if(indice != NULL) {
			indice->fijarDato(dato);
	}
}

int main(){
	ListaCircular miLista;
	miLista.crearLista();
	miLista.visualizar();
    Sleep(10000);
	return 0;
}
















/*Insertando al final de la lista
void ListaCircularDoble::insertarFinLista(int dato)
{
	NodoDoble* nuevo;
	nuevo=new NodoDoble(dato);
	nuevo->ponerAtras(cola);
	if (cola!=NULL)
		cola->ponerAdelante(nuevo);
	else
		cabeza=cola=nuevo;
	cola=nuevo;
}*/

