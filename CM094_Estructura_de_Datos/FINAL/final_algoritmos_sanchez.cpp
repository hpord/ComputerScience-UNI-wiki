/////////////////////////////////////////////////////////////////////////////////////////
//////////////////////// CRISTHIAN WIKI SÁNCHEZ SAUÑE //////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////////
#include <iostream>
#include <string>
#include <sstream>
using namespace std;
string IntToString (int);
int n_nodos, n_arcos;
int veces, elementos=0, n;
int nodos_[20];


///////////////////// DECLARACIÓN DE LAS PRINCIPALES CLASES ////////////////////////////
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
	void enOrden(Nodo*);
	void porAnchura(arbolBB);
	int encontrarAltura(Nodo*);
	void verNivel(Nodo*,int);
	//////////EXAMEN FINAL///////
	void recorrido(Nodo*,int);
	//////////EXAMEN FINAL//////
};

class nodo_completo
{
	public:
	class arco; //Contiene el destino del arco y la direccion del siguiente arco
				//El inicio es este nodo (self)
	int nombre; //nombre del nodo
	nodo_completo* sgte; //puntero al siguiente nodo del directorio
	arco* ady; //puntero al primer arco de la lista de arcos del nodo
	nodo_completo* p; //puntero al primer nodo de la lista nodos del directorio
	void insertarNodo(int); //Inserta un nodo al directorio
	void mostrarGrafo(); //Muestra el grafo
	void insertarArco(int, int); //Solicita los nombres del nodo inicial y final
						//Si los encuentra llama a agregarArco() pra crear el arco
	void agregarArco(nodo_completo*,nodo_completo*,arco*); //Crea el arco con los datos enviados por insertarArco()
};

class nodo_completo::arco
{
	public:
	nodo_completo* destino; //puntero al nodo de llegada
	arco* sgte;
};

nodo_completo* p=new nodo_completo;

///////////////////////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////////////////////////
/*
  Nota: Las siguientes funciones, se usaron de la PC4
*/
void arbolBB::crear(int nuevoDato) //Crea la raiz
{
	if (raiz==NULL) //Si no tiene raiz, crea el nodo raiz
	{
		raiz=new Nodo;
		raiz->dato=nuevoDato;
		return;
	}
		Nodo *r=raiz;
		crear(r, nuevoDato); //Llamada a la funciÃ³n recursiva
}


// Funcion recursiva
void arbolBB::crear(Nodo *r, int nuevoDato)
{
	if (nuevoDato < r->dato) // Si el nuevoDato es menor que el dato raÃ­z entonces se mueve a la izquierda
	{
		if(r->izq==NULL) // Si izq is NULL coloca el nuevoNodo a la izquierda.
		{
			Nodo *nuevoNodo;
		
			nuevoNodo=new Nodo;
			nuevoNodo->dato=nuevoDato;
			r->izq=nuevoNodo;
			return;
		}
		crear(r->izq, nuevoDato); // Si no mueve la raÃ­z al nodo de la izquierda
	}
    else
	{
		if (nuevoDato> r->dato) // Si el nuevoDato es mayor que el dato raÃ­z entonces se mueve a la derecha
		{
			if(r->der==NULL) // Si der is NULL coloca el nuevoNodo a la derecha.
			{
				Nodo *nuevoNodo=new Nodo;
				nuevoNodo->dato=nuevoDato;
				r->der=nuevoNodo;
				return;
			}
			crear(r->der, nuevoDato); // Si no mueve la raÃ­z al nodo de la derecha
		}
	}
}


//Altura del nodo
int arbolBB::encontrarAltura(Nodo* raiz)
{
	if (raiz!=NULL)
		return max(encontrarAltura(raiz->izq),encontrarAltura(raiz->der))+1;
}

void arbolBB::verNivel(Nodo* raiz,int n)
{
	if (raiz!=NULL)
	{
		if(n==0)
			cout<<raiz->dato<<" ";
		verNivel(raiz->izq,n-1);
		verNivel(raiz->der,n-1);
	}
}

