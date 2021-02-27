/*
Autor: Cristhian Wiki Sánchez Sauñe
Curso: Algoritmos y estructura de datos
Fecha de creación v1: 07/09/2020
Tema: Grafos 4 - Lista de adyacencia
*/

#include <iostream>
#include <string>
#include <sstream>
using namespace std;
string IntToString (int);
int n_nodos, n_arcos;

class nodo
{
	public:
	class arco; //Contiene el destino del arco y la direccion del siguiente arco
				//El inicio es este nodo (self)
	string nombre; //nombre del nodo
	nodo* sgte; //puntero al siguiente nodo del directorio
	arco* ady; //puntero al primer arco de la lista de arcos del nodo
	nodo* p; //puntero al primer nodo de la lista nodos del directorio
	void insertarNodo(); //Inserta un nodo al directorio
	void mostrarGrafo(); //Muestra el grafo
	void insertarArco(); //Solicita los nombres del nodo inicial y final
						//Si los encuentra llama a agregarArco() pra crear el arco
	void agregarArco(nodo*,nodo*,arco*); //Crea el arco con los datos enviados por insertarArco()					
	void eliminarNodo(string);
	void borrarTodosArcos(nodo*);
	void mostrarArcos();
	void eliminarArco(string, string);
};

class nodo::arco
{
	public:
	nodo* destino; //puntero al nodo de llegada
	arco* sgte;
};
int numeroNodos(nodo*);


//////////////////////////////////////////////////////////////////////
void nodo::insertarNodo()
{
	nodo* t; //Contador que recorre todo el directorio
	nodo* nuevo=new nodo;//"nuevo" es el nodo que se insertara al directorio
	cout<<"ingrese su nombre: ";
	cin>>nuevo->nombre; //Se asigna un nombre al nuevo nodo
	nuevo->sgte=NULL; //nuevo no apunta aningun nodo
	nuevo->ady=NULL; //nuevo no apunta a ningun arco
	if(p==NULL) //Si el primer nodo del directorio es NULL
	{
		p=nuevo; //"nuevo" es el primer nodo del directorio (o sea la cabeza)
		cout<<"\t\t1er nodo del directorio\n";
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
		cout<<"\t\tNodo ingresado\n";
	}
}

