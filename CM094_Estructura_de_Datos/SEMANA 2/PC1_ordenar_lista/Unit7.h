//---------------------------------------------------------------------------

#ifndef Unit7H
#define Unit7H
//---------------------------------------------------------------------------
#include <System.Classes.hpp>
#include <Vcl.Controls.hpp>
#include <Vcl.StdCtrls.hpp>
#include <Vcl.Forms.hpp>
//---------------------------------------------------------------------------
class TfrmOrdenamiento : public TForm
{
__published:	// IDE-managed Components
	TListBox *lbA1;
	TListBox *lbB5;
	TListBox *lbB4;
	TListBox *lbB3;
	TListBox *lbB2;
	TListBox *lbA2;
	TListBox *lbA3;
	TListBox *lbA4;
	TListBox *lbA5;
	TListBox *lbB1;
	TButton *btnGenerar;
	TButton *btnOrdenarLetra;
	TButton *btnSalir;
	TButton *btnOrdenarNum;
	TListBox *lbA6;
	TListBox *lbB6;
	void __fastcall btnSalirClick(TObject *Sender);
	void __fastcall btnGenerarClick(TObject *Sender);
	void __fastcall btnOrdenarNumClick(TObject *Sender);
	void __fastcall btnOrdenarLetraClick(TObject *Sender);
	//void __fastcall ListBox1Click(TObject *Sender);
private:	// User declarations
public:		// User declarations
	__fastcall TfrmOrdenamiento(TComponent* Owner);
};
//---------------------------------------------------------------------------
extern PACKAGE TfrmOrdenamiento *frmOrdenamiento;
//---------------------------------------------------------------------------
#endif
