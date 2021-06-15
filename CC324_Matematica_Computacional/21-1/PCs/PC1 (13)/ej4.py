import numpy as np
from numpy import array
from numpy import dot

# coordenadas de la base
P1, P2, P3, P4 = [0, 0, 0], [0, 1, 0], [1, 1, 0], [1, 0, 0]
P1, P2, P3, P4 = array(P1), array(P2), array(P3), array(P4)

# para las 4 coordenadas faltantes, solo nos importa
# la coodenada P5 (encima de P1)
P5 = array([0, 0, 1])

# punto a probar
X = array([0, 0, 1])


# Las 3 importantes direcciones son u, v, w
u, v, w = P1 - P2, P1 - P4, P1 - P5

# si u, v, w son 3 aristas perpendiculares de la caja
if dot(u, v) == 0 & dot(u, w) == 0 & dot(v, w) == 0:
    print("\nLas aristas son perpendiculares..\n")

    if (
        (dot(u, P2) <= dot(u, X) <= dot(u, P1))
        and (dot(v, P4) <= dot(v, X) <= dot(v, P1))
        and (dot(w, P5) <= dot(w, X) <= dot(w, P1))
    ):
        print(f"El punto {X}  pertenece a la caja")
    else:
        print(f"El punto {X}  NO pertenece a la caja")

# si las aristas no son perpendiculares,
# necesitamos vectores u, v, w que sean
# perpendiculares a las caras de la caja
else:
    print("\nLas aristas NO son perpendiculares..\n")
    u = np.cross(P1 - P4, P1 - P5)
    v = np.cross(P1 - P2, P1 - P5)
    w = np.cross(P1 - P2, P1 - P4)

    if (
        (dot(u, P2) <= dot(u, X) <= dot(u, P1))
        and (dot(v, P4) <= dot(v, X) <= dot(v, P1))
        and (dot(w, P5) <= dot(w, X) <= dot(w, P1))
    ):
        print(f"El punto {X}  pertenece a la caja")
    else:
        print(f"El punto {X}  NO pertenece a la caja")