void nodo::insertarArco()
{
	string ini,fin; //Son los nombres del nodo inicio y final del arco
	arco* nuevo=new arco(); //"nuevo" es el arco que se insertara y enlaza a los nodos inicio y final
	nodo* aux; //Contador que recorre la lista del directorio hasta encontrar el nodo inicial
	nodo* aux2; //Contador que recorre la lista del directorio hasta encontrar el nodo final
	if (p==NULL)
	{
		cout<<"Grafo vacio\n";
	}
	nuevo->sgte=NULL; //El "nuevo" arco no apunta a ningun arco
	cout<<"\t\tIngrese el nombre del nodo inicio (origen): ";
	cin>>ini;
	cout<<"\t\tIngrese el nombre del nodo final (destino): ";
	cin>>fin;
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

void nodo::agregarArco(nodo* aux,nodo* aux2, arco* nuevo)
{
	arco *q; //Contador que recorre todos los arcos de un nodo del directorio
	if(aux->ady==NULL) //Si el nodo aux no tiene ningun arco
	{
		aux->ady=nuevo; //entonces el primer arco del nodo es "nuevo" (la cabeza)
		nuevo->destino=aux2; //El destino del "nuevo" arco
		cout<<"\t\t1er arco del nodo\n\n";
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
		cout<<"\t\tArco agregado\n\n";
	}
}

////////////////////////////////////////////////////////////////////////////////

void nodo::eliminarNodo(string nom)
{
	//string nom;
	nodo* aux;
	nodo* ant;
	aux=p;
	if (p==NULL)
	{
		cout<<"Grafo vacio\n";
		return;
	}
	//cout<<"Ingrese el nombre del nodo a borrar: ";
	//cin>>nom;
	while(aux!=NULL)
	{
		if(aux->nombre==nom)
		{
			if(aux->ady!=NULL)
			{
				p->borrarTodosArcos(aux);
			}
			if(aux==p)
			{
				p=p->sgte;
				delete(aux);
				cout<<"Nodo cabeza eliminado\n";
				return;
			}
			else
			{
				ant->sgte=aux->sgte;
				cout<<"Nodo eliminado\n";
			 	delete(aux);
			 	return;
			} 
		}
		else
		{
			ant=aux;
			aux=aux->sgte;
		}
		
	}
}

void nodo::borrarTodosArcos(nodo* aux)
{
	arco* q;
	arco* r;
	q=aux->ady;
	while(q->sgte!=NULL)
	{
		r=q;
		q=q->sgte;
		delete(r);
	}

}

void nodo::eliminarArco(string ini, string fin)
{
	//string ini, fin; //nodos inicial y final del arco
	nodo* aux; //Contador que buscara el nodo con nombre "ini"
	nodo* aux2; //Contador que buscara el nodo con nombre "fin"
	arco* q; //Contador que recorre la lista de arcos
	arco* r; //Variable temporal que recuerda al arco anterior a q
	//cout<<"Ingrese el nombre del nodo inicio: ";
	//cin>>ini;
	//cout<<"Ingrese el nombre del nodo final: ";
	//cin>>fin;
	aux=p; //Inicializa aux a la cabeza del directorio
	aux2=p; //Inicializa aux2 a la cabeza del directorio
	while(aux2!=NULL) //Localiza el nodo que tiene nombre "fin"
	{
		if(aux2->nombre==fin) //Ese nodo se asigna a aux2
		{
		break;
		}
		else
		aux2=aux2->sgte; //avanza al siguiente nodo
	}
	if(aux2==NULL) return;
	while(aux!=NULL) //Localiza el nodo que tiene nombre "ini"
	{
		if(aux->nombre==ini) //Ese nodo se asigna a aux
		{
			q=aux->ady; //Asigna a q la cabecera de la lista de arcos
			while(q!=NULL) //recorre la lista de arcos
			{
				if(q->destino==aux2) //Comprueba si el destino del arco es el nodo aux2
				{
					if(q==aux->ady) //Si q es el nodo cabecera de la lista de arcos
					aux->ady=aux->ady->sgte; //La nueva cabecera es el nodo al que apuntaba q
					else //Si q no es la cabecera de la lista de arcos
					r->sgte=q->sgte; //el nodo siguiente al nodo anterior a q sera el nodo que sigue a q, de esa forma hace un puente
					delete(q); //elimina el arco q
					cout<<"Arco  "<<aux->nombre<<"----->"<<aux2->nombre<<" Eliminado\n";
					return;
				}
				r=q; //Almacena el arco actual
				q=q->sgte; //Avanza al arco siguiente
			}
		}
		aux = aux->sgte; //Avanza al sigueinte nodo
	}
}

///////////////////////////////////////////////////////////////////////////////

void nodo::mostrarArcos()
{
	nodo* aux; //Contador que recorre la lista directorio
	arco* ar; //Contador que recorre los arcos del nodo
	string nom; //nombre del nodo a analizar
	cout<<"Ingrese el nombre del nodo: ";
	cin>>nom;
	aux=p; //Inicializa el contador a la cabeza
	//de la lista directorio
	while(aux!=NULL)
	{
		if(aux->nombre==nom) //Si encuentra el nodo con el mismo nombre
		{
			if(aux->ady==NULL) //Si la cabeza de la lista de arcos es NULL
			{
				cout<<"El nodo no contiene arcos\n";
				return;
			}
			else
			{
				cout<<"Nodo\t|\tLista de adyacencia\n";
				cout<<aux->nombre<<"\t|"; //Imprime el nodo a analizar
				ar=aux->ady; //Obtiene el arco cabeza de la lista de arcos
				while(ar!=NULL)
				{
					cout<<ar->destino->nombre<<" "; //Imprime el nombre del nodo destino del arco
					ar=ar->sgte; //Avanza al siguiente arco
				}
				cout<<endl;
				return;
			}
		}
		else
		aux=aux->sgte; //Avanza al siguiente nodo del directorio
	}
}

void nodo::mostrarGrafo()
{
	nodo* t; //Contador que recorre todo el directorio
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

/////////////////////////////////////

void completarNodos(nodo *p)
{
	cout<<"Cuantos nodos ingresara: ";
	cin>>n_nodos;
	for(int i=1;i<=n_nodos;i++)
	{
		cout<<"\tNodo "<<i<<", ";
		p->insertarNodo();
	}
	cout<<endl;
}
void completarArcos(nodo *p)
{
	cout<<"Cuantos arcos ingresara: ";
	cin>>n_arcos;
	for(int i=1;i<=n_arcos;i++)
	{
		cout<<"\tArco "<<i<<": "<<endl;
		p->insertarArco();
	}
	cout<<endl;
}

/////////////////////////////////////


int main()
{
	nodo* p=new nodo;
	nodo* temporal;
	bool continuar=true;
	
	cout<<endl;
	cout<<"########################################################################"<<endl;
	cout<<"################      Grafos 4: lista de adyacencia    #################"<<endl;
	cout<<"################      Autor: Cristhian Wiki S. S.      #################"<<endl;
	cout<<"########################################################################\n\n"<<endl;
	
	completarNodos(p);
	completarArcos(p);
	
	cout<<"\nMostrando grafo:\n";
	p->mostrarGrafo();
	
	string nodo_eliminar;
	cout<<"Seleccione el nodo a eliminar: ";
	cin>>nodo_eliminar;
	
	while(continuar){
		
		string inferior, superior;
		superior=nodo_eliminar;
		temporal=p->p;
		
		n_nodos = numeroNodos(p);
		// El siguiente 'for' será dinámico
		
		for(int i=0; i<n_nodos; i++){
		
			inferior = temporal->nombre;
		
			if(inferior!=superior){
				p->eliminarArco(inferior, superior);
			}
			temporal = temporal->sgte;
		}
	
		p->eliminarNodo(nodo_eliminar);
		
		cout<<"\nMostrando grafo modificado:\n";
		p->mostrarGrafo();
		
		cout<<"\nIngrese otro nodo a eliminar (-1 para salir): ";
		cin>>nodo_eliminar;
		
		if(nodo_eliminar==IntToString(-1)){
			continuar=false;
		}
	}
	
	cout<<"\n\tHasta la proxima :D !!\n\n";	
	
	return 0;
}



///////// FUNCIONES AUXILIARES //////////


string IntToString (int a)
{
    stringstream temp;
    temp<<a;
    return temp.str();
}

int numeroNodos(nodo* p){
	int n_nod = 0;
	nodo* tmp;
	tmp = p->p;
	while(tmp!=NULL){
		n_nod+=1;
		tmp=tmp->sgte;
	}
	return n_nod;
}


/////////////////////////////////////////
