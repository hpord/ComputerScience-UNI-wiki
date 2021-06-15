// CRISTHIAN WIKI SANCHEZ SAUNE

#include <bits/stdc++.h> 
using namespace std; 
#define N 3 

// Nodo del árbol de búsqueda
struct Node 
{ 
	//  almacena el nodo principal del nodo actual ayuda a rastrear la ruta cuando se encuentra la respuesta
	Node* parent; 

	// contiene el costo de los nodos padres, incluido el nodo actual 
	int pathCost; 

	// contiene el costo menos prometedor
	int cost; 

	int cityID; 

	int containerID; 

	// La matriz booleana asignada contendrá información sobre los contenedores disponibles
	bool assigned[N]; 
}; 

// Función para asignar un nuevo nodo de árbol de búsqueda
// Aquí la ciudad x está asignada al contenedor y
Node* newNode(int x, int y, bool assigned[], 
			Node* parent) 
{ 
	Node* node = new Node; 

	for (int j = 0; j < N; j++) 
		node->assigned[j] = assigned[j]; 
	node->assigned[y] = true; 

	node->parent = parent; 
	node->cityID = x; 
	node->containerID = y; 

	return node; 
} 

// Función para calcular el costo menos prometedor del nodo después de que la ciudad x se asigne al contenedor y.
int calculateCost(int costMatrix[N][N], int x, 
				int y, bool assigned[]) 
{ 
	int cost = 0; 

	// para almacenar los contenedores no disponibles
	bool available[N] = {true}; 

	// empezar desde la siguiente ciudad
	for (int i = x + 1; i < N; i++) 
	{ 
		int min = INT_MAX, minIndex = -1; 

		// hacer para cada contenedor
		for (int j = 0; j < N; j++) 
		{ 
			// si el contenedor no es asignado
			if (!assigned[j] && available[j] && 
				costMatrix[i][j] < min) 
			{ 
				// guardamos el número del contenedor
				minIndex = j; 

				// guardamos el coste
				min = costMatrix[i][j]; 
			} 
		} 

		// agregar el costo de la próxima ciudad
		cost += min; 

		// contenedor deja de estar disponible 
		available[minIndex] = false; 
	} 

	return cost; 
} 

// Objeto de comparación que se utilizará para ordenar el montículo
struct comp 
{ 
	bool operator()(const Node* lhs, 
				const Node* rhs) const
	{ 
		return lhs->cost > rhs->cost; 
	} 
}; 


void printAssignments(Node *min) 
{ 
	if(min->parent==NULL) 
		return; 

	printAssignments(min->parent); 
	cout << "Asignando ciudad " << char(min->cityID + '1') 
		<< " para contenedor " << min->containerID << endl; 

} 

// Encontramos el mínimo usando ramificación y poda
int findMinCost(int costMatrix[N][N]) 
{ 
	// Cree una cola de prioridad para almacenar nodos en vivo del árbol de búsqueda;
	priority_queue<Node*, std::vector<Node*>, comp> pq; 

	// inicializar el montículo al nodo ficticio con un costo 0
	bool assigned[N] = {false}; 
	Node* root = newNode(-1, -1, assigned, NULL); 
	root->pathCost = root->cost = 0; 
	root->cityID = -1; 

	// Agregue un nodo ficticio a la lista de nodos activos;
	pq.push(root); 

	// Encuentra un nodo activo con el menor costo, 
	// agrega sus hijos a la lista de nodos activos y 
    // finalmente lo borra de la lista.
	while (!pq.empty()) 
	{ 
		// Encuentre un nodo activo con el menor costo estimado
		Node* min = pq.top(); 
	
		// El nodo encontrado se elimina de la lista de nodos activos.
		pq.pop(); 
	
		// i almacena la siguiente ciudad
		int i = min->cityID + 1; 
	
		// si todas las ciudades son asignadas a un contenedor
		if (i == N) 
		{ 
			printAssignments(min); 
			return min->cost; 
		} 
	
		// para cada contenedor
		for (int j = 0; j < N; j++) 
		{ 
			// Si no está asignado
			if (!min->assigned[j]) 
			{ 
			// crear un nuevo nodo de árbol
			Node* child = newNode(i, j, min->assigned, min); 
	
			// costo para los nodos padres, incluido el nodo actual
			child->pathCost = min->pathCost + costMatrix[i][j]; 
	
			// calcular su límite inferior
			child->cost = child->pathCost + 
				calculateCost(costMatrix, i, j, child->assigned); 
	
			// Agregar hijo a la lista de nodos activos 
			pq.push(child); 
			} 
		} 
	} 
} 

int main() 
{ 
	// coordenada 'x' representa una ciudad 
	// coordenada 'y' representa un contenedor 
	int costMatrix[N][N] = 
	{ 
		{30, 40, 70}, 
		{60, 20, 10}, 
		{40, 90, 30} 
	}; 

	cout << "\nEl coste optimo es "
		<< findMinCost(costMatrix); 

	return 0; 
} 

