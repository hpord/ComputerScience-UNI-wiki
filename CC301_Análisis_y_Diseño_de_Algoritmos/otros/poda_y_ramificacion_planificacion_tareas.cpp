//  Programa para resolver el problema de asignación 
// de trabajos utilizando Branch y Bound


#include <bits/stdc++.h> 
using namespace std; 
#define N 4 
  
// nodo del árbol del espacio de estado
struct Node { 
    // almacena el nodo padre del nodo actual
    // ayuda a rastrear la ruta cuando se encuentra la respuesta
    Node* parent; 
  
    // contiene el costo de los nodos ancestros (padres)
    // incluido el nodo actual
    int pathCost; 
  
    // contiene el costo menos prometedor
    int cost; 
  
    // contener el ID del trabajador
    int workerID; 
  
    // contiene ID de trabajo
    int jobID; 
  
    // La matriz booleana asignada contendrá
    // información sobre los trabajos disponibles
    bool assigned[N]; 
}; 
  
// Función para asignar un nuevo nodo de árbol de búsqueda
// Aquí la Persona x está asignada al trabajo y
Node* newNode(int x, int y, bool assigned[], Node* parent) { 
    Node* node = new Node; 
  
    for (int j = 0; j < N; j++) node->assigned[j] = assigned[j]; 
    
    
    node->assigned[y] = true; 
  
    node->parent = parent; 
    node->workerID = x; 
    node->jobID = y; 
  
    return node; 
} 
  
// Función para calcular el costo menos prometedor
// del nodo después de que el trabajador x se asigne al trabajo y.
int calculateCost(int costMatrix[N][N], int x, int y, bool assigned[]) { 
    int cost = 0; 
  
    // para almacenar los trabajos no disponibles
    bool available[N] = {true}; 
  
    // empezar desde el siguiente trabajador
    for (int i = x + 1; i < N; i++){ 
        int min = INT_MAX, minIndex = -1; 
  
        // hacer para cada trabajo
        for (int j = 0; j < N; j++){ 
            // si el trabajo no está asignado
            if (!assigned[j] && available[j] && costMatrix[i][j] < min){ 
                // almacena el número de trabajador
                minIndex = j; 
  
                // almacena el coste
                min = costMatrix[i][j]; 
            } 
        } 
  
        // Agregar costo del próximo trabajador
        cost += min; 
  
        // el trabajo deja de estar disponible
        available[minIndex] = false; 
    } 
  
    return cost; 
} 
  
// Objeto de comparación que se utilizará para ordenar el montículo 'heap'
struct comp { 
    bool operator()(const Node* lhs, const Node* rhs) const { 
        return lhs->cost > rhs->cost; 
    } 
}; 
  
// imprimir asignaciones
void printAssignments(Node *min) { 
    if(min->parent==NULL) return; 
  
    printAssignments(min->parent); 
    cout << "Asignar trabajador " << char(min->workerID + 'A') 
         << " para el trabajo " << min->jobID + 1<< endl; 
  
} 
  
// Encuentra el costo mínimo usando Branch y Bound.
int findMinCost(int costMatrix[N][N]) 
{ 
    // Cree una cola de prioridad para almacenar nodos del árbol de búsqueda; 
    priority_queue<Node*, std::vector<Node*>, comp> pq; 
  
    // inicializar el montículo en el nodo ficticio con costo 0
    bool assigned[N] = {false}; 
    Node* root = newNode(-1, -1, assigned, NULL); 
    root->pathCost = root->cost = 0; 
    root->workerID = -1; 
  
    // Agregue un nodo ficticio a la lista de nodos activos;
    pq.push(root); 
  
    // Encuentra un nodo activo con el menor costo,
    // agrega sus hijos a la lista de nodos y
    // finalmente lo borra de la lista.
    while (!pq.empty()){ 
      // Encuentre un nodo activo con el menor costo estimado
      Node* min = pq.top(); 
  
      // El nodo encontrado se elimina de la lista de
      // nodos en vivo
      pq.pop(); 
  
      // i almacena al próximo trabajador
      int i = min->workerID + 1; 
  
      // Si a todos los trabajadores se les asigna un trabajo.
      if (i == N){ 
          printAssignments(min); 
          return min->cost; 
      } 
  
      // hacer para cada trabajo 
      for (int j = 0; j < N; j++){ 
        // Si no está asignado
        if (!min->assigned[j]) { 
          // crear un nuevo nodo de árbol
          Node* child = newNode(i, j, min->assigned, min); 
  
          // costo para los nodos ancestros, incluido el nodo actual
          child->pathCost = min->pathCost + costMatrix[i][j]; 
  
          // calcular su límite inferior
          child->cost = child->pathCost + 
            calculateCost(costMatrix, i, j, child->assigned); 
  
          // Agregar hijo a la lista de nodos en vivo;
          pq.push(child); 
        } 
      } 
    } 
} 
  
  
  
  
int main(){ 
    // La coordenada x representa un trabajador 
	// la coordenada y representa un trabajo
	
    int costMatrix[N][N] = { 
        {9, 2, 7, 8}, 
        {6, 4, 3, 7}, 
        {5, 8, 1, 8}, 
        {7, 6, 9, 4} 
    }; 
  
  
    /* int costMatrix[N][N] = { 
        {82, 83, 69, 92}, 
        {77, 37, 49, 92}, 
        {11, 69,  5, 86}, 
        { 8,  9, 98, 23} 
    }; 
    */
  
    /* int costMatrix[N][N] = { 
        {2500, 4000, 3500}, 
        {4000, 6000, 3500}, 
        {2000, 4000, 2500} 
    };*/
  
    /*int costMatrix[N][N] = { 
        {90, 75, 75, 80}, 
        {30, 85, 55, 65}, 
        {125, 95, 90, 105}, 
        {45, 110, 95, 115} 
    };*/
  
  
    cout << "\nEl costo optimo es : "
        << findMinCost(costMatrix); 
  
    return 0; 
}
