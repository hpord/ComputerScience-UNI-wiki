//Crea el árbol de forma NO recursiva
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
	void preOrden(Nodo*);
	void enOrden(Nodo*);
	void postOrden(Nodo*);
};
void arbolBB::crear(int nuevoDato)
{
	//Crea la raiz del arbol
	if (raiz==NULL)
	{
		raiz=new Nodo;
		raiz->dato=nuevoDato;
		raiz->izq=raiz->der=NULL;
		//cout<<"raiz: "<<raiz->dato<<endl;
		return;
	}
	//Crea un nodo y le asigna el nuevo dato, si es que ya se tiene la raiz
	Nodo *nuevoNodo,*r;
	nuevoNodo=new Nodo;
	nuevoNodo->dato=nuevoDato;
	nuevoNodo->izq=nuevoNodo->der=NULL;
	//Inicializa la raiz
	r=raiz;
	while(r!=NULL) //Continua mientras la raiz no sea una hoja
	{
		if(nuevoDato<r->dato)
		{
			if(r->izq==NULL)
			{
				r->izq=nuevoNodo;
				//cout<<"izquierda "<<raiz->izq<<endl;
				break;
			}
			r=r->izq;
		}
		else if(nuevoDato>r->dato)
		{
			if(r->der==NULL)
			{
				r->der=nuevoNodo;
				//cout<<"derecha "<<raiz->der<<endl;
				break;
			}
			r=r->der;
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
	cout<<"Cuantos nodos desea insertar: ";
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