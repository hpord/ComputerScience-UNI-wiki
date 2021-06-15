template <typename T>
class Nombre{
	private:
		T dato;
	public:
		Nombre(T data){
		dato=data;
		}
	T leer();
	void fijar(T data);
};

template <typename T>
T Nombre<T>::leer(){
  return dato;
}

template <typename T>
void Nombre<T>::fijar(T d){
	dato=d;
}

// Implementando el main
#include <iostream>
#include <string>
using namespace std;
int main(){
	Nombre<string>nombre1("Juan");
	cout<<nombre1.leer()<<endl;
	system("pause");
	return 0;
}

