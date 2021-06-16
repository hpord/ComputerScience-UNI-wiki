//Crear recursivo
#include <iostream>
using namespace std;
class Nodo
{
	public:
	int dato;
	Nodo *izq,*der;
	Nodo(){
		dato=NULL;
		izq=der=NULL;
	}
};
class arbolBB
{
	public:
	Nodo *raiz;
	arbolBB()
	{
		raiz=NULL;
	}
	void crear(int);
	void crear(Nodo*, int);
	void preOrden(Nodo*);
	void enOrden(Nodo*);
	void postOrden(Nodo*);
};
void arbolBB::crear(int nuevoDato) //Crea la raiz
{
	if (raiz==NULL) //Si no tiene raíz, crea el nodo raiz
	{
		raiz=new Nodo;
		raiz->dato=nuevoDato;
		return;
	}
		Nodo *r=raiz;
		crear(r, nuevoDato); //Llamada a la función recursiva
}
// Funcion recursiva
void arbolBB::crear(Nodo *r, int nuevoDato)
{
	if (nuevoDato < r->dato) // Si el nuevoDato es menor que el dato raíz entonces se mueve a la izquierda
	{
		if(r->izq==NULL) // Si izq is NULL coloca el nuevoNodo a la izquierda.
		{
			Nodo *nuevoNodo;
			nuevoNodo=new Nodo;
			nuevoNodo->dato=nuevoDato;
			r->izq=nuevoNodo;
			return;
		}
		crear(r->izq, nuevoDato); // Si no mueve la raíz al nodo de la izquierda
	}
else 
	{
		if (nuevoDato> r->dato) // Si el nuevoDato es mayor que el dato raíz entonces se mueve a la derecha
		{
			if(r->der==NULL) // Si der is NULL coloca el nuevoNodo a la derecha.
			{
				Nodo *nuevoNodo=new Nodo;
				nuevoNodo->dato=nuevoDato;
				r->der=nuevoNodo;
				return;
			}
			crear(r->der, nuevoDato); // Si no mueve la raíz al nodo de la derecha
		}
	}
}

//Funcion recursiva para preorden
void arbolBB::preOrden(Nodo *raiz)
{
	if (raiz!=NULL)
	{
		cout<<raiz->dato<<"  ";
		preOrden(raiz->izq);
		preOrden(raiz->der);
	}
}
//Funcion recursiva para enorden
void arbolBB::enOrden(Nodo *raiz)
{
	if (raiz!=NULL)
	{
		enOrden(raiz->izq);
		cout<<raiz->dato<<"  ";
		enOrden(raiz->der);
	}
}
//Funcion recursiva para postorden
void arbolBB::postOrden(Nodo *raiz)
{
	if (raiz!=NULL)
	{
		postOrden(raiz->izq);
		postOrden(raiz->der);
		cout<<raiz->dato<<"  ";
	}
}
//Funcion completar arbol
void completarArbol(arbolBB &a)
{
	int n,dato;
	cout<<"Cuantos nodos desea insertar (recursivo): ";
	cin>>n;
	for (int i=1; i<=n;i++)
	{
		cout<<"Dato "<<i<<": ";
		cin>>dato;
		a.crear(dato);
	}
}
int main()
{
	arbolBB a;
	completarArbol(a);
	cout<<"\nPre Orden"<<endl;
	a.preOrden(a.raiz);
	cout<<"\nEn Orden"<<endl;
	a.enOrden(a.raiz);
	cout<<"\nPost Orden"<<endl;
	a.postOrden(a.raiz);
	return 0;
}