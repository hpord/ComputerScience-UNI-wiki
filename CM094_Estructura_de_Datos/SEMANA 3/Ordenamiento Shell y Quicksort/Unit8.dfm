object frmOrdenacionV2: TfrmOrdenacionV2
  Left = 0
  Top = 0
  Caption = 'OrdenacionV2'
  ClientHeight = 367
  ClientWidth = 450
  Color = clWhite
  Font.Charset = DEFAULT_CHARSET
  Font.Color = clHotLight
  Font.Height = -11
  Font.Name = '@Yu Gothic UI Semibold'
  Font.Style = []
  OldCreateOrder = False
  PixelsPerInch = 96
  TextHeight = 13
  object Label1: TLabel
    Left = 24
    Top = 45
    Width = 97
    Height = 13
    Caption = 'Ingrese un n'#250'mero:'
  end
  object Label2: TLabel
    Left = 216
    Top = 24
    Width = 29
    Height = 13
    Caption = 'Lista'
    Font.Charset = SHIFTJIS_CHARSET
    Font.Color = clMaroon
    Font.Height = -11
    Font.Name = 'UD Digi Kyokasho NK-B'
    Font.Style = [fsBold]
    ParentFont = False
  end
  object Label3: TLabel
    Left = 288
    Top = 24
    Width = 85
    Height = 13
    Caption = 'Lista ordenada'
    Font.Charset = SHIFTJIS_CHARSET
    Font.Color = clGreen
    Font.Height = -11
    Font.Name = 'UD Digi Kyokasho NK-B'
    Font.Style = [fsBold]
    ParentFont = False
  end
  object bntLimpiar: TButton
    Left = 24
    Top = 136
    Width = 89
    Height = 25
    Cursor = crHandPoint
    Caption = 'Limpiar'
    TabOrder = 0
    OnClick = bntLimpiarClick
  end
  object lbLista: TListBox
    Left = 200
    Top = 64
    Width = 49
    Height = 241
    Cursor = crNo
    Font.Charset = SHIFTJIS_CHARSET
    Font.Color = clMaroon
    Font.Height = -13
    Font.Name = 'UD Digi Kyokasho NK-B'
    Font.Style = [fsBold]
    ItemHeight = 15
    ParentFont = False
    TabOrder = 1
  end
  object btnShell: TButton
    Left = 24
    Top = 176
    Width = 89
    Height = 25
    Cursor = crHandPoint
    Caption = 'Shell'
    TabOrder = 2
    OnClick = btnShellClick
  end
  object btnQuicksort: TButton
    Left = 24
    Top = 216
    Width = 89
    Height = 25
    Cursor = crHandPoint
    Caption = 'QuickSort'
    TabOrder = 3
    OnClick = btnQuicksortClick
  end
  object btnSalir: TButton
    Left = 352
    Top = 311
    Width = 158
    Height = 48
    Cursor = crHandPoint
    Caption = 'SALIR'
    Font.Charset = SHIFTJIS_CHARSET
    Font.Color = clRed
    Font.Height = -11
    Font.Name = 'UD Digi Kyokasho N-B'
    Font.Style = [fsBold]
    ParentFont = False
    Style = bsCommandLink
    TabOrder = 4
    OnClick = btnSalirClick
  end
  object lbListaOrdenada: TListBox
    Left = 296
    Top = 64
    Width = 49
    Height = 241
    Cursor = crNo
    Font.Charset = SHIFTJIS_CHARSET
    Font.Color = clGreen
    Font.Height = -13
    Font.Name = 'UD Digi Kyokasho NK-B'
    Font.Style = [fsBold]
    ItemHeight = 15
    ParentFont = False
    TabOrder = 5
  end
  object txtNumero: TEdit
    Left = 24
    Top = 64
    Width = 65
    Height = 21
    Cursor = crIBeam
    TabOrder = 6
    OnKeyPress = txtNumeroKeyPress
  end
  object btnAgregar: TButton
    Left = 95
    Top = 64
    Width = 58
    Height = 21
    Cursor = crHandPoint
    Caption = 'Agregar'
    TabOrder = 7
    OnClick = btnAgregarClick
  end
  object btnCrear: TButton
    Left = 38
    Top = 289
    Width = 75
    Height = 25
    Caption = 'crear'
    TabOrder = 8
    Visible = False
    OnClick = btnCrearClick
  end
end
