# ver laboratorio para poder entender como resolví el problema

from __future__ import annotations
from abc import ABC, abstractmethod


class Context:
    """
    The Context defines the interface of interest to clients. It also maintains
    a reference to an instance of a State subclass, which represents the current
    state of the Context.
    """

    _state = None
    """
    A reference to the current state of the Context.
    """

    def __init__(self, state: State) -> None:
        self.transition_to(state)

    def transition_to(self, state: State):
        """
        The Context allows changing the State object at runtime.
        """

        print(f"Contexto: Transición  {type(state).__name__}")
        self._state = state
        self._state.context = self

    """
    The Context delegates part of its behavior to the current State object.
    """

    def salida1(self):
        self._state.handle1()

    def salida2(self):
        self._state.handle2()


class State(ABC):
    """
    The base State class declares methods that all Concrete State should
    implement and also provides a backreference to the Context object,
    associated with the State. This backreference can be used by States to
    transition the Context to another State.
    """

    @property
    def context(self) -> Context:
        return self._context

    @context.setter
    def context(self, context: Context) -> None:
        self._context = context

    @abstractmethod
    def handle1(self) -> None:
        pass

    @abstractmethod
    def handle2(self) -> None:
        pass


"""
Los Estados concretos implementan diversos comportamientos, asociados con un estado del
Contexto.
"""


class Cerrada(State):
    def handle1(self) -> None:
        print("\n'Cerrada' maneja la solicitud Salida1: Abrir")
        print("'Cerrada' quiere cambiar el estado del contexto.")
        self.context.transition_to(Abierta())

    def handle2(self) -> None:
        print("\n'Cerrada' maneja la solicitud Salida2: Armar")
        print("'Cerrada' quiere cambiar el estado del contexto.")
        self.context.transition_to(Armada())


class Abierta(State):
    def handle1(self) -> None:
        print("\n'Abierta' maneja la solicitud Salida1: Cerrar")
        print("'Abierta' quiere cambiar el estado del contexto.")
        self.context.transition_to(Cerrada())

    def handle2(self) -> None:
        print("\n'Abierta' maneja la solicitud Salida2: None")
        print("No hace nada")


class Armada(State):
    def handle1(self) -> None:
        print("\n'Armada' maneja la solicitud Salida1: Desarmar")
        print("'Armada' quiere cambiar el estado del contexto.")
        self.context.transition_to(Cerrada())

    def handle2(self) -> None:
        print("\n'Armada' maneja la solicitud Salida2: Abrir")
        print("'Armada' quiere cambiar el estado del contexto.")
        self.context.transition_to(Emergencia())


class Emergencia(State):
    def handle1(self) -> None:
        print("\n'Emergencia' maneja la solicitud Salida1: FIN DE PROCESO")

    def handle2(self) -> None:
        print("\n'Emergencia' maneja la solicitud Salida2: None")
        print("No hace nada")


if __name__ == "__main__":

    context = Context(Cerrada())
    context.salida1()
    context.salida1()
    context.salida2()
    context.salida2()
    context.salida1()