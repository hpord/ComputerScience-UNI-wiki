digit =[[
'###',
'# #',
'# #',
'# #',
'###',
],
[
'  #',
'  #',
'  #',
'  #',
'  #',
],
[
'###',
'  #',
'###',
'#  ',
'###',
],
[
'###',
'  #',
'###',
'  #',
'###',
],
[
'# #',
'# #',
'###',
'  #',
'  #',
],
[
'###',
'#  ',
'###',
'  #',
'###',
],
[
'###',
'#  ',
'###',
'# #',
'###',
],
[
'###',
'  #',
'  #',
'  #',
'  #',
],
[
'###',
'# #',
'###',
'# #',
'###',
],
[
'###',
'# #',
'###',
'  #',
'###',
]]


numero = input("Dame un numero: ")
for i in range(5):
  renglon = ""                   # Empezar con renglón vacío
  for cifra in numero:           # Crear el renglón
    cifra= int(cifra)            # Recorriendo cada cifra
    renglon += digit[cifra][i]   # y añadiéndola al renglón
    renglon += " "               # mas un espacio en blanco
  print(renglon)                 # Imprimir el renglón creado