//Recorrer el arbol por anchura (por nivel)
void arbolBB::porAnchura(arbolBB a)
{
	int nivel=0,niveles;
	niveles=a.encontrarAltura(a.raiz)-1;
	cout<<endl;
	while(nivel<=niveles)
	{
		verNivel(a.raiz,nivel);
		nivel++;
		cout<<endl;
	}
}

//Funcion recursiva para enorden
void arbolBB::enOrden(Nodo *raiz)
{
	if (raiz!=NULL)
	{
		enOrden(raiz->izq);
		cout<<raiz->dato<<"    ";
		nodos_[elementos]=raiz->dato;
		elementos+=1;
		enOrden(raiz->der);
	}
}


/*
  Nota: La siguiente función es una variación del método 'busqueda'
*/
//////////////////////////////////////////////////////////////// 
//	ESTA FUNCIÓN ES CRUCIAL PARA EL PROBLEMA DE TRAZAR LOS ARCOS
void arbolBB::recorrido(Nodo* padre_absoluto,int hijo_final)
{
	Nodo *r;
	Nodo *rpta=NULL;
	r=padre_absoluto; //Se inicializa a la raiz del arbol
	while(r!=NULL)
	{
		if(r->dato==hijo_final)
		{
			rpta=r;
			p->insertarArco(hijo_final, padre_absoluto->dato); // SE TRAZAN LOS ARCOS
			break;
		}
		else{
		
			if (hijo_final<r->dato){
			
				r=r->izq;
				if(r->dato!=hijo_final){
					p->insertarArco(hijo_final, r->dato);   // SE TRAZAN LOS ARCOS
				}
				
			}
			else{
			
				r=r->der;
				if(r->dato!=hijo_final){
					p->insertarArco(hijo_final, r->dato);   // SE TRAZAN LOS ARCOS
				}
			}
		}
	}
}

/////////////////////////////////////////////////////////
//Funcion completar arbol
void completarArbol(arbolBB &a)
{
	int dato;
	cout<<"-> ¿Cuantos nodos desea insertar (recursivo)? : ";
	cin>>n;
	cout<<endl;
	for (int i=1; i<=n;i++)
	{
		cout<<"  + Dato "<<i<<": ";
		cin>>dato;
		a.crear(dato);
	}
}


/*
  Nota: Las siguientes funciones, se usaron de la PC5
*/

///////////////////////////////////////////////////////////////////////////////////////////////////////////////
void nodo_completo::insertarNodo(int nod)
{
	nodo_completo* t; //Contador que recorre todo el directorio
	nodo_completo* nuevo=new nodo_completo;//"nuevo" es el nodo que se insertara al directorio
	//cout<<"ingrese su nombre: ";
	nuevo->nombre = nod; //Se asigna un nombre al nuevo nodo
	nuevo->sgte=NULL; //nuevo no apunta aningun nodo
	nuevo->ady=NULL; //nuevo no apunta a ningun arco
	if(p==NULL) //Si el primer nodo del directorio es NULL
	{
		p=nuevo; //"nuevo" es el primer nodo del directorio (o sea la cabeza)
	}
	else
	{
		t=p; //t se inicializa al primer nodo del directorio
		while(t->sgte!=NULL) //Verifica si existe un nodo despÃºes de t
		{
			t=t->sgte; //Si es cierto, avanza al siguiente nodo
		}
		t->sgte=nuevo; //Cuando t apunte a NULL, significa que es el ultimo
						//entonces hacemos que apunte a "nuevo", y asi "nuevo" es el ultimo
	}
}


