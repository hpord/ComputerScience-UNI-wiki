from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Optional

# Chain of Responsibility 'COR'

class Handler(ABC):
    """
    La interfaz Handler declara un método para construir la cadena de controladores.
    También declara un método para ejecutar una solicitud.
    """

    @abstractmethod
    def set_next(self, handler: Handler) -> Handler:
        pass

    @abstractmethod
    def handle(self, request) -> Optional[str]:
        pass


class AbstractHandler(Handler):
    """
    
    El comportamiento de encadenamiento predeterminado se puede implementar 
    dentro de una clase de controlador base.
    """

    _next_handler: Handler = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        # Devolver un controlador desde aquí nos permitirá vincular los controladores de una manera conveniente como esta:
        # mono.set_next(ardilla).set_next(perro)
        return handler

    @abstractmethod
    def handle(self, request: Any) -> str:
        if self._next_handler:
            return self._next_handler.handle(request)

        return None


"""

Todos los manejadores concretos manejan una solicitud o la 
pasan al siguiente manejador (manipulador) en la cadena.
"""


class MonkeyHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == "Platano":
            return f"Mono: Me comeré el {request}"
        else:
            return super().handle(request)


class SquirrelHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == "Nuez":
            return f"Ardilla: Me comeré la {request}"
        else:
            return super().handle(request)


class DogHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == "Hueso":
            return f"Perro: Me comeré el {request}"
        else:
            return super().handle(request)


def client_code(handler: Handler) -> None:
    """
    El código de cliente suele ser adecuado para trabajar con un solo controlador. 
    En la mayoría de los casos, ni siquiera es consciente de que el manejador es 
    parte de una cadena.
    """

    for food in ["Nuez", "Platano", "Taza de cafe"]:
        print(f"\nCliente: Quién quiere un(a) {food}?")
        result = handler.handle(food)
        if result:
            print(f"  {result}", end="")
        else:
            print(f"  {food} se dejó intacto.", end="")



if __name__ == "__main__":
    monkey = MonkeyHandler()
    squirrel = SquirrelHandler()
    dog = DogHandler()

    monkey.set_next(squirrel).set_next(dog)

    # El cliente debe poder enviar una solicitud a cualquier controlador, 
    # no solo al primero en la cadena.
    print("Cadena: Mono > Ardilla > Perro")
    client_code(monkey)
    print("\n")

    print("Subcadena: Ardilla > Perro")
    client_code(squirrel)
    print("\n")