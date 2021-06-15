#include <bits/stdc++.h>
 
using namespace std;
 
// Estructura de un archivo que almacena el peso y el valor correspondiente del archivo
struct File {
    int value, weight;
 
    // Constructor
    File(int value, int weight)
    {
       this->value=value;
       this->weight=weight;
    }
};
 
// Función de comparación para clasificar el archivo según la relación valor / peso
bool cmp(struct File a, struct File b)
{
    double r1 = (double)a.value / (double)a.weight;
    double r2 = (double)b.value / (double)b.weight;
    return r1 > r2;
}
 
// Función voraz principal para resolver el problema.
double fractionalKnapsack(int W, struct File arr[], int n)
{
    // 	clasificación de archivos según la proporción
    sort(arr, arr + n, cmp);
 
 
    int curWeight = 0; // Peso actual en mochila
    double finalvalue = 0.0; // Resultado (valor en mochila)
 
    // Recorrer todos los elementos
    for (int i = 0; i < n; i++) {
        // Si el elemento no se desborda, agréguelo por completo
        if (curWeight + arr[i].weight <= W) {
            curWeight += arr[i].weight;
            finalvalue += arr[i].value;
        }
 
        // Si no podemos agregar el elemento actual, agregue una parte fraccionaria 
        else {
            int remain = W - curWeight;
            finalvalue += arr[i].value
                          * ((double)remain
                             / (double)arr[i].weight);
            break;
        }
    }
 
    // Devolviendo valor final 
    return finalvalue;
}
 

int main()
{
    int W = 60; //    Tamaño de memoria máximo
    
    File arr[] = { { 1, 60}, { 1, 100}, { 1, 20}, { 1, 20}};  // PESO - VALOR (valor es constante)
 
    int n = sizeof(arr) / sizeof(arr[0]);
 
    cout << "\nValor maximo que podemos ocupar = "
         << fractionalKnapsack(W, arr, n);
    return 0;
}
