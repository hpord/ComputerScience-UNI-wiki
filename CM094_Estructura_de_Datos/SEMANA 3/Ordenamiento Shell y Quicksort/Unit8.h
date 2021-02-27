//---------------------------------------------------------------------------

#ifndef Unit8H
#define Unit8H
//---------------------------------------------------------------------------
#include <System.Classes.hpp>
#include <Vcl.Controls.hpp>
#include <Vcl.StdCtrls.hpp>
#include <Vcl.Forms.hpp>
//---------------------------------------------------------------------------
class TfrmOrdenacionV2 : public TForm
{
__published:	// IDE-managed Components
	TButton *bntLimpiar;
	TLabel *Label1;
	TListBox *lbLista;
	TButton *btnShell;
	TButton *btnQuicksort;
	TButton *btnSalir;
	TListBox *lbListaOrdenada;
	TLabel *Label2;
	TLabel *Label3;
	TEdit *txtNumero;
	TButton *btnAgregar;
	TButton *btnCrear;
	void __fastcall btnSalirClick(TObject *Sender);
	void __fastcall bntLimpiarClick(TObject *Sender);
	void __fastcall btnAgregarClick(TObject *Sender);
	void __fastcall txtNumeroKeyPress(TObject *Sender, System::WideChar &Key);
	void __fastcall btnCrearClick(TObject *Sender);
	void __fastcall btnShellClick(TObject *Sender);
	void __fastcall btnQuicksortClick(TObject *Sender);
private:	// User declarations
public:		// User declarations
	__fastcall TfrmOrdenacionV2(TComponent* Owner);
};
//---------------------------------------------------------------------------
extern PACKAGE TfrmOrdenacionV2 *frmOrdenacionV2;
//---------------------------------------------------------------------------
#endif
