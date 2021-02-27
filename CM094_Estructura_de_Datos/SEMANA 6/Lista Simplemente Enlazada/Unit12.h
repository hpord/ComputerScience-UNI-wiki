//---------------------------------------------------------------------------

#ifndef Unit12H
#define Unit12H
//---------------------------------------------------------------------------
#include <System.Classes.hpp>
#include <Vcl.Controls.hpp>
#include <Vcl.StdCtrls.hpp>
#include <Vcl.Forms.hpp>
#include <Vcl.ExtCtrls.hpp>
#include <Vcl.Imaging.pngimage.hpp>
//---------------------------------------------------------------------------
class TForm12 : public TForm
{
__published:	// IDE-managed Components
	TListBox *lstDireccion;
	TLabel *Label5;
	TListBox *lstValor;
	TListBox *lstApunta;
	TLabel *Label6;
	TLabel *Label7;
	TPanel *pnlCreacion;
	TEdit *txtDato;
	TLabel *Label1;
	TLabel *Label2;
	TEdit *txtC;
	TEdit *txtLimInf;
	TLabel *Label3;
	TLabel *Label4;
	TEdit *txtLimSup;
	TButton *btnAleatorio;
	TRadioButton *rdbManual;
	TRadioButton *rdbAleatorio;
	TPanel *pnlOperaciones;
	TRadioButton *rdbInsercion;
	TRadioButton *rdbBusqueda;
	TRadioButton *rdbBorrado;
	TRadioButton *rdbModificar;
	TPanel *pnlInsercion;
	TRadioButton *rdbCabeza;
	TRadioButton *rdbCola;
	TRadioButton *rdbInsertarA;
	TRadioButton *rdbInsertarD;
	TLabel *Label8;
	TEdit *txtDatoIns;
	TButton *btnInsertar;
	TEdit *txtDatoRef;
	TLabel *lblInsertar;
	TPanel *pnlCoincidencia;
	TListBox *lstDireccionC;
	TListBox *lstValorC;
	TListBox *lstApuntaC;
	TLabel *Label11;
	TLabel *Label12;
	TLabel *Label13;
	TPanel *pnlBusqueda;
	TComboBox *cboDato;
	TLabel *Label10;
	TButton *btnBusqueda;
	TButton *btnAceptar;
	TLabel *Label9;
	TLabel *Label14;
	TLabel *Label15;
	TEdit *txtDireccion;
	TEdit *txtApunta;
	TEdit *txtValor;
	TImage *imgUNI;
	TLabel *lblCurso;
	TPanel *pnlBorrado;
	TLabel *Label16;
	TComboBox *cboDatoB;
	TButton *btnBorrar;
	TLabel *Label17;
	TEdit *txtDireccionB;
	TLabel *Label18;
	TEdit *txtValorB;
	TEdit *txtApuntaB;
	TLabel *Label19;
	TPanel *pnlModificar;
	TLabel *Label20;
	TComboBox *cboDatoM;
	TLabel *Label21;
	TEdit *txtNuevo;
	TButton *btnModificar;
	TButton *btnVoltear;
	TButton *btnLimpiar;
	void __fastcall FormCreate(TObject *Sender);
	void __fastcall rdbInsercionClick(TObject *Sender);
	void __fastcall rdbBusquedaClick(TObject *Sender);
	void __fastcall rdbBorradoClick(TObject *Sender);
	void __fastcall rdbModificarClick(TObject *Sender);
	void __fastcall rdbManualClick(TObject *Sender);
	void __fastcall rdbAleatorioClick(TObject *Sender);
	void __fastcall txtDatoKeyPress(TObject *Sender, System::WideChar &Key);
	void __fastcall btnAleatorioClick(TObject *Sender);
	void __fastcall btnVoltearClick(TObject *Sender);
	void __fastcall btnLimpiarClick(TObject *Sender);
	void __fastcall btnInsertarClick(TObject *Sender);
	void __fastcall rdbCabezaClick(TObject *Sender);
	void __fastcall rdbColaClick(TObject *Sender);
	void __fastcall rdbInsertarAClick(TObject *Sender);
	void __fastcall rdbInsertarDClick(TObject *Sender);
	void __fastcall btnBusquedaClick(TObject *Sender);
	void __fastcall btnBorrarClick(TObject *Sender);
	void __fastcall btnModificarClick(TObject *Sender);
	void __fastcall cboDatoMEnter(TObject *Sender);
	void __fastcall cboDatoBEnter(TObject *Sender);
	void __fastcall cboDatoEnter(TObject *Sender);


private:	// User declarations
public:		// User declarations
	__fastcall TForm12(TComponent* Owner);
};
//---------------------------------------------------------------------------
extern PACKAGE TForm12 *Form12;
//---------------------------------------------------------------------------
#endif
