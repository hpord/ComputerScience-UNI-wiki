### ¿Qué es esto?
La descripción lo dice todo.

### ¿Cómo utilizarlo?
Primero necesita crear un archivo de autómatas donde defina sus producciones, estados de inicio y cosas así.
```python
Q P F # estados totales
a # introducir símbolos de palabras
Z Y # Símbolos de pila 
Q # estado inicial
Z # Pila inicial 
F # estados de aceptación
F # E - acepta con pila vacía o F - acepta con estado de aceptación
Q a Z Q YZ # lista de producciones (estado actual, lectura de la palabra, tomar de la pila, siguiente estado, agregar a la pila)
Q a Y Q YY
Q e Z P Z
Q e Y P Y
P a Z P e
P a Y P e
P e Z F e
```

**Notas:**
* Estamos de acuerdo en que "e" significa épsilon y no aparecerá como símbolo de estado.
* No debe usar símbolos de pila que tengan más de un carácter; cualquier otra cosa está bien.

¡Eso es todo! Simplemente ejecute el script y debería solicitar la ubicación del archivo de entrada y las palabras para probar.

### Agradecimientos
Me base en el repositorio de [theodoregold](https://github.com/theodoregold/pushdown-automata) para poder construir este constructor de autómatas PDA.

