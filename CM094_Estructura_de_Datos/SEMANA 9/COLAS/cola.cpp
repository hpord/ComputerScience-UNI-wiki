#include <iostream>
using namespace std;
class NodoCola
{
    
  public:
    NodoCola* siguiente;
    int elemento;
    NodoCola (int x){ 
        elemento = x;
        siguiente = 0; //NULL
    
    }

};

class Cola
{
  private:
    NodoCola* frente;
    NodoCola* final;
  public:
    Cola() //Constructor que crea la cola vacía
    {
    frente = final = 0; //NULL
    }
    void insertar(int elemento); //Inserta un elemento al final de la cola
    int quitar(); //Retira un elemento del frente de la cola
    int frenteCola(); //Devuelve el elemento del frente de la cola
    int finalCola(); //Devuelve el elemento del frente de la cola
    bool colaVacia(); //Verdadero si la cola esta vacía
    NodoCola* devolverFrente(); //Devuelve el nodo de el frente
    NodoCola* devolverFinal(); //Devuelve el nodo de el frente
};


NodoCola* Cola::devolverFrente()
{
    return frente;
}

NodoCola* Cola::devolverFinal()
{
    return final;
}

int Cola::frenteCola()
{
    if (colaVacia())
    {
        cout<<"Cola vacia: ";
        return 0; //NULL
    }
    else return frente -> elemento;

}

int Cola::finalCola()
{
    if (colaVacia())
    {
        cout<<"Cola vacia: ";
        return 0; //NULL
    }
    else return final -> elemento;

}

void Cola::insertar(int elemento)
{
    NodoCola* nuevo;
    nuevo = new NodoCola (elemento);
    if (colaVacia())
    {
        frente = nuevo;
    }
    else
    {
        (final -> siguiente) = nuevo;
    }
    final = nuevo;
}

bool Cola::colaVacia()
{

    if(frente == 0) //NULL
    frente=final=0;
    return frente == 0; //NULL

}

int Cola:: quitar()
    {
    if (colaVacia())
    {
        cout<<"Cola vacia, no se puede extraer.\n";
        return 0; //NULL
    }
    else
    {
        cout<<"Se elimino de la memoria el nodo: "<<frente;
        int x = (frente -> elemento);
        NodoCola* a = frente;
        frente = (frente -> siguiente);
        delete a;
        return x;
    }
}

void completarCola(Cola &cola)
{
    int x, n;
    cout<<"Cuantos elementos ingresara a la cola: ";
    cin>>n;
    cout<<"Digite el elemento y luego pulse Enter\n";
    for (int i = 0; i < n ; i++){
        cout<<"Direccion frente: "<<cola.devolverFrente()<<" . Elemento frente: "<<cola.frenteCola()<<endl;
        cout<<"Direccion final: "<<cola.devolverFinal()<<" . Elemento final: "<<cola.finalCola()<<endl;
        cout<<"indice "<<i<<": ";
        cin >> x;
        cola.insertar(x);
        }
    cout<<"Direccion frente: "<<cola.devolverFrente()<<" . Elemento frente: "<<cola.frenteCola()<<endl;
    cout<<"Direccion final: "<<cola.devolverFinal()<<" . Elemento final: "<<cola.finalCola()<<endl;
}

void mostrarCola(Cola &cola)
{
    int x;
    cout <<"\nElementos de la Pila:"<<endl;
    while (!cola.colaVacia()){
        cout<<"Direccion frente: "<<cola.devolverFrente()<<" . Elemento frente: "<<cola.frenteCola()<<endl;
        cout<<"Direccion final: "<<cola.devolverFinal()<<" . Elemento final: "<<cola.finalCola()<<endl;
        x = cola.quitar();
        cout << " . "<<x <<endl;
    }
        cout<<"Direccion frente: "<<cola.devolverFrente()<<" . Elemento frente: "<<cola.frenteCola()<<endl;
        cout<<"Direccion final: "<<cola.devolverFinal()<<" . Elemento final: "<<cola.finalCola()<<endl;
}


int main(){
    Cola cola;
    completarCola(cola);
    mostrarCola(cola);
    return 0;
}
 