 //Nodo Generico
template <typename T> class Nodo
{
  private:
	T dato;
	Nodo <T>* enlace;
  public:
	Nodo (T t){
	   dato = t;
	   enlace = 0;
	}
	Nodo (T p, Nodo<T>* n){
	   dato = p;
	   enlace = n;
	}
	T datoNodo(){
	   return dato;
	}
	Nodo<T>* enlaceNodo(){
	   return enlace;
	}

	void ponerEnlace(Nodo<T>* sgte){
	   enlace = sgte;
	}
};

// Creamos la clase Lista
class Lista{
	private:
		Nodo<int>* primero;
	public:
		Lista(){
			primero=NULL;
		}
		void crearLista();
		void visualizarLista();
		void insertarCabezaLista(int);
		void insertarUltimo(int);
		Nodo<int>* ultimo();
		Nodo<int>* buscarLista(int);
		void insertarLista(int, int);
		void eliminar(int);
};

#include <iostream>
#include <string>
using namespace std;
// definimos el método crear lista
void Lista::crearLista(){
	int x;
	//primero=0; //NULL
	cout<<"El buble termina con -1"<<endl;
	do{
		cin>>x;
		if (x!=-1) {
			primero = new Nodo<int>(x, primero);
		}

	}while(x!=-1);
}
//definimos el método para visualizar la lista
void Lista::visualizarLista(){
	 Nodo<int>* indice;
	 cout<<"Direccion del nodo\tValor\tApunta"<<endl;
	 for (indice = primero; indice!=NULL; indice=indice->enlaceNodo()) {
		  cout<<indice<<"\t\t"<<indice->datoNodo()<<"\t"<<indice->enlaceNodo()<<endl;
	 }
	 cout<<endl;
}

// definimos el método de insertar la cabeza en la lista
void Lista::insertarCabezaLista(int dato){
	Nodo<int>* nuevo;
	nuevo = new Nodo<int>(dato);
	nuevo->ponerEnlace(primero); //Enlaza nuevo con primero
	primero = nuevo;  // mueve primero y apunta al nuevo nodo
}

// Definimos el método para insertar dato a la cola (al final)
void Lista::insertarUltimo(int dato){
	Nodo<int>* ultimo = this->ultimo();
	ultimo->ponerEnlace(new Nodo<int>(dato));
}
//Recorre la lista hasta encontrar
//la direccion del ultimo nodo
Nodo<int>* Lista::ultimo(){
	Nodo<int>* p = primero;
	while (p->enlaceNodo()!= NULL){
		p = p->enlaceNodo();
	}
	return p;
}

//Busqueda en listas enlazadas
Nodo<int>* Lista::buscarLista(int dato){
	Nodo<int>* indice;
	for (indice = primero; indice!= NULL; indice = indice->enlaceNodo()){
		if (dato == indice -> datoNodo()){
			return indice;
		}

	}
	return NULL; //Si no lo encuentra devuelve 0 (NULL)
}

//Insercion entre dos nodos de la lista
void Lista::insertarLista(int datoAnt, int dato){
	Nodo<int>* nuevo;
	Nodo<int>* anterior;
	nuevo = new Nodo<int>(dato);
	anterior=Lista::buscarLista(datoAnt);
	nuevo -> ponerEnlace(anterior -> enlaceNodo());
	anterior -> ponerEnlace(nuevo);
}

//Borrado de un nodo de la lista
void Lista::eliminar(int dato)
{
	Nodo<int> *actual, *anterior;
	bool encontrado;
	actual = primero;
	anterior = NULL;
	encontrado = false;
	// búsqueda del nodo y del anterior
	while ((actual != NULL) && !encontrado){
		encontrado = (actual->datoNodo() == dato);
		if (!encontrado){
			anterior = actual;
			actual = actual -> enlaceNodo();
		}
	}
	// enlace del nodo anterior con el siguiente
	if (actual != NULL){
		// distingue entre cabecera y resto de la lista
		if (actual == primero){
			primero = actual -> enlaceNodo();
		}else{
			anterior -> ponerEnlace(actual->enlaceNodo());
		}
		delete actual;
	}
}

int main(){
	/*
	Nodo<string>* cola;
	Nodo<string>* nodo2;
	Nodo<string>* nodo3;
	Nodo<string>* cabeza;
	cola=new Nodo<string>("Pablo");
	nodo2=new Nodo<string>("Guadalupe",cola);
	nodo3=new Nodo<string>("Benito",nodo2);
	cabeza=new Nodo<string>("Maria",nodo3);
	cout<<"Direccion de la cabeza\tValor\A donde apunta"<<endl;
	cout<<cabeza<<"\t\t"<<cabeza->datoNodo()<<"\t"<<cabeza->enlaceNodo()<<endl<<endl;
	cout<<"Direccion de la cola\tValor\Adonde apunta"<<endl;
	cout<<cola<<"\t\t"<<cola->datoNodo()<<"\t"<<cola->enlaceNodo()<<endl<<endl;*/

	int cabeza, cola, nodo_anterior, nodo_nuevo, nodo_eliminado;
	Lista miLista;
	miLista.crearLista();
	miLista.visualizarLista();

	cout<<"\nAgrega el elemento a insertar en  la cabeza: ";
	cin>>cabeza;
	cout<<"\nACTUALIZANDO..\n\n";
	miLista.insertarCabezaLista(cabeza);
	miLista.visualizarLista();

	cout<<"\nAgrega el elemento a insertar en  la cola: ";
	cin>>cola;
	cout<<"\nACTUALIZANDO..\n\n";
	miLista.insertarUltimo(cola);
	miLista.visualizarLista();

	cout<<"\nDigite el nuevo nodo y el nodo antiguo a ser reemplazado: ";
	cin>>nodo_nuevo;
	cin>>nodo_anterior;
	cout<<"\nACTUALIZANDO..\n\n";
	miLista.insertarLista(nodo_anterior, nodo_nuevo);
	miLista.visualizarLista();

	cout<<"\nDigite el nodo a ser eliminado: ";
	cin>>nodo_eliminado;
	cout<<"\nACTUALIZANDO..\n\n";
	miLista.eliminar(nodo_eliminado);
	miLista.visualizarLista();


	system("pause");
	return 0;

}

