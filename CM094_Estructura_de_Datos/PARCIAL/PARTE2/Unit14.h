//---------------------------------------------------------------------------

#ifndef Unit14H
#define Unit14H
//---------------------------------------------------------------------------
#include <System.Classes.hpp>
#include <Vcl.Controls.hpp>
#include <Vcl.StdCtrls.hpp>
#include <Vcl.Forms.hpp>
#include <Vcl.ExtCtrls.hpp>
#include <Vcl.Imaging.pngimage.hpp>
//---------------------------------------------------------------------------
class TfrmFecha : public TForm
{
__published:	// IDE-managed Components
	TLabel *Label1;
	TLabel *Label2;
	TLabel *Label3;
	TLabel *Label4;
	TEdit *txtDia;
	TEdit *txtMes;
	TEdit *txtAnio;
	TLabel *Label5;
	TButton *btnAceptar;
	TLabel *Label6;
	TLabel *Label7;
	TListBox *lstFI;
	TListBox *lstFO;
	TImage *Image1;
	TButton *btnSalir;
	TButton *btnOrdenar;
	TButton *btnReiniciar;
	void __fastcall btnSalirClick(TObject *Sender);
	void __fastcall btnReiniciarClick(TObject *Sender);
	void __fastcall FormActivate(TObject *Sender);
	void __fastcall btnAceptarClick(TObject *Sender);
	void __fastcall btnOrdenarClick(TObject *Sender);
private:	// User declarations
public:		// User declarations
	__fastcall TfrmFecha(TComponent* Owner);
};
//---------------------------------------------------------------------------
extern PACKAGE TfrmFecha *frmFecha;
//---------------------------------------------------------------------------
#endif
