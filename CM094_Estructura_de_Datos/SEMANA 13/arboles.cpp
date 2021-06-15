//Clase 16 Grafos 2
#include <iostream>
#include <string>
using namespace std;
class Vertice
{
	private:
		string nombre;
		int numVertice;
	public:
		Vertice(){} //Vertice vacio
		Vertice(string x)
		{
			nombre=x;
			numVertice=-1;
		}
		Vertice(string x, int  n)
		{
			nombre=x;
			numVertice=n;
		}
		string ObtenernomVertice()
		{
			return nombre;
		}
		void FijarVertice(string nom)
		{
			nombre=nom;
		}
		bool igual(string n)
		{
			return nombre==n;
		}
		void FijarnumVertice(int n)
		{
			numVertice=n;
		}
		int ObtenernumVertice()
		{
			return numVertice;
		}
};
class GrafoMatriz
{
	private:
		int maxVerts; //maximo numero de vertices
		int numVerts; //numero actual de vertices
		Vertice* verts; //puntero a la clase Vertice (luego sera un vector)
		int** matAd; //puntero a puntero de enteros (luego sea la matriz)
	public:
		GrafoMatriz(int mx)
		{
			maxVerts=mx;
			verts=new Vertice[mx]; //Crea vector de vertices vacios
			matAd=new int*[mx]; //Crea vector de punteros a enteros
			numVerts=0; //Inicializa a 0 el numero inicial de vertices
			for (int i=0; i<mx;i++)
				matAd[i]=new int[mx]{};//Crea matriz de adyacencia con ceros
		}
		int ObtenervalorCelda(int i,int j){return matAd[i][j];}
		void FijarvalorCelda(int i,int j,int n){matAd[i][j]=n;}
		int ObtenernumDeVertices(){return numVerts;}
		int FijarnumDeVertices(int n){numVerts=n;}
		void nuevoVertice(string); //Crea un nuevo vertice y asigna automaticamente su 
									//numero de vertice
		int numVertice(string); //Devuleve el numero asignado al vertice
		void nuevoArco(string,string); //Crea un nuevo arco haciendo referencia a sus nombres
		void nuevoArco(int,int); //Crea un nuevo arco haciendo referencia a sus numeros de vertice
		void nuevoArco(int,int,int); //Crea un nuevo arco, el tercer agumento es el peso
		void nuevoArco(string,string,int); //Crea un nuevo arco, el tercer agumento es el peso
		int maxNumVertice(); //Determina el numero maximo de vertices
		bool adyacente(string, string);
		bool adyacente(int, int);
		int ObtenerValor(string, string);
		int ObtenerValor(int, int);
		void Pesovalor(string, string, int);
		void Pesovalor(int,int, int);
		Vertice Obtenervertice(int);
		Vertice Obtenervertice(string);
		void Reemplazarvertice( int, Vertice);
		void Reemplazarvertice( string, Vertice);
};
void GrafoMatriz::nuevoVertice(string nom)
{
	bool esta=(numVertice(nom)>=0);
	if (!esta)
	{
		Vertice v=Vertice(nom,numVerts);
		verts[numVerts]=v; //Se inserta en el vector de vertices
		numVerts=numVerts+1;
	}
}
int GrafoMatriz::numVertice(string nom)
{
	int i; //Posicion en el vector de vertices
	bool encontrado=false;
	for (i=0;i<numVerts;i++)
	{
		encontrado=verts[i].igual(nom);
		if (encontrado)
			return i;
	}
	return -1;
}
void GrafoMatriz::nuevoArco(string a,string b)
{
	int va,vb;
	va=numVertice(a);
	vb=numVertice(b);
	if (va<0 || vb<0)
		cout<<"Vertice no existe\n";
	else
		matAd[va][vb]=1;
}
void GrafoMatriz::nuevoArco(int va,int vb)
{
	if (va<0 || vb<0 || va>numVerts || vb>numVerts)
		cout<<"Vertice no existe\n";
	else
		matAd[va][vb]=1;
}
void GrafoMatriz::nuevoArco(int va,int vb, int peso)
{
	if (va<0 || vb<0 || va>numVerts || vb>numVerts)
		cout<<"Vertice no existe\n";
	else
		matAd[va][vb]=peso;
}
void GrafoMatriz::nuevoArco(string a,string b, int peso)
{
	int va,vb;
	va=numVertice(a);
	vb=numVertice(b);
	if (va<0 || vb<0)
		cout<<"Vertice no existe\n";
	else
		matAd[va][vb]=peso;
}
int GrafoMatriz::maxNumVertice(){return maxVerts;}
void completarGrafo(GrafoMatriz& grafo)
{
	int n=grafo.maxNumVertice();
	string nombre;
	cout<<"La cantidad maxima de nodos es: "<<n<<endl;
	for(int i=0;i<n;i++)
	{
		cout<<"nombre "<<i<<": ";
		cin>>nombre;
		grafo.nuevoVertice(nombre);
	}
}
void completarArcos(GrafoMatriz& grafo)
{
	int n,peso;
	string nomVert1,nomVert2;
	cout<<"Cuantos arcos creara: ";
	cin>>n; 
	cout<<"Ingrese los nombres de los vertices\n";
	for(int i=0;i<n;i++)
	{
		cout<<"Arco "<<i+1<<endl;
		cout<<"Vertice salida: ";
		cin>>nomVert1;
		cout<<"Vertice llegada: ";
		cin>>nomVert2;
		cout<<"Peso del arco: ";
		cin>>peso;
		grafo.nuevoArco(nomVert1,nomVert2,peso);
	}
}
void mostrarMatriz(GrafoMatriz& grafo)
{
	int n=grafo.maxNumVertice();
	cout<<"Mostrando la matriz:\n";
	for(int i=0;i<n;i++)
	{
		for(int j=0;j<n;j++)
		{
			cout<<grafo.ObtenervalorCelda(i,j)<<"   ";
		}
		cout<<endl;
	}
}
bool GrafoMatriz::adyacente(string a, string b)
{
	int va, vb;
	va = numVertice(a);
	vb = numVertice(b);
	if (va < 0 || vb < 0)
		cout<<"Vertice no existe\n";
	else
		return matAd[va][vb] >= 1;
}
bool GrafoMatriz::adyacente(int va, int vb)
{
if (va < 0 || vb < 0 || va >= numVerts || vb >= numVerts)
cout<<"Vertice no existe\n";
else
return matAd[va][vb] >= 1;
}
int GrafoMatriz::ObtenerValor(string a, string b)
{
	int va, vb;
	va = numVertice(a);
	vb = numVertice(b);
	if (va < 0 || vb < 0)
	cout<<"Vertice no existe\n";
	else
	return matAd[va][vb];
}
int GrafoMatriz::ObtenerValor( int va, int vb)
{
	if (va < 0 || vb < 0 || va >= numVerts || vb >= numVerts)
	cout<<"Vertice no existe\n";
	else
	return matAd[va][vb];
}
void GrafoMatriz::Pesovalor(string a, string b, int v)
{
	int va, vb;
	va = numVertice(a);
	vb = numVertice(b);
	if (va < 0 || vb < 0)
	cout<<"Vertice no existe\n";
	else
	matAd[va][vb] = v;
}
void GrafoMatriz::Pesovalor(int va, int vb, int v)
{
	if (va < 0 || vb < 0 || va >= numVerts || vb >= numVerts)
	cout<<"Vertice no existe\n";
	else
	matAd[va][vb] = v;
}
Vertice GrafoMatriz::Obtenervertice(int va)
{
	if (va < 0 || va >= numVerts)
		cout<<"Vertice no existe\n";
	else
		return verts[va];
}
Vertice GrafoMatriz::Obtenervertice(string a)
{
	int va=numVertice(a);
	if (va< 0)
		cout<<"Vertice no existe\n";
	else
		return verts[va];
}
void GrafoMatriz::Reemplazarvertice( int va, Vertice vert)
{
	if (va < 0 || va >= numVerts)
		cout<<"Vertice no existe\n";
	else 
	{
		vert.FijarnumVertice(verts[va].ObtenernumVertice());
		verts[va] = vert;
	}
}
void GrafoMatriz::Reemplazarvertice( string a, Vertice vert)
{
	int va=numVertice(a);
	if (va < 0 )
		cout<<"Vertice no existe\n";
	else 
	{
		vert.FijarnumVertice(verts[va].ObtenernumVertice());
		verts[va] = vert;
	}
}
///////////////////////////////////////

