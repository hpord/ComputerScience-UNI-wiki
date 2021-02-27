//---------------------------------------------------------------------------

#ifndef Unit6H
#define Unit6H
//---------------------------------------------------------------------------
#include <System.Classes.hpp>
#include <Vcl.Controls.hpp>
#include <Vcl.StdCtrls.hpp>
#include <Vcl.Forms.hpp>
//---------------------------------------------------------------------------
class TORDENAMIENTO : public TForm
{
__published:	// IDE-managed Components
	TLabel *Label1;
	TEdit *txtNumero;
	TButton *btnAnadir;
	TButton *btnLimpiar;
	TLabel *Label2;
	TButton *btnSeleccion;
	TButton *btnInsercion;
	TButton *btnIntercambio;
	TListBox *lstLista;
	TButton *btnBurbuja;
	TLabel *Lista;
	TLabel *Label4;
	TListBox *lstListaOrd;
	TButton *btnSalir;
	TButton *btnCrear;
	void __fastcall btnSalirClick(TObject *Sender);
	void __fastcall btnAnadirClick(TObject *Sender);
	void __fastcall txtNumeroKeyPress(TObject *Sender, System::WideChar &Key);
	void __fastcall btnLimpiarClick(TObject *Sender);
	void __fastcall btnIntercambioClick(TObject *Sender);
	void __fastcall btnCrearClick(TObject *Sender);
	void __fastcall btnSeleccionClick(TObject *Sender);
	void __fastcall btnInsercionClick(TObject *Sender);
	void __fastcall btnBurbujaClick(TObject *Sender);
	//void __fastcall FormKeyPress(TObject *Sender, System::WideChar &Key);
	//void __fastcall txtNumeroKeyPress(TObject *Sender, System::WideChar &Key);
private:	// User declarations
public:		// User declarations
	__fastcall TORDENAMIENTO(TComponent* Owner);
};
//---------------------------------------------------------------------------
extern PACKAGE TORDENAMIENTO *ORDENAMIENTO;
//---------------------------------------------------------------------------
#endif
