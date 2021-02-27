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
		NodoCircular (int t)
		{
			dato = t;
			enlace = this; // se apunta a sí mismo
		}
		int datoNodo() // devuelve el dato
		{
			return dato;
		}
		void fijarDato(int a) // fija el dato
		{
			dato=a;
		}
		NodoCircular* enlaceNodo() // devuelve nodo al que apunta
		{
			return enlace;
		}
		void ponerEnlace(NodoCircular* sgte)
		{
			enlace = sgte; // enlaza con el nodo sgte
		}
};

//La clase ListaCircular
class ListaCircular
{
	private:
		NodoCircular* acceso;
	public:
		ListaCircular() // Constructor
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
void ListaCircular::crearLista()
{
	int x;
	acceso=NULL; //Inicializa la lista
	cout << "Termina con -1" << endl;

	do{
		cin >> x;
		if (x != -1)
		{
			insertarAcceso(x);
		}
	}while (x != -1);
}

//Inserta un dato
void ListaCircular::insertarAcceso(int dato)
{
	NodoCircular* nuevo;
	nuevo = new NodoCircular (dato);
	if (acceso != 0 )
	{
		nuevo -> ponerEnlace(acceso -> enlaceNodo());
		acceso -> ponerEnlace(nuevo); //Cierra el circulo
	}
	acceso = nuevo; //Ahora nuevo es el acceso
}


//Visualiza la lista
void ListaCircular::visualizar()
{
	NodoCircular* indice;
	if (acceso != 0)
	{
		indice = acceso->enlaceNodo(); // siguiente nodo al de acceso
		cout<<"DirDelDato"<<"\t"<<"Dato"<<"\t"<<"Siguiente"<<endl;
		do {
			cout <<indice<< "\t" <<indice->datoNodo()<<"\t"<<indice->enlaceNodo()<<endl;
			indice = indice -> enlaceNodo();
		}while(indice != acceso -> enlaceNodo());
	}
}

// insertarAntes
void ListaCircular::insertarAntes(int datoFijo, int anterior){
	NodoCircular* indice;
	NodoCircular* prueba;


	int encontrado=0;
	indice=acceso;


	while((!encontrado)&& (indice->enlaceNodo()!=acceso)){
		encontrado = (indice->enlaceNodo()->datoNodo()==datoFijo);
		if(!encontrado)
		 indice=indice->enlaceNodo();
	 }


	encontrado = (indice->enlaceNodo()->datoNodo()==datoFijo);
	if(encontrado){
		prueba=indice->enlaceNodo();
		if(acceso==acceso->enlaceNodo())
		   acceso=NULL;
		else{
		   if(prueba==acceso)
			 acceso=indice;
			 indice->ponerEnlace(prueba->enlaceNodo());
		}
		delete(prueba);
	}
}

// insertarAntes
void ListaCircular::insertarDespues(int datoFijo, int despues){
	NodoCircular* indice;
	NodoCircular* prueba;


	int encontrado=0;
	indice=acceso;


	while((!encontrado)&& (indice->enlaceNodo()!=acceso)){
		encontrado = (indice->enlaceNodo()->datoNodo()==datoFijo);
		if(!encontrado)
		 indice=indice->enlaceNodo();
	 }


	encontrado = (indice->enlaceNodo()->datoNodo()==datoFijo);


	if(encontrado){
		prueba=indice->enlaceNodo();
		if(acceso==acceso->enlaceNodo())
		   acceso=NULL;
		else{
		   if(prueba==acceso)
			 acceso=indice;
			 indice->ponerEnlace(prueba->enlaceNodo());
		}
		delete(prueba);
	}
}

// eliminar
void ListaCircular::eliminar(int dato){
	NodoCircular* indice;
	NodoCircular* prueba;


	int encontrado=0;
	indice=acceso;


	while((!encontrado)&& (indice->enlaceNodo()!=acceso)){
		encontrado = (indice->enlaceNodo()->datoNodo()==dato);
		if(!encontrado)
		 indice=indice->enlaceNodo();
	 }


	encontrado = (indice->enlaceNodo()->datoNodo()==dato);
	if(encontrado){
		prueba=indice->enlaceNodo();
		if(acceso==acceso->enlaceNodo())
		   acceso=NULL;
		else{
		   if(prueba==acceso)
			 acceso=indice;
			 indice->ponerEnlace(prueba->enlaceNodo());
		}
		delete(prueba);
	}
}


// modificar
void ListaCircular::modificar(int datoAntiguo, int datoNuevo){
	NodoCircular* indice;
	NodoCircular* prueba;


	int encontrado=0;
	indice=acceso;


	while((!encontrado)&& (indice->enlaceNodo()!=acceso)){
		encontrado = (indice->enlaceNodo()->datoNodo()==datoAntiguo);
		if(!encontrado)
		 indice=indice->enlaceNodo();
	 }

	encontrado = (indice->enlaceNodo()->datoNodo()==datoAntiguo);
	if(encontrado){
		indice->enlaceNodo()->fijarDato(datoNuevo);
	}

}



int main(){

	int numero, numero_nuevo;

	ListaCircular miLista;
	miLista.crearLista();
	miLista.visualizar();


	cout<<"Ingrese el número a eliminar : ";
	cin>>numero;
	miLista.eliminar(numero);
	miLista.visualizar();

	cout<<"Ingrese el número a reemplazar : ";
	cin>>numero;
	cout<<"Ingrese su reemplazo : ";
	cin>>numero_nuevo;
	miLista.modificar(numero, numero_nuevo);
	miLista.visualizar();

	Sleep(10000);
	return 0;
}

