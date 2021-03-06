//---------------------------------------------------------------------------

#ifndef Unit7H
#define Unit7H
//---------------------------------------------------------------------------
#include <System.Classes.hpp>
#include <Vcl.Controls.hpp>
#include <Vcl.StdCtrls.hpp>
#include <Vcl.Forms.hpp>
#include <Vcl.ExtCtrls.hpp>
//---------------------------------------------------------------------------
class TfrmIndirectos : public TForm
{
__published:	// IDE-managed Components
	TLabel *Label1;
	TEdit *txtN;
	TLabel *Label2;
	TLabel *Label3;
	TListBox *lstLista;
	TListBox *lstListaO;
	TButton *btnShell;
	TButton *btnQuickSort;
	TButton *btnSalir;
	TButton *btnLimpiar;
	TButton *btnCrear;
	TShape *Shape1;
	TMemo *mmoA;
	TMemo *mmoB;
	TMemo *mmoAB;
	TLabel *Label4;
	TLabel *Label5;
	TLabel *Label6;
	TLabel *Label7;
	TButton *btnMerge;
	TButton *btnHeap;
	TButton *btnMezclar;
	TButton *btnRadix;
	void __fastcall btnSalirClick(TObject *Sender);
	void __fastcall btnLimpiarClick(TObject *Sender);
	void __fastcall txtNKeyPress(TObject *Sender, System::WideChar &Key);
	void __fastcall btnCrearClick(TObject *Sender);
	void __fastcall btnShellClick(TObject *Sender);
	void __fastcall btnQuickSortClick(TObject *Sender);
	void __fastcall btnMezclarClick(TObject *Sender);
	void __fastcall btnMergeClick(TObject *Sender);
	void __fastcall btnHeapClick(TObject *Sender);
	void __fastcall btnRadixClick(TObject *Sender);
private:	// User declarations
public:		// User declarations
	__fastcall TfrmIndirectos(TComponent* Owner);
};
//---------------------------------------------------------------------------
extern PACKAGE TfrmIndirectos *frmIndirectos;
//---------------------------------------------------------------------------
#endif
