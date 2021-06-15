//PILA DINAMICA
#include <iostream>
using namespace std;
class NodoPila{
	public:
	int elemento;
	NodoPila* siguiente;
	NodoPila(int x) //Constructor
	{
		elemento = x;
		siguiente = NULL;
	}
	
};
class PilaDina{
	public:
	NodoPila* cima;
	PilaDina () //Constructor
	{
	cima = NULL; 
	}
	void insertar(int);
	int quitar();
	int cimaPila(); 
	bool pilaVacia(); 
	void limpiarPila();
	void visualizarPila();
	void crearPila();
};

void PilaDina::insertar(int elemento){
	NodoPila* nuevo;
	nuevo = new NodoPila(elemento);
	nuevo -> siguiente = cima;
	cima = nuevo;
}

void PilaDina::visualizarPila(){
	int dato;
	cout <<"\nElementos de la Pila:"<<endl;
	while(!pilaVacia()){
		cout<<"Direccion cima: "<<cima<<" . Elemento en la cima: "<<cimaPila()<<endl;
		dato = quitar();
		cout <<"Se retiro: "<< dato << endl;
	}
	cout<<"Al terminar queda:\n";
	cout<<"Direccion cima: "<<cima<<" . Elemento en la cima: "<<cimaPila()<<endl;
}

bool PilaDina::pilaVacia(){
	return cima == NULL;
}

int PilaDina::cimaPila(){
	if (pilaVacia()){
		cout<<"Pila vacia\n";
		return NULL;
	}
	else
		return cima->elemento;
}
	
int PilaDina::quitar(){
	NodoPila* n;
	if (pilaVacia()){
		cout<<"Pila vacia, no se puede extraer.\n";
	}
	else{
		n = cima;
		int x = cima -> elemento;
		cima = cima -> siguiente;
		delete n;
		return x;
	}

}

void PilaDina::crearPila(){
	int dato,n;
	cout<<"Cuantos elementos desea ingresar: ";
	cin>>n;
	for (int i=0; i<n; i++){
		cout<<"Direccion cima: "<<cima<<" . Elemento en la cima: "<<cimaPila()<<endl;
		cout<<"Ingrese el dato ("<<i<<"): ";
		cin>>dato;
		insertar(dato);
	}
	cout<<"Direccion cima: "<<cima<<" . Elemento en la cima: "<<cimaPila()<<endl;
}

void PilaDina::limpiarPila(){
	/*NodoPila *indice;
	for(indice=cima;indice!=NULL;indice=indice->siguiente){
	delete indice;
	}
	cima=NULL;*/
	NodoPila *n;
	cout<<"Limpiando la Pila:\n";
	while(!pilaVacia()){
		cout<<"Direccion cima: "<<cima<<" . Elemento en la cima: "<<cimaPila()<<endl;
		n=cima;
		cima=cima->siguiente;
		delete n;
	}

}

int ackermann_r(int m, int n) {
    if(m == 0) {
        return n + 1;
    } else if(n == 0) {
        return ackermann_r(m - 1, 1);
    } else {
        return ackermann_r(m - 1, ackermann_r(m, n - 1));
    }
}

int ackermann_i(int m, int n, PilaDina &pila) {
	
    pila.insertar(m);
	while(!pila.pilaVacia()){
	    m=pila.quitar();
	    if(m==0) n+=m+1;
	    else if(n==0){
	       n += 1;
	       pila.insertar(--m);
	    }
	    else{
	        pila.insertar(--m);
	        pila.insertar(++m);
	        n--;
    	}
	}

	return n;
}


/////////////////////////
int main(){
	PilaDina pila;
	int m=3, n=2, ack_seq=0, ack_rec=0;
	/*pila.insertar(7);
	pila.insertar(6);
	pila.insertar(5);
	pila.insertar(4);
	pila.insertar(3);*/
	//pila.crearPila();
	//pila.limpiarPila();
	cout<<"\nPila antes de ejecutar el algoritmo de ackermann\n";
	pila.visualizarPila();
	cout<<endl;
	cout<<"Valor de m: "<<m<<endl;
	cout<<"Valor de n: "<<n<<endl;
	
	cout<<"\n-----------------------------------------";
	cout<<"\n\nEjecutando el algoritmo de ackermann\n";
	ack_seq = ackermann_i(m, n, pila);
	ack_rec = ackermann_r(m, n);
	
	cout<<"\n\nSolucion recursiva: "<<ack_rec<<"\tSolucion iterativa: "<<ack_seq<<endl;
	return 0;
}
