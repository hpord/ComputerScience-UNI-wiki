# include <iostream>
#include <vcl.h>
#include <stdio.h>
#include <string>
//Pila con Listas

using namespace std;
class NodoPila
{
	public:
	int elemento;
	NodoPila* siguiente;
	NodoPila(int x) //Constructor
	{
		elemento=x;
		siguiente=0; //NULL
	}
};
class PilaDina
{
	public:
	NodoPila* cima;
	PilaDina() //Constructor
	{
		cima=0;//NULL
	}
	void insertar(int elemento);
	int quitar(); //Solo mueve la cima
	int cimaPila();//Muestra el elemento de la cima
	bool pilaVacia();
	void limpiarPila(); // Si utiliza delete
};
void completarPila(PilaDina &pila)
{
	int x, n;
	cout<<"Cuantos elementos ingresara a la pila: ";
	cin>>n;
	cout<<"Digite el elemento y luego pulse Enter\n";
	for (int i = 0; i < n ; i++)
	{
		cout<<"Direccion cima: "<<pila.cima<<" . Elemento en la cima: "<<pila.cimaPila()<<endl;
		cout<<"indice "<<i<<": ";
		cin >> x;
		pila.insertar(x);
	}
	cout<<"Direccion cima: "<<pila.cima<<" . Elemento en la cima: "<<pila.cimaPila()<<endl;
}
void mostrarPila(PilaDina &pila)
{
	int x;
	cout <<"\nElementos de la Pila a retirar:"<<endl;
	while (!pila.pilaVacia())
	{
		cout<<"Direccion cima: "<<pila.cima<<" . Elemento en la cima: "<<pila.cimaPila()<<endl;
		x = pila.quitar();
		cout << x << "  ";
	}
	cout<<"Direccion cima: "<<pila.cima<<" . Elemento en la cima: "<<pila.cimaPila()<<endl;
}
void PilaDina::insertar(int elemento)
{
	NodoPila* nuevo;
	nuevo = new NodoPila(elemento);
	nuevo -> siguiente = cima;
	cima = nuevo;
}
int PilaDina::cimaPila()
{
	if (pilaVacia())
	{
		cout<<"Pila vacia\n";
		return 0; //NULL
	}
	else
		return cima->elemento;
}
bool PilaDina::pilaVacia()
{
	return cima == 0; //NULL
}
int PilaDina::quitar()
{
	if (pilaVacia())
	{
		cout<<"Pila vacia, no se puede extraer.\n";
		return 0; //NULL
	}
	else
	{
		int x = cima -> elemento;
		cima = cima -> siguiente;
		return x;
	}
}
void PilaDina:: limpiarPila()
{
	NodoPila* n;
	cout<<"Limpiar Pila: "<<endl;
	while(!pilaVacia())
	{
		cout<<"Direccion cima: "<<cima<<" . Elemento en la cima: "<<cimaPila()<<endl;
		n = cima;
		cima = cima -> siguiente;
		delete n;
	}
}
int main()
{
	PilaDina pila;
	completarPila(pila);
	mostrarPila(pila);
	return 0;	
}
/////////////////////////////////////////////////////
/////////////////////////////////////////////////////
/////////////////////////////////////////////////////
/////////////////////////////////////////////////////
//Pila con Arrays
typedef int TipoDato;
const int TAMPILA=6;
#include <iostream>
using namespace std;
class Pila
{
	private:
		int cima; //El indice del último elemento ingresado
		TipoDato listaPila[TAMPILA];
	public:
	Pila()
	{
		cima=-1;//Condicion de pila vacia
	}
	void insertar(TipoDato);
	TipoDato quitar();
	bool pilaVacia(); //verdadero si la pila esta vacia
	bool pilaLlena();
	void limpiarPila();
	TipoDato cimaPila(); //El elemento que esta en la cima
	int mostrarCima(); //Devuelve la cima
	int tamanoPila();	
};
void Pila::insertar(TipoDato elemento)
{
	if(pilaLlena())
	{
		cout<<"Desbordamiento (overflow)\n";
	}
	else
	{
		cima++;
		listaPila[cima]=elemento;
	}
}
bool Pila::pilaLlena()
{
	return cima==TAMPILA-1;
}
bool Pila::pilaVacia()
{
	return cima==-1;
}
int Pila::mostrarCima()//Devuelve la cima (que coincide indice del array)
{
	return cima;
}
TipoDato Pila::cimaPila()// Devuelve el elemento en la cima
{
	if (pilaVacia())
	{
		cout<<"Desbordamiento negativo, No hay mas elementos\n";
		return 0;
	}
	else
		return listaPila[cima];
}
TipoDato Pila::quitar()
{
	TipoDato x;
	if (pilaVacia())
	{
		cout<<"Desbordameinto negativo (underflow)\n";
		return 0; //NULL
	}
	else
	{
		x=listaPila[cima];
		cima--;
		return x;
	}
}
int Pila::tamanoPila()
{
	return TAMPILA;
}
void Pila::limpiarPila()
{
	cima=-1;
}
//////////////////////////
void completarPila(Pila &pila)
{
	TipoDato x;
	int n;
	cout<<"Cuantos elementos ingresara a la pila (max. 6):";
	cin>>n;
	cout<<"Escriba el elemento y pulse Enter:\n";
	for (int i=0;i<n;i++)
	{
		cout<<"Cima pila "<<pila.mostrarCima()<<" : " <<"Elemento cima "<<pila.cimaPila()<<endl;
		cout<<"Indice "<<i<<" : ";
		cin>>x;
		pila.insertar(x);
		//cout<<"Cima pila "<<pila.mostrarCima()<<" : " <<"Elemento cima "<<pila.cimaPila()<<endl;
	}
	cout<<"Cima pila "<<pila.mostrarCima()<<" : " <<"Elemento cima "<<pila.cimaPila()<<endl;
}
void mostrarPila(Pila &pila)
{
	TipoDato x;
	cout<<"\nElementos retirados de la pila:\n";
	while(!pila.pilaVacia())
	{
		cout<<"Cima pila "<<pila.mostrarCima()<<" : " <<"Elemento cima "<<pila.cimaPila()<<endl;
		x=pila.quitar();
		cout<<x<<"   ";
	//cout<<"Cima pila "<<pila.mostrarCima()<<" : " <<"Elemento cima "<<pila.cimaPila()<<endl;
	}
	cout<<"Cima pila "<<pila.mostrarCima()<<" : " <<"Elemento cima "<<pila.cimaPila()<<endl;
}
int main()
{
	Pila pila;
	int x;
	completarPila(pila);
	pila.insertar(777);
	pila.insertar(888);
	pila.quitar();
	pila.quitar();
	pila.quitar();
	mostrarPila(pila);
	return 0;
}
//////////////Solución Ejercicio 1////////////
#include <string>
int main()
{
	Pila pilaChar; //Crea la pila vacia
	TipoDato ch; //Son los caracteres de la palabra
	bool esPal; //Devuelve true si es palindromo
	string palabra;
	string palabraSE; //Es la palabra sin espacios
	cout<<"Escriba una frase o palabra:\n";
	getline(cin,palabra);
	for (int i=0;i<palabra.length();i++)
	{
		ch=toupper(palabra[i]);
		if (ch!=' ')
		{
			pilaChar.insertar(ch);
			palabraSE+=ch;
		}
	}
	//Comprobamos si es palindromo
	esPal=true;
	for (int i=0;esPal && !pilaChar.pilaVacia();i++)
	{
		ch=pilaChar.quitar();
		esPal=(ch==palabraSE[i]);
	}
	if(esPal)
		cout<<"La palabra SI es palindromo\n";
	else
		cout<<"La palabra NO es palindromo\n";

	Sleep(10000);
	return 0;
}

