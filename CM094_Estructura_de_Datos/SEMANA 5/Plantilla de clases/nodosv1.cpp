class Nodo{

	private:
		int dato;
		Nodo* puntero;
	public:
		Nodo(int d){
		   dato=d;
		   enlace=0;
		}
		Nodo(int d, Nodo* n){
		   dato=d;
		   enlace=n;
		}
		int datoNodo(){ //retorna el dato
		   return dato;
		}
		Nodo* enlaceNodo(){ //Retorna la direccion
		   return enlace;
		}
};
