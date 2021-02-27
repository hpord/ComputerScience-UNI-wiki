from logic import *

# Oracion: "If it's rains, it's wet".
def rainWet():
    Rain = Atom('Rain') # si llueve
    Wet = Atom('Wet') # si esta mojado
    return Implies(Rain, Wet)

# Oracion: "There is a light that shines."
def lightShines():
    def Light(x): return Atom('Light', x)    # si x esta encendido
    def Shines(x): return Atom('Shines', x)  # si x esta brillando
    return Exists('$x', And(Light('$x'), Shines('$x')))

# Definiendo Padres en terminos de hijos.
def parentChild():
    def Parent(x, y): return Atom('Parent', x, y)  # si x tiene un padre y
    def Child(x, y): return Atom('Child', x, y)    # si x tiene un hijo y
    return Forall('$x', Forall('$y', Equiv(Parent('$x', '$y'), Child('$y', '$x'))))