void nodo_completo::insertarArco(int ini, int fin)
{
	arco* nuevo=new arco(); //"nuevo" es el arco que se insertara y enlaza a los nodos inicio y final
	nodo_completo* aux; //Contador que recorre la lista del directorio hasta encontrar el nodo inicial
	nodo_completo* aux2; //Contador que recorre la lista del directorio hasta encontrar el nodo final
	
	
	nuevo->sgte=NULL; //El "nuevo" arco no apunta a ningun arco
	aux=p; //aux se inicializa al primer nodo del directorio
	aux2=p; //aux2 se inicializa al primer nodo del directorio
	while(aux2!=NULL) //Verifica que aun no se llega al final del directorio
	{
		if(aux2->nombre==fin)
		{
			break; //Si encontro el nombre sale de while
		}
		aux2=aux2->sgte; //Avanza al siguiente nodo
	}
	if (aux2==NULL) return; //Si no existe el nodo de nombre "fin"
	while(aux!=NULL) //Verifica que aun no se llega al final del directorio
	{
		if(aux->nombre==ini)
		{
			agregarArco(aux,aux2,nuevo); //Llama a la funcion agregarArco() que uno los nodos
										//aux y aux2
			return; 			
		}
		aux=aux->sgte; //Avanza al siguiente nodo
	}
	if (aux==NULL) return;
}

void nodo_completo::agregarArco(nodo_completo* aux,nodo_completo* aux2, arco* nuevo)
{
	arco *q; //Contador que recorre todos los arcos de un nodo del directorio
	if(aux->ady==NULL) //Si el nodo aux no tiene ningun arco
	{
		aux->ady=nuevo; //entonces el primer arco del nodo es "nuevo" (la cabeza)
		nuevo->destino=aux2; //El destino del "nuevo" arco
	}
	else
	{
		q=aux->ady; //si el nodo ya tiene arcos, q se incializa al primer arco
		while(q->sgte!=NULL) 
		{
			q=q->sgte; //Mientras sea diferente de NULL avanza
		}
		q->sgte=nuevo; //Coloca el arco "nuevo" al final
		nuevo->destino=aux2; //se fija el destino del "nuevo" arco a aux2
	}
}

/////////////////////////////////////////////////////////////////////////////
void nodo_completo::mostrarGrafo()
{
	nodo_completo* t; //Contador que recorre todo el directorio
	arco* ar;//Contador que recorre la lista de arcos
	t=p;
	cout<<"Nodo\t|\tLista de adyacencia\n";
	while (t!=NULL) //Verifica si el nodo t es NULL
	{
		cout<<t->nombre<<"\t|"; //Muestra el nombre del nodo
		if (t->ady!=NULL) //Si el nodo tiene un arco o sea tiene la cabeza
		{
			ar=t->ady; //Obtiene el primer arco del nodo t (la cabeza)
			while(ar!=NULL)
			{
				cout<<"  "<<ar->destino->nombre; //Muestra el nombre del nodo destino del arco
				ar=ar->sgte; //avanza al siguiente arco de la lista
			}
		}
		t=t->sgte; //Avanza al siguiente nodo
		cout<<endl;
	}
	cout<<endl;
}

///////////////////////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////////////////////////
// MÉTODO PRINCIPAL

int main()
{
	arbolBB a;
	int dato_;
	
	cout<<"/////////////////////////////////////////////////////////////////////////////////////////"<<endl;
    cout<<"////////////////////////          EXAMEN FINAL       ///////////////////////////////////"<<endl;
    cout<<"////////////////////////    Nombre: Cristhian Wiki   ///////////////////////////////////"<<endl;
    cout<<"/////////////////////////////////////////////////////////////////////////////////////////\n"<<endl;
	
	completarArbol(a);
	a.porAnchura(a);
	
	cout<<endl;
	cout<<"inOrden: ";
	a.enOrden(a.raiz);
	cout<<"\n"<<endl;
	
	for(int i=0; i<n; i++){
		p->insertarNodo(nodos_[i]);     //  todos los elementos del árbol binario se transforman en un grafo 'p'
	}
	
	for(int i=0; i<n; i++){
		// después de recorrer el grafo 'in orden', almacenamos las variables en el arreglo nodos_[]
		// apartir de un hijo determinado, trazamos la ruta hasta el padre
		if(int(a.raiz->dato)!=nodos_[i]){
			a.recorrido(a.raiz, nodos_[i]);    // dirigirse a la declaración de 'recorrido' para ver cómo se hacen los arcos
		}
	    
	}
	
	////////////// CONVERSIÓN LISTA DE ADYACENCIA //////////////////////////////
	cout<<"\nMostrando grafo:\n\n";
	p->mostrarGrafo();
	
	return 0;
	
}
























