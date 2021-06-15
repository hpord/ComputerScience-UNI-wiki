/////////////////////////////////////////////////////////////////////////////////////////
//////////////////////// CRISTHIAN WIKI S¡NCHEZ SAU—E //////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////////
//Operaciones con BST
//Crear recursivo
#include <iostream>
using namespace std;
int veces;
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
Nodo *padreSucesor;
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
	int contarNodos(Nodo*);
	int encontrarAltura(Nodo*);
	void porAnchura(arbolBB);
	void verNivel(Nodo*,int);
	Nodo* busqueda(Nodo*,int);
	void borrarNodo(int);
};
void arbolBB::crear(int nuevoDato) //Crea la raiz
{
	if (raiz==NULL) //Si no tiene raiz, crea el nodo raiz
	{
		raiz=new Nodo;
		raiz->dato=nuevoDato;
		return;
	}
		Nodo *r=raiz;
		crear(r, nuevoDato); //Llamada a la funci√≥n recursiva
}


// Funcion recursiva
void arbolBB::crear(Nodo *r, int nuevoDato)
{
	if (nuevoDato < r->dato) // Si el nuevoDato es menor que el dato ra√≠z entonces se mueve a la izquierda
	{
		if(r->izq==NULL) // Si izq is NULL coloca el nuevoNodo a la izquierda.
		{
			Nodo *nuevoNodo;
		
			nuevoNodo=new Nodo;
			nuevoNodo->dato=nuevoDato;
			r->izq=nuevoNodo;
			return;
		}
		crear(r->izq, nuevoDato); // Si no mueve la ra√≠z al nodo de la izquierda
	}
    else
	{
		if (nuevoDato> r->dato) // Si el nuevoDato es mayor que el dato ra√≠z entonces se mueve a la derecha
		{
			if(r->der==NULL) // Si der is NULL coloca el nuevoNodo a la derecha.
			{
				Nodo *nuevoNodo=new Nodo;
				nuevoNodo->dato=nuevoDato;
				r->der=nuevoNodo;
				return;
			}
			crear(r->der, nuevoDato); // Si no mueve la ra√≠z al nodo de la derecha
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
		cout<<raiz->dato<<"    ";
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

//Contar nodos
int arbolBB::contarNodos(Nodo* raiz)
{
	int n=1;
	if (raiz->izq!=NULL)
		n=n+contarNodos(raiz->izq);
	if (raiz->der!=NULL)
		n=n+contarNodos(raiz->der);
	return n;
}

//Altura del nodo
int arbolBB::encontrarAltura(Nodo* raiz)
{
	if (raiz!=NULL)
		return max(encontrarAltura(raiz->izq),encontrarAltura(raiz->der))+1;
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

//Busqueda de un nodo
Nodo* arbolBB::busqueda(Nodo* raiz,int datoBuscado)
{
	Nodo *r;
	Nodo *rpta=NULL;
	r=raiz; //Se inicializa a la raiz del arbol
	while(r!=NULL)
	{
		if(r->dato==datoBuscado)
		{
			rpta=r;
			break;
		}
		if (datoBuscado<r->dato)
			r=r->izq;
		else
			r=r->der;
	}
}

///////////////////////NUEVA FUNCION/////////////////
Nodo *sucesor(Nodo *arbol){
	// Determinando el nodo m·s izquierdo posible 
	
	if(arbol==NULL){
		return NULL;
	}
	if(arbol->izq){
		padreSucesor=arbol;
		veces++;  // llevamos cuenta de cuantas veces giramos a la izquierda
		return sucesor(arbol->izq);
	}
	else{
		return arbol;
	}
}

///////////////////////NUEVA FUNCION/////////////////
void eliminarSucesor(Nodo *eliminar){
	// Usaremos la funciÛn anterior, para eliminar el sucesor
	
	if(eliminar->izq&&eliminar->der){
		veces=0; // este contador global me dir· si en la b˙squeda del sucesor 
				//  cuantas 'veces' se ha girado a la izquierda
		Nodo *suc = sucesor(eliminar->der);  // en la b˙squeda del sucesor, se comienza girando a la derecha (eliminar->der)
		eliminar->dato = suc->dato;
		
		
		// consideramos todas las opciones de cambio de nodo con 2 hijos
		if(suc->izq==NULL&&suc->der!=NULL&&veces>=1){
			padreSucesor->izq=suc->der;
		}
		else if(suc->izq==NULL&&suc->der==NULL&&veces==0){
			eliminar->der=NULL;
		}
		else if(suc->izq==NULL&&suc->der==NULL&&veces>=1){
			padreSucesor->izq=NULL;
		}
		else if(suc->izq==NULL&&suc->der!=NULL&&veces==0){
			
			eliminar->der=suc->der;
		
     	}	
	}
}

//Borrar nodos
//Borrar nodo
void arbolBB::borrarNodo (int datoBorrar)
{
	Nodo*r,*padre=NULL,*temp;
	r=raiz;
	while(r!=NULL) //Busca el dato a borrar
	{
		if(r->dato==datoBorrar)
			break;
		padre=r;
		if (datoBorrar < r->dato)
			r=r->izq;
		else
			r=r->der;
	} //Fin de la busqueda

	if(r==NULL)
	{
		cout<<" El dato no esta en el arbol"<<endl;
		return;
	}
	else if (padre->dato < r->dato) //Si el nodo objetivo esta a la derecha
	{
	 
		if ((r->der==NULL) && (r->izq!=NULL)) // Si r solo tiene hijo izquierdo
		{
			temp=r;
			padre->der=r->izq;
			delete temp;
		}
		else if ((r->der!=NULL) && (r->izq==NULL)) // Si r solo tiene hijo derecho
		{
			temp=r;
			padre->der=r->der;
			delete temp;
		}
		else if ((r->izq==NULL) &&(r->der==NULL)) // si r es una hoja
		{
			temp=r;
			padre->der=NULL;
			delete temp;
		}
		
		else if (r->izq && r->der) // si r tiene 2 hijos
	 	{
		    eliminarSucesor(r);   	    	
		}		
	}
   
	else if (padre->dato > r->dato) //Si el nodo objetivo esta a la izquierda
	{
		if ((r->der==NULL) && (r->izq!=NULL)) // Si r solo tiene hijo izquierdo
		{
			temp=r;
			padre->izq=r->izq;
			delete temp;
		}
		else if ((r->der!=NULL) && (r->izq==NULL)) // Si r solo tiene hijo derecho
		{
			temp=r;
			padre->izq=r->der;
			delete temp;
		}
		else if ((r->izq==NULL) &&(r->der==NULL)) // si r es una hoja
		{
			temp=r;
			padre->izq=NULL;
			delete temp;
		}
		
		else if (r->izq && r->der) // si r tiene 2 hijos
	 	{
		    eliminarSucesor(r);			    	
		}
	}		
}

//Funcion completar arbol
void completarArbol(arbolBB &a)
{
	int n, dato;
	cout<<"-> øCuantos nodos desea insertar (recursivo)? : ";
	cin>>n;
	cout<<endl;
	for (int i=1; i<=n;i++)
	{
		cout<<"  + Dato "<<i<<": ";
		cin>>dato;
		a.crear(dato);
	}
}

int main()
{
	arbolBB a;
	Nodo* x;
	int elim;
	bool seguir=true;
	
	cout<<"/////////////////////////////////////////////////////////////////////////////////////////"<<endl;
    cout<<"////////////////////////    ARBOL DE BUSQUEDA - BST   ///////////////////////////////////"<<endl;
    cout<<"/////////////////////////////////////////////////////////////////////////////////////////\n"<<endl;
	
	
	completarArbol(a);
	a.porAnchura(a);
	
	cout<<endl;
	cout<<"inOrden: ";
	a.enOrden(a.raiz);
	cout<<endl;
	
	while(seguir==true){
		cout<<"\n--> Ingrese el dato a eliminar (-1 salir): ";
		cin>>elim;
		if(elim==-1){
			seguir=false;
			cout<<"\n\tHasta luego :)!\n";
		}else{
			a.borrarNodo(elim);
			cout<<"\n--> Luego de borrar "<<elim<<":\n";
			a.porAnchura(a);
			
			cout<<endl;
				cout<<"inOrden: ";
				a.enOrden(a.raiz);
			cout<<endl;
			cout<<"-----------------------------------"<<endl;
			cout<<"\nsigamos..\n";
		}
    }	
	return 0;
}
