//Arbol binario
#include <iostream>
#include <cmath>
using namespace std;
typedef string Tipo;
class Nodo
{
	private:
		Tipo dato;
		Nodo* izq;
		Nodo* der;
	public:
		Nodo (Tipo valor)//Constructor que inicializa el nodo como hoja
		{
			dato=valor;
			izq=der=NULL;
		}
		Nodo (Nodo* nodoIzq,Tipo valor,Nodo* nodoDer) //Constructor de subarbol con hijos
		{
			dato=valor;
			izq=nodoIzq;
			der=nodoDer;
		}
		//Operaciones de acceso
		Tipo valorNodo(){return dato;} //Devuelve el valor almacenado en el nodo
		Nodo* subArbolIzq(){return izq;} //Devuelve el nodo de la izquierda
		Nodo* subArbolDer(){return der;} //Devuelve el nodo de la derecha
		//Operaciones de modificacion
		void nuevoValor(Tipo d){dato=d;} //Asigna el valor (dato) del nodo
		void nodoIzq(Nodo *n){izq=n;} //Asigna un nodo a la izquierda
		void nodoDer(Nodo *n){der=n;} //Asigna un nodo a la izquierda
};
class ArbolB
{
	private:
	Nodo *raiz;
	public:
	ArbolB() //Constructor. Inicializa la raiz a un null, arbol vacio
	{
		raiz = NULL; //NULL
	}
	ArbolB(Nodo *r) //Constructor. Inicializa la raiz a un puntero a un Nodo
	{
		raiz = r;
	}
	//Funciones
	bool esVacio() // Devuelve verdadero si el arbol esta vacio
	{
		return raiz == NULL; 
	}
	Nodo raizArbol() // Devuelve el nodo raiz
	{
		if(raiz)
			return *raiz;
		else
			cout<<"arbol vacio";
	}
	Nodo * hijoIzq() // Devuelve el nodo izquierdo
	{
	if(raiz)
		return raiz->subArbolIzq();
	else
		cout<<"arbol vacio";
	}
	Nodo* hijoDer() // Devuelve el nodo derecho
	{
	if(raiz)
		return raiz->subArbolDer();
	else
		cout<<"arbol vacio";
	}
	Nodo* nuevoArbol(Nodo* nodoIzq, Tipo dato, Nodo* nodoDer) //Crea y Retorna un nuevo nodo
	{
		return new Nodo(nodoIzq, dato, nodoDer);
	}
	void Praiz( Nodo *r) //Fija el atributo raiz a un nodo
	{
		raiz = r;
	}
	Nodo * Oraiz() //Devuelve el puntero al nodo raiz
	{
		return raiz;
	}
};
int main()
{
	ArbolB a[15],ar;
	Nodo* n[15];
	//Nivel 3
	n[0]=a[0].nuevoArbol(NULL,"Benito",NULL);
	n[1]=a[1].nuevoArbol(NULL,"Federico",NULL);
	n[2]=a[2].nuevoArbol(NULL,"Rosa",NULL);
	n[3]=a[3].nuevoArbol(NULL,"Luis",NULL);
	n[4]=a[4].nuevoArbol(NULL,"Pedro",NULL);
	n[5]=a[5].nuevoArbol(NULL,"Ramon",NULL);
	n[6]=a[6].nuevoArbol(NULL,"Zulema",NULL);
	n[7]=a[7].nuevoArbol(NULL,"Pamela",NULL);
	//Nivel 2
	n[8]=a[8].nuevoArbol(n[0],"Maria",n[1]);
	n[9]=a[9].nuevoArbol(n[2],"Rodrigo",n[3]);
	n[10]=a[10].nuevoArbol(n[4],"Anyora",n[5]);
	n[11]=a[11].nuevoArbol(n[6],"Abel",n[7]);
	//Nivel 1
	n[12]=a[12].nuevoArbol(n[8],"Isabel",n[9]);
	n[13]=a[13].nuevoArbol(n[10],"Jesus",n[11]);
	//Nivel 0
	n[14]=a[14].nuevoArbol(n[12],"Esperanza",n[13]);
	ar.Praiz(n[14]);
	//mostrando el arbol
	cout<<"Nivel 0"<<endl;
	cout<<ar.Oraiz()->valorNodo()<<endl;
	cout<<"Nivel 1"<<endl;
	cout<<ar.Oraiz()->subArbolIzq()->valorNodo()<<"  ";
	cout<<ar.Oraiz()->subArbolDer()->valorNodo()<<endl;
	cout<<"Nivel 2"<<endl;
	cout<<ar.Oraiz()->subArbolIzq()->subArbolIzq()->valorNodo()<<"  ";
	cout<<ar.Oraiz()->subArbolIzq()->subArbolDer()->valorNodo()<<"  ";
	
	cout<<ar.Oraiz()->subArbolDer()->subArbolIzq()->valorNodo()<<"  ";
	cout<<ar.Oraiz()->subArbolDer()->subArbolDer()->valorNodo()<<endl;
	cout<<"Nivel 3"<<endl;
	cout<<ar.Oraiz()->subArbolIzq()->subArbolIzq()->subArbolIzq()->valorNodo()<<"  ";
	cout<<ar.Oraiz()->subArbolIzq()->subArbolIzq()->subArbolDer()->valorNodo()<<"  ";
	
	cout<<ar.Oraiz()->subArbolIzq()->subArbolDer()->subArbolIzq()->valorNodo()<<"  ";
	cout<<ar.Oraiz()->subArbolIzq()->subArbolDer()->subArbolDer()->valorNodo()<<"  ";
	
	cout<<ar.Oraiz()->subArbolDer()->subArbolIzq()->subArbolIzq()->valorNodo()<<"  ";
	cout<<ar.Oraiz()->subArbolDer()->subArbolIzq()->subArbolDer()->valorNodo()<<"  ";
	
	cout<<ar.Oraiz()->subArbolDer()->subArbolDer()->subArbolIzq()->valorNodo()<<"  ";
	cout<<ar.Oraiz()->subArbolDer()->subArbolDer()->subArbolDer()->valorNodo()<<endl;
	
	return 0;
}