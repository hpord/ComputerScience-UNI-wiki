////////////BICOLA///////////
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
class Bicola
{
	private:
		NodoCola* frente;
		NodoCola* final;
	public:
	Bicola()//Constructor que cera la Bicola
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
	//Funciones adiconales para la Bicola
	void ponerFinal(int elemento); //Equivalente a insertar()
	void ponerFrente(int elemento);
	int quitarFrente(); //Equivalente a quitar
	int quitarFinal();
	int frenteBicola(); //Equivalente a frenteCola
	int finalBicola();
	bool bicolaVacia(); //Equivalente a colaVacia
	int numElemsBicola(); //Devuelve al cantidad de elementos de la bicola
};
/////////////////////
//Proviene de la Cola
/////////////////////
//Devuelve el nodo que esta al frente
NodoCola* Bicola::devolverFrente()
{
	return frente;
}
//Devuelve el nodo que esta al final
NodoCola* Bicola::devolverFinal()
{
	return final;
}
//Devuelve el elemento que esta en el frente
int Bicola::frenteCola()
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
int Bicola::finalCola()
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
void Bicola::insertar(int elemento)
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
bool Bicola::colaVacia()
{
	if(frente==0)//En Dev C++ NULL=0
		frente=final=0;
	return frente==0;
}
//Elimina los nodos desde el frente
int Bicola::quitar()
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
/////////////////////////
/////Funciones de Bicola
////////////////////////////////
//Poner elemento al frente
void Bicola::ponerFrente(int elemento)
{
	NodoCola* nuevo;
	nuevo = new NodoCola(elemento);
	if (bicolaVacia())
	{
		final = nuevo;
	}
	else
	{
		(nuevo -> siguiente)= frente;
	}
	frente = nuevo;
}
//Quitar elemento del final
int Bicola::quitarFinal()
{
	int x;
	if (!bicolaVacia())
	{
	if (frente == final) // Bicola dispone de un solo nodo
	{
		x = quitar();
	}
	else
	{
		cout<<"Se elimino de la memoria el nodo: "<<final;
		NodoCola* a = frente;
		while (a -> siguiente != final)
			a = a -> siguiente;
		x = final -> elemento;
		final = a;
		delete (a -> siguiente);
		final->siguiente=NULL;
	}
	}
	else
	{
	cout<<"Bicola vacia\n";
	return 0; //NULL
	}
	return x;
}
//Devuelve el elemento final
int Bicola::finalBicola()
{
	if (bicolaVacia())
	{
	cout<<"Error: bicola vacia\n";
	return 0; //NULL
	}
	return (final -> elemento);
}
//Devuelve la cantidad de elementos de la Bicola
int Bicola::numElemsBicola()
{
	int n = 0;
	NodoCola* a = frente;
	if (!bicolaVacia())
	{
		n = 1;
		while (a != final)
		{
			n++;
			a = a -> siguiente;
		}
	}
	return n;
}
//Funciones equivalentes
void Bicola::ponerFinal(int elemento)
{
	insertar(elemento); 
}
int Bicola::frenteBicola()
{
	return frenteCola(); 
}
int Bicola::quitarFrente()
{
	return quitar(); 
}
bool Bicola::bicolaVacia()
{
	return colaVacia();
}
///////////////////////////////
///////////////////////////////
//Completa la cola desde el final
void completarBicola(Bicola &bicola)
{
	int x,n;
	cout<<"Cuantos elementos ingresara a la cola: ";
	cin>>n;
	cout<<"Digite el elemento y luego pulse Enter\n";
	for (int i=1;i<=n;i++)
	{
		cout<<"Direccion frente: "<<bicola.devolverFrente()<<
		" . Elemento frente: "<<bicola.frenteCola()<<endl;
		cout<<"Direccion final: "<<bicola.devolverFinal()<<
		" . Elemento final: "<<bicola.finalCola()<<endl;
		cout<<"Indice "<<i<<": ";
		cin>>x;
		bicola.ponerFrente(x);
	}
	cout<<"Direccion frente: "<<bicola.devolverFrente()<<
	" . Elemento frente: "<<bicola.frenteCola()<<endl;
	cout<<"Direccion final: "<<bicola.devolverFinal()<<
	" . Elemento final: "<<bicola.finalCola()<<endl;
}
//Muestra la cola desde el frente
void mostrarBicola(Bicola &bicola)
{
	int x;
	cout<<"\nMostrando los elementos de la cola:\n";
	while(!bicola.colaVacia())
	{
		cout<<"Direccion frente: "<<bicola.devolverFrente()<<
		" . Elemento frente: "<<bicola.frenteCola()<<endl;
		cout<<"Direccion final: "<<bicola.devolverFinal()<<
		" . Elemento final: "<<bicola.finalCola()<<endl;
		x=bicola.quitarFinal();
		cout<<" . "<<x<<endl;
	}
	cout<<"Direccion frente: "<<bicola.devolverFrente()<<
	" . Elemento frente: "<<bicola.frenteCola()<<endl;
	cout<<"Direccion final: "<<bicola.devolverFinal()<<
	" . Elemento final: "<<bicola.finalCola()<<endl;
}
int main()
{
	Bicola bicola;
	completarBicola(bicola);
	cout<<"\nCantidad de elementos: "<<bicola.numElemsBicola()<<endl;
	bicola.ponerFrente(999);
	bicola.ponerFinal(888);
	cout<<"\nCantidad de elementos: "<<bicola.numElemsBicola()<<endl;
	mostrarBicola(bicola);
	cout<<"\nCantidad de elementos: "<<bicola.numElemsBicola()<<endl;
	return 0;
}