object frmGrafo: TfrmGrafo
  Left = 0
  Top = 0
  Caption = 'Grafo'
  ClientHeight = 608
  ClientWidth = 1032
  Color = clBtnFace
  Font.Charset = DEFAULT_CHARSET
  Font.Color = clWindowText
  Font.Height = -15
  Font.Name = 'Tahoma'
  Font.Style = []
  OldCreateOrder = False
  PixelsPerInch = 96
  TextHeight = 18
  object Label1: TLabel
    Left = 8
    Top = 11
    Width = 210
    Height = 18
    Caption = 'Cantidad de nodos (Maximo 10)'
  end
  object Label2: TLabel
    Left = 8
    Top = 560
    Width = 403
    Height = 18
    Caption = '(dir. Nodo actual // dir. Nodo siguiente // dir. cabeza de arco)'
    Font.Charset = DEFAULT_CHARSET
    Font.Color = clOlive
    Font.Height = -15
    Font.Name = 'Tahoma'
    Font.Style = []
    ParentFont = False
  end
  object Label3: TLabel
    Left = 464
    Top = 560
    Width = 328
    Height = 18
    Caption = '(dir. inicio arco // dir.  final  arco // dir. prox. arco)'
  end
  object txtNodos: TEdit
    Left = 264
    Top = 8
    Width = 121
    Height = 26
    Alignment = taRightJustify
    NumbersOnly = True
    TabOrder = 0
  end
  object btnDibujar: TButton
    Left = 424
    Top = 3
    Width = 81
    Height = 41
    Caption = 'Dibujar'
    TabOrder = 1
    OnClick = btnDibujarClick
  end
  object btnCrearGrafo: TButton
    Left = 544
    Top = 3
    Width = 129
    Height = 41
    Caption = 'Crear Grafo'
    TabOrder = 2
    OnClick = btnCrearGrafoClick
  end
end
