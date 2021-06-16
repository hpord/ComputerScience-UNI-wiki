//Nodo Generico
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
//La clase lista
class Lista
{
	private:
	Nodo<int>* primero;
	public:
	Lista()
	{
		primero=0;
	}
	void crearLista();
	void visualizarLista();
	void insertaOrden(int);   //Crea la lista ordenada
	void insertarCabezaLista(int);
	void insertarUltimo(int);
	Nodo<int>* ultimo();
	Nodo<int>* buscarLista(int);
	void insertarLista(int,int);
	void eliminar(int);
};
#include <iostream>
#include <string>
using namespace std;
// Crea lista ordenada

void Lista::insertaOrden(int dato){
	 Nodo<int>* nuevo; //Nodo que voy a inseertar
	 nuevo = new Nodo<int>(dato);
	 if(primero==NULL){ // la lista esta vacia y 'dato' es el primer elemento
		primero=nuevo;
	 }else {
		 if (dato<primero->datoNodo()) { // Cuando el dato es el menor de la lista
			 nuevo->ponerEnlace(primero);
			 primero=nuevo;
		 }else{ // busca a la derecha hasta que encuentre un mayor o termine la lista
			Nodo<int> *anterior, *indice;
			anterior=indice=primero;
			while((indice->enlaceNodo() != NULL) && (dato>indice->datoNodo()) ){

				anterior=indice;
				indice=indice->enlaceNodo();
			}
			// Insertamos el nuevo nodo
			if(dato>indice->datoNodo()){
				anterior=indice;
			}
			nuevo->ponerEnlace(anterior->enlaceNodo());
			anterior->ponerEnlace(nuevo);
         }
	 }

}
//Crear Lista
void Lista::crearLista()
{
	 int x;
	 cout<<"Termina con -1"<<endl;
	 do
	 {
		cin>>x;
		if (x!=-1)
		{
			insertaOrden(x);
			//primero=new Nodo<int>(x,primero);
		}
	 } while (x!=-1);

}
//Visualizar lista
void Lista::visualizarLista()
{
	Nodo<int>* indice;
	cout<<"Direccion del nodo\tDato\tA donde apunta"<<endl;
	for(indice=primero; indice!=NULL;indice=indice->enlaceNodo())
	cout<<indice<<"\t\t"<<indice->datoNodo()<<"\t"<<indice->enlaceNodo()<<endl;
}
void Lista::insertarCabezaLista(int dato)
{
	Nodo<int>* nuevo;
	nuevo=new Nodo<int>(dato);
	nuevo->ponerEnlace(primero);
	primero=nuevo;
}
 //Insercion en la cola de la lista
 void Lista::insertarUltimo(int dato)
 {
	 Nodo<int>* ultimo=this->ultimo();
	 ultimo->ponerEnlace(new Nodo<int>(dato));
 }
 //Recorre la lista hasta encontrar la direccion
 //del ultimo nodo
 Nodo<int>* Lista::ultimo()
 {
	Nodo<int>* p=primero;
	while(p->enlaceNodo()!=NULL)
	{
		p=p->enlaceNodo();
	}
	return p;
 }
 //Busqueda en una lista
 Nodo<int>* Lista::buscarLista(int dato)
 {
	 Nodo<int>* indice;
	 for (indice=primero;indice!=NULL;indice=indice->enlaceNodo())
	 {
		if (dato==indice->datoNodo()) {
			return indice;
		}
	 }
	 return NULL;//NULL es 0
 }
 //Insertar nodo despues de otro
 void Lista::insertarLista(int datoAnt,int dato)
 {
	 Nodo<int>* nuevo;
	 Nodo<int>* anterior;
	 nuevo = new Nodo<int>(dato);
	 anterior=Lista::buscarLista(datoAnt);
	 nuevo->ponerEnlace(anterior->enlaceNodo());
	 anterior->ponerEnlace(nuevo);
 }
 //Borrado de un nodo
 void Lista::eliminar(int dato)
 {
	Nodo<int> *actual,*anterior;
	bool encontrado;
	actual=primero;
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
	   if(actual==primero)
	   {
		   primero-actual->enlaceNodo();
	   }
	   else
	   {
		   anterior->ponerEnlace(actual->enlaceNodo());
       }
	}
	delete actual;
 }
int main()
{
	/*Nodo<string>* cola;
	Nodo<string>* nodo2;
	Nodo<string>* nodo3;
	Nodo<string>* cabeza;
	cola=new Nodo<string>("Pablo");
	nodo2=new Nodo<string>("Guadalupe",cola);
	nodo3=new Nodo<string>("Benito",nodo2);
	cabeza=new Nodo<string>("Maria",nodo3);
	cout<<"Direccion de la cabeza\tDato\tA donde apunta"<<endl;
	cout<<cabeza<<"\t\t"<<cabeza->datoNodo()<<"\t"<<cabeza->enlaceNodo()<<endl<<endl;
	cout<<"Direccion de la cola\tDato\tA donde apunta"<<endl;
	cout<<cola<<"\t\t"<<cola->datoNodo()<<"\t"<<cola->enlaceNodo()<<endl<<endl;*/
	Lista miLista;
	miLista.crearLista();
	miLista.visualizarLista();
	miLista.insertarCabezaLista(7);
	miLista.insertarUltimo(11);
	miLista.insertarLista(5,100);
	miLista.eliminar(8);
	miLista.visualizarLista();
	system("pause");
	return 0;
}
