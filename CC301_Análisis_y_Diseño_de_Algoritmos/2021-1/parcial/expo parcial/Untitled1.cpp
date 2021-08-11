// Programa en C++ que implementa el Algoritmo Greedy en la Coloracion de Grafos
#include <iostream> 
#include <list> 
using namespace std; 
  
// Clase que representa a un grafo no dirigido 
class Grafo 
{ 
    int V;    // Numero de vertices 
    list<int> *adj;    // Un array dinamico de listas de adyacencia 
public: 
    // Constructor y destructor 
    Grafo(int V)   { this->V = V; adj = new list<int>[V]; } 
    ~Grafo()       { delete [] adj; } 
  
    // Funcion que agrega una arista al grafo 
    void agregarArista(int v, int w); 
  
    // Imprime colores Greedy de los vertices 
    void greedyColoracion(); 
}; 
  
void Grafo::agregarArista(int v, int w) 
{ 
    adj[v].push_back(w); 
    adj[w].push_back(v);  // Nota: El grafo no está dirigido 
} 
  
// Asigna colores (comenzando desde 0) a todos los vertices e imprime la asignacion de colores 
void Grafo::greedyColoracion() 
{ 
    int resultado[V]; 
  
    // Asigna el primer color al primer vertice 
    resultado[0]  = 0; 
  
    // Inicializar los V-1 vertices restantes como no asignados 
    for (int u = 1; u < V; u++) 
        resultado[u] = -1;  // Ningun color esta asignado a V 
  
    // Un arreglo temporal para almacenar los colores disponibles. El verdadero valor
    // de available[cr] significaria que el color "cr" se asigna a uno de sus vertices adyacentes
    bool disponible[V]; 
    for (int cr = 0; cr < V; cr++) 
        disponible[cr] = false; 
  
    // Asignar colores a los V-1 vertices restantes
    for (int u = 1; u < V; u++) 
    { 
        // Procesa todos los vertices adyacentes y marca sus colores como no disponibles 
        list<int>::iterator i; 
        for (i = adj[u].begin(); i != adj[u].end(); ++i) 
            if (resultado[*i] != -1) 
                disponible[resultado[*i]] = true; 
  
        // Encuentra el primer color disponible
        int cr; 
        for (cr = 0; cr < V; cr++) 
            if (disponible[cr] == false) 
                break; 
  
        resultado[u] = cr; // Asigna el color encontrado
  
        // Resetea los valores a Falso para la siguiente iteracion 
        for (i = adj[u].begin(); i != adj[u].end(); ++i) 
            if (resultado[*i] != -1) 
                disponible[resultado[*i]] = false; 
    } 
  
    // Imprime el resultado 
    for (int u = 0; u < V; u++) 
        cout << "Vertice " << u << " --->  Color "
             << resultado[u] << endl; 
} 
  
int main() 
{ 
    Grafo g1(5); 
    g1.agregarArista(0, 1); 
    g1.agregarArista(0, 2); 
    g1.agregarArista(1, 2); 
    g1.agregarArista(1, 3); 
    g1.agregarArista(2, 3); 
    g1.agregarArista(3, 4); 
    cout << "Coloracion del grafo 1 \n------------------------- \n"; 
    g1.greedyColoracion(); 
  
    Grafo g2(5); 
    g2.agregarArista(0, 1);
    g1.agregarArista(1, 3);
    g2.agregarArista(1, 4); 
    g2.agregarArista(2, 4); 
    g2.agregarArista(4, 3); 
    cout << "\nColoracion del grafo 2 \n------------------------- \n"; 
    g2.greedyColoracion(); 
  
    return 0; 
} 
