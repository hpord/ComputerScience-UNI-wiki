//---------------------------------------------------------------------------

#ifndef Unit13H
#define Unit13H
//---------------------------------------------------------------------------
#include <System.Classes.hpp>
#include <Vcl.Controls.hpp>
#include <Vcl.StdCtrls.hpp>
#include <Vcl.Forms.hpp>
#include <Vcl.ExtCtrls.hpp>
#include <Vcl.Imaging.pngimage.hpp>
//---------------------------------------------------------------------------
class TfrmListaDoble : public TForm
{
__published:	// IDE-managed Components
	TLabel *Label1;
	TEdit *txtDato;
	TListBox *lstAtras;
	TListBox *lstDirDato;
	TListBox *lstDato;
	TListBox *lstAdelante;
	TButton *btnInsertarD;
	TButton *btnInsertarA;
	TButton *btnEliminar;
	TButton *btnModificar;
	TLabel *Label2;
	TLabel *Label3;
	TLabel *Label4;
	TLabel *Label5;
	TLabel *Label6;
	TEdit *txtNum;
	TEdit *txtDatoN;
	TLabel *Label7;
	TImage *Image1;
	TButton *btnVis;
	void __fastcall btnModificarClick(TObject *Sender);
	void __fastcall btnInsertarDClick(TObject *Sender);
	void __fastcall btnVisClick(TObject *Sender);
	void __fastcall btnInsertarAClick(TObject *Sender);
	void __fastcall txtDatoKeyPress(TObject *Sender, System::WideChar &Key);
	void __fastcall btnEliminarClick(TObject *Sender);
private:	// User declarations
public:		// User declarations
	__fastcall TfrmListaDoble(TComponent* Owner);
};
//---------------------------------------------------------------------------
extern PACKAGE TfrmListaDoble *frmListaDoble;
//---------------------------------------------------------------------------
#endif