int main()
{
	GrafoMatriz grafo(5);
	Vertice verti;
	Vertice verti2("Z");
	//completarGrafo(grafo);
	//completarArcos(grafo);
	//mostrarMatriz(grafo);
	grafo.nuevoVertice("D");
	grafo.nuevoVertice("F");
	grafo.nuevoVertice("K");
	grafo.nuevoVertice("L");
	grafo.nuevoVertice("R");
	grafo.nuevoArco("D","K");//Tambien puede ingresar(0,2)
	grafo.nuevoArco("D","F");
	grafo.nuevoArco("F","K");
	grafo.nuevoArco("F","D");
	grafo.nuevoArco("L","K");
	grafo.nuevoArco("L","F");
	grafo.nuevoArco("R","D");
	grafo.Pesovalor("F","K",7);
	cout<<"Imprimiendo la matriz:\n";
	for(int i=0;i<5;i++)
	{
		for(int j=0;j<5;j++)
		{
			cout<<grafo.ObtenervalorCelda(i,j)<<"   ";
		}
		cout<<endl;
	}
	verti=grafo.Obtenervertice("L");
	cout<<verti.ObtenernomVertice()<<endl;
	cout<<verti.ObtenernumVertice()<<endl;
	grafo.Reemplazarvertice("L",verti2);
	verti=grafo.Obtenervertice("Z");
	cout<<verti.ObtenernomVertice()<<endl;
	cout<<verti.ObtenernumVertice()<<endl;
	return 0;
}