object frmIndirectos: TfrmIndirectos
  Left = 0
  Top = 0
  Caption = 'M'#233'todos de Ordenaci'#243'n Indirectos'
  ClientHeight = 668
  ClientWidth = 1044
  Color = clBtnFace
  Font.Charset = DEFAULT_CHARSET
  Font.Color = clWindowText
  Font.Height = -11
  Font.Name = 'Tahoma'
  Font.Style = []
  OldCreateOrder = False
  PixelsPerInch = 96
  TextHeight = 13
  object Label1: TLabel
    Left = 32
    Top = 24
    Width = 181
    Height = 25
    Caption = 'Ingrese un n'#250'mero'
    Font.Charset = DEFAULT_CHARSET
    Font.Color = clWindowText
    Font.Height = -21
    Font.Name = 'Tahoma'
    Font.Style = []
    ParentFont = False
  end
  object Label2: TLabel
    Left = 403
    Top = 24
    Width = 137
    Height = 25
    Caption = 'Lista ordenada'
    Font.Charset = DEFAULT_CHARSET
    Font.Color = clWindowText
    Font.Height = -21
    Font.Name = 'Tahoma'
    Font.Style = []
    ParentFont = False
  end
  object Label3: TLabel
    Left = 256
    Top = 24
    Width = 42
    Height = 25
    Caption = 'Lista'
    Font.Charset = DEFAULT_CHARSET
    Font.Color = clWindowText
    Font.Height = -21
    Font.Name = 'Tahoma'
    Font.Style = []
    ParentFont = False
  end
  object Shape1: TShape
    Left = 552
    Top = 8
    Width = 9
    Height = 649
    Brush.Color = clSkyBlue
  end
  object Label4: TLabel
    Left = 688
    Top = 8
    Width = 266
    Height = 25
    Caption = 'Mezclar dos listas ordenadas'
    Font.Charset = DEFAULT_CHARSET
    Font.Color = clWindowText
    Font.Height = -21
    Font.Name = 'Tahoma'
    Font.Style = []
    ParentFont = False
  end
  object Label5: TLabel
    Left = 608
    Top = 56
    Width = 62
    Height = 25
    Caption = 'Lista A'
    Font.Charset = DEFAULT_CHARSET
    Font.Color = clWindowText
    Font.Height = -21
    Font.Name = 'Tahoma'
    Font.Style = []
    ParentFont = False
  end
  object Label6: TLabel
    Left = 760
    Top = 56
    Width = 62
    Height = 25
    Caption = 'Lista B'
    Font.Charset = DEFAULT_CHARSET
    Font.Color = clWindowText
    Font.Height = -21
    Font.Name = 'Tahoma'
    Font.Style = []
    ParentFont = False
  end
  object Label7: TLabel
    Left = 912
    Top = 56
    Width = 89
    Height = 25
    Caption = 'Lista AUB'
    Font.Charset = DEFAULT_CHARSET
    Font.Color = clWindowText
    Font.Height = -21
    Font.Name = 'Tahoma'
    Font.Style = []
    ParentFont = False
  end
  object txtN: TEdit
    Left = 32
    Top = 55
    Width = 121
    Height = 33
    Font.Charset = DEFAULT_CHARSET
    Font.Color = clWindowText
    Font.Height = -21
    Font.Name = 'Tahoma'
    Font.Style = []
    ParentFont = False
    TabOrder = 0
    OnKeyPress = txtNKeyPress
  end
  object lstLista: TListBox
    Left = 256
    Top = 55
    Width = 121
    Height = 546
    Font.Charset = DEFAULT_CHARSET
    Font.Color = clWindowText
    Font.Height = -21
    Font.Name = 'Tahoma'
    Font.Style = []
    ItemHeight = 25
    ParentFont = False
    TabOrder = 1
  end
  object lstListaO: TListBox
    Left = 403
    Top = 55
    Width = 121
    Height = 546
    Font.Charset = DEFAULT_CHARSET
    Font.Color = clWindowText
    Font.Height = -21
    Font.Name = 'Tahoma'
    Font.Style = []
    ItemHeight = 25
    ParentFont = False
    TabOrder = 2
  end
  object btnShell: TButton
    Left = 32
    Top = 184
    Width = 121
    Height = 49
    Caption = 'Shell'
    Font.Charset = DEFAULT_CHARSET
    Font.Color = clWindowText
    Font.Height = -21
    Font.Name = 'Tahoma'
    Font.Style = []
    ParentFont = False
    TabOrder = 3
    OnClick = btnShellClick
  end
  object btnQuickSort: TButton
    Left = 32
    Top = 256
    Width = 121
    Height = 49
    Caption = 'QuickSort'
    Font.Charset = DEFAULT_CHARSET
    Font.Color = clWindowText
    Font.Height = -21
    Font.Name = 'Tahoma'
    Font.Style = []
    ParentFont = False
    TabOrder = 4
    OnClick = btnQuickSortClick
  end
  object btnSalir: TButton
    Left = 32
    Top = 583
    Width = 105
    Height = 42
    Caption = 'Salir'
    Font.Charset = DEFAULT_CHARSET
    Font.Color = clRed
    Font.Height = -27
    Font.Name = 'Tahoma'
    Font.Style = []
    ParentFont = False
    Style = bsCommandLink
    TabOrder = 5
    OnClick = btnSalirClick
  end
  object btnLimpiar: TButton
    Left = 32
    Top = 112
    Width = 121
    Height = 49
    Caption = 'Limpiar'
    Font.Charset = DEFAULT_CHARSET
    Font.Color = clWindowText
    Font.Height = -21
    Font.Name = 'Tahoma'
    Font.Style = []
    ParentFont = False
    TabOrder = 6
    OnClick = btnLimpiarClick
  end
  object btnCrear: TButton
    Left = 159
    Top = 112
    Width = 82
    Height = 66
    Caption = 'Crear Vector'
    Font.Charset = DEFAULT_CHARSET
    Font.Color = clWindowText
    Font.Height = -21
    Font.Name = 'Tahoma'
    Font.Style = []
    ParentFont = False
    TabOrder = 7
    Visible = False
    WordWrap = True
    OnClick = btnCrearClick
  end
  object mmoA: TMemo
    Left = 608
    Top = 87
    Width = 105
    Height = 314
    Font.Charset = DEFAULT_CHARSET
    Font.Color = clBlue
    Font.Height = -19
    Font.Name = 'Tahoma'
    Font.Style = []
    ParentFont = False
    TabOrder = 8
  end
  object mmoB: TMemo
    Left = 760
    Top = 87
    Width = 105
    Height = 314
    Font.Charset = DEFAULT_CHARSET
    Font.Color = clBlue
    Font.Height = -19
    Font.Name = 'Tahoma'
    Font.Style = []
    ParentFont = False
    TabOrder = 9
  end
  object mmoAB: TMemo
    Left = 904
    Top = 87
    Width = 129
    Height = 570
    Font.Charset = DEFAULT_CHARSET
    Font.Color = clBlue
    Font.Height = -19
    Font.Name = 'Tahoma'
    Font.Style = []
    ParentFont = False
    TabOrder = 10
  end
  object btnMerge: TButton
    Left = 32
    Top = 336
    Width = 121
    Height = 49
    Caption = 'Merge'
    Font.Charset = DEFAULT_CHARSET
    Font.Color = clWindowText
    Font.Height = -21
    Font.Name = 'Tahoma'
    Font.Style = []
    ParentFont = False
    TabOrder = 11
    OnClick = btnMergeClick
  end
  object btnHeap: TButton
    Left = 32
    Top = 416
    Width = 121
    Height = 49
    Caption = 'Heap'
    Font.Charset = DEFAULT_CHARSET
    Font.Color = clWindowText
    Font.Height = -21
    Font.Name = 'Tahoma'
    Font.Style = []
    ParentFont = False
    TabOrder = 12
    OnClick = btnHeapClick
  end
  object btnMezclar: TButton
    Left = 760
    Top = 464
    Width = 115
    Height = 73
    Caption = 'Mezclar'
    Font.Charset = DEFAULT_CHARSET
    Font.Color = clWindowText
    Font.Height = -21
    Font.Name = 'Tahoma'
    Font.Style = []
    ParentFont = False
    TabOrder = 13
    OnClick = btnMezclarClick
  end
  object btnRadix: TButton
    Left = 32
    Top = 488
    Width = 121
    Height = 49
    Caption = 'Radix'
    Font.Charset = DEFAULT_CHARSET
    Font.Color = clWindowText
    Font.Height = -19
    Font.Name = 'Tahoma'
    Font.Style = []
    ParentFont = False
    TabOrder = 14
    OnClick = btnRadixClick
  end
end
