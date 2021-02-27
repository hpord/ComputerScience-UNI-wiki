//---------------------------------------------------------------------------

#ifndef Unit16H
#define Unit16H
//---------------------------------------------------------------------------
#include <System.Classes.hpp>
#include <Vcl.Controls.hpp>
#include <Vcl.StdCtrls.hpp>
#include <Vcl.Forms.hpp>
//---------------------------------------------------------------------------
class TfrmGrafo : public TForm
{
__published:	// IDE-managed Components
	TLabel *Label1;
	TEdit *txtNodos;
	TButton *btnDibujar;
	TButton *btnCrearGrafo;
	TLabel *Label2;
	TLabel *Label3;
	void __fastcall btnDibujarClick(TObject *Sender);
	void __fastcall btnCrearGrafoClick(TObject *Sender);
private:	// User declarations

public:		// User declarations

	__fastcall TfrmGrafo(TComponent* Owner);
};
//---------------------------------------------------------------------------
extern PACKAGE TfrmGrafo *frmGrafo;
//---------------------------------------------------------------------------
#endif
