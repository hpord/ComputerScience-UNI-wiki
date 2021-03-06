//---------------------------------------------------------------------------

#include <vcl.h>
#pragma hdrstop

#include "Unit14.h"
//---------------------------------------------------------------------------
#pragma package(smart_init)
#pragma resource "*.dfm"
#include <string>



TfrmFecha *frmFecha;
void ordBurbuja(int[], int);
int tamano=0;
int *listaFechaSuma, *indices;
//---------------------------------------------------------------------------
__fastcall TfrmFecha::TfrmFecha(TComponent* Owner)
	: TForm(Owner)
{
}
//---------------------------------------------------------------------------
void __fastcall TfrmFecha::btnSalirClick(TObject *Sender)
{
	frmFecha->Close();
}
//---------------------------------------------------------------------------
void __fastcall TfrmFecha::btnReiniciarClick(TObject *Sender)
{
   lstFI->Clear();
   lstFO->Clear();
   txtDia->SetFocus();
}
//---------------------------------------------------------------------------

void __fastcall TfrmFecha::FormActivate(TObject *Sender)
{
   txtDia->SetFocus();
}
//---------------------------------------------------------------------------

void __fastcall TfrmFecha::btnAceptarClick(TObject *Sender)
{
  if( txtDia->Text!="" && txtMes->Text!="" && txtAnio->Text!=""){

	 String fecha;
	 if( (1<=StrToInt(txtDia->Text) && StrToInt(txtDia->Text)<=31)
		  && (1<=StrToInt(txtMes->Text) && StrToInt(txtMes->Text)<=12)
		  && (1900<StrToInt(txtAnio->Text) && StrToInt(txtAnio->Text)<2100)
		  && (StrToInt(txtAnio->Text)%4 == 0 )){

		  fecha = txtDia->Text + "/" + txtMes->Text + "/" +  txtAnio->Text;
		  lstFI->Items->Add(fecha);

		  txtDia->Text="";
		  txtMes->Text="";
		  txtAnio->Text="";
		  txtDia->SetFocus();

		  tamano+=1;

	 }else{
		 ShowMessage("Fecha incorrecta");
     }
   }else{
	   ShowMessage("Error en ingresar datos vacios");
   }

}
//---------------------------------------------------------------------------

void __fastcall TfrmFecha::btnOrdenarClick(TObject *Sender)
{
	tamano=lstFI->Items->Count;
	listaFechaSuma = new int[tamano];
	indices = new int[tamano];

	for (int i=0; i < tamano; i++) {
		indices[i] = i;
	}

	for (int i=0; i < tamano; i++) {
		int suma=0, diaMesAnio=1;

		std::string s = AnsiString(lstFI->Items->Strings[i]).c_str();

		std::string delimiter = "/";

		size_t pos = 0;
		std::string token;
		while ((pos = s.find(delimiter)) != std::string::npos) {
			token = s.substr(0, pos);

			//ShowMessage(stoi(token));
			if(diaMesAnio==1){
			   suma += stoi(token);
			}
			if(diaMesAnio==2){
			   suma += (30*stoi(token));
			}

			s.erase(0, pos + delimiter.length());

			diaMesAnio+=1;
		}
        if(diaMesAnio==3){
			   suma += (365*stoi(s));
			}

		listaFechaSuma[i] = suma;
	}



	 ordBurbuja(listaFechaSuma, tamano);

	 for (int i = 0; i < tamano; i++) {
		 //ShowMessage(listaFechaSuma[i]);
	 }

	 for (int i=0; i < tamano; i++) {
		lstFO->Items->Add(lstFI->Items->Strings[indices[i]]);
	}

}
//---------------------------------------------------------------------------

void intercambiar(int &x, int &y){
	int aux=x;
	x=y;
	y=aux;
}

void ordBurbuja(int a[], int n){
	bool interruptor = true;
	int pasada, j;
	for (pasada = 0; pasada < n-1 && interruptor; pasada++) {
		interruptor = false;
		for (j = 0; j < n-pasada-1; j++) {
			if (a[j] > a[j+1]) {
			   interruptor = true;
			   intercambiar(a[j], a[j+1]);
			   intercambiar(indices[j], indices[j+1]);
			}
		}
	}
}


