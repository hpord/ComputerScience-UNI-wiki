///////////COLA//////////
#include <iostream>
using namespace std;
class NodoCola
{
	public:
		NodoCola* siguiente;
		int elemento;
		NodoCola(int x)
		{
			elemento=x;
			siguiente=0;//NULL
		}
};
class Cola
{
	private:
		NodoCola* frente;
		NodoCola* final;
	public:
	Cola()//Constructor que cra la cola
	{
		frente=final=0; //NULL
	}
	void insertar(int elemento);
	int quitar();
	int frenteCola();
	int finalCola();
	bool colaVacia();
	NodoCola* devolverFrente();
	NodoCola* devolverFinal();
};
//Devuelve el nodo que esta al frente
NodoCola* Cola::devolverFrente()
{
	return frente;
}
//Devuelve el nodo que esta al final
NodoCola* Cola::devolverFinal()
{
	return final;
}
//Devuelve el elemento que esta en el frente
int Cola::frenteCola()
{
	if (colaVacia())
	{
		cout<<"Cola vacia: ";
		return 0; //NULL
	}
	else
		return frente->elemento;
}
//Devuelve el elemento que esta en el frente
int Cola::finalCola()
{
	if (colaVacia())
	{
		cout<<"Cola vacia: ";
		return 0; //NULL
	}
	else
		return final->elemento;
}
//Inserta un elemento por el final de la cola
void Cola::insertar(int elemento)
{
	NodoCola* nuevo;
	nuevo=new NodoCola(elemento);
	if (colaVacia())
	{
		frente=nuevo;
	}
	else
	{
		final->siguiente=nuevo;
	}
	final=nuevo;
}
bool Cola::colaVacia()
{
	if(frente==0)//En Dev C++ NULL=0
		frente=final=0;
	return frente==0;
}
//Elimina los nodos desde el frente
int Cola::quitar()
{
	if (colaVacia())
	{
		cout<<"Cola vacia, no se puede extraer.\n";
		return 0;//NULL
	}
	else
	{
		cout<<"Se elimina de la memoria el nodo: "<<frente;
		int x=frente->elemento;
		NodoCola* a=frente;
		frente=frente->siguiente;
		delete a;
		return x;
	}
}
////////////////////////////////
///////////////////////////////
//Completa la cola desde el final
void completarCola(Cola &cola)
{
	int x,n;
	cout<<"Cuantos elementos ingresara a la cola: ";
	cin>>n;
	cout<<"Digite el elemento y luego pulse Enter\n";
	for (int i=1;i<=n;i++)
	{
		cout<<"Direccion frente: "<<cola.devolverFrente()<<
		" . Elemento frente: "<<cola.frenteCola()<<endl;
		cout<<"Direccion final: "<<cola.devolverFinal()<<
		" . Elemento final: "<<cola.finalCola()<<endl;
		cout<<"Indice "<<i<<": ";
		cin>>x;
		cola.insertar(x);
	}
	cout<<"Direccion frente: "<<cola.devolverFrente()<<
	" . Elemento frente: "<<cola.frenteCola()<<endl;
	cout<<"Direccion final: "<<cola.devolverFinal()<<
	" . Elemento final: "<<cola.finalCola()<<endl;
}
//Muestra la cola desde el frente
void mostrarCola(Cola &cola)
{
	int x;
	cout<<"\nMostrando los elementos de la cola:\n";
	while(!cola.colaVacia())
	{
		cout<<"Direccion frente: "<<cola.devolverFrente()<<
		" . Elemento frente: "<<cola.frenteCola()<<endl;
		cout<<"Direccion final: "<<cola.devolverFinal()<<
		" . Elemento final: "<<cola.finalCola()<<endl;
		x=cola.quitar();
		cout<<" . "<<x<<endl;
	}
	cout<<"Direccion frente: "<<cola.devolverFrente()<<
	" . Elemento frente: "<<cola.frenteCola()<<endl;
	cout<<"Direccion final: "<<cola.devolverFinal()<<
	" . Elemento final: "<<cola.finalCola()<<endl;
}

int main()
{
	Cola cola;
	completarCola(cola);
	cola.insertar(777);
	cola.insertar(888);
	cola.insertar(999);
	cola.quitar();
	cola.quitar();
	mostrarCola(cola);
	return 0;
}
