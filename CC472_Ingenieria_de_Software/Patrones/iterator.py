from __future__ import annotations
from collections.abc import Iterable, Iterator
from typing import Any, List


"""
Para crear un iterador en Python, hay dos clases abstractas de la
en el módulo `collections` - Iterable, Iterador. Necesitamos implementar el
`__iter __ ()` método en el objeto iterado (collection), y el `__next__ ()`
método en el iterador.
"""


class AlphabeticalOrderIterator(Iterator):
    """
     Los iteradores concretos implementan varios algoritmos transversales. 
     Estas clases almacenan la posición transversal actual en todo momento.
    """

    """
    `_position` almacena la posición transversal actual. Un iterador puede
    tienen muchos otros campos para almacenar el estado de iteración, especialmente cuando
    se supone que funciona con un tipo particular de colección.
    """
    _position: int = None

    """  
    Este atributo indica la posición transversal.
    """
    _reverse: bool = False

    def __init__(self, collection: WordsCollection, reverse: bool = False) -> None:
        self._collection = collection
        self._reverse = reverse
        self._position = -1 if reverse else 0

    def __next__(self):
        """
        El método __next __ () debe devolver el siguiente elemento de la secuencia. En
        llegando al final, y en llamadas posteriores, debe lanzar un StopIteration.
        """
        try:
            value = self._collection[self._position]
            self._position += -1 if self._reverse else 1
        except IndexError:
            raise StopIteration()

        return value


class WordsCollection(Iterable):
    """
    Las colecciones concretas proporcionan uno o varios métodos para recuperar
    instancias de iterador, compatibles con la clase de colección.
    """

    def __init__(self, collection: List[Any] = []) -> None:
        self._collection = collection

    def __iter__(self) -> AlphabeticalOrderIterator:
        """
        El método __iter __ () devuelve el objeto iterador en sí, 
        por defecto devolvemos el iterador en orden ascendente.
        """
        return AlphabeticalOrderIterator(self._collection)

    def get_reverse_iterator(self) -> AlphabeticalOrderIterator:
        return AlphabeticalOrderIterator(self._collection, reverse = True)

    def add_item(self, item: Any):
        self._collection.append(item)


if __name__ == "__main__":
    """ El código del cliente puede conocer o no las clases de Iterador o Colección, dependiendo 
    del nivel de direccionamiento indirecto que desee mantener en su programa. """

    collection = WordsCollection()
    collection.add_item("Primero")
    collection.add_item("Segundo")
    collection.add_item("Tercero")

    print("Recorrido recto:")
    print("\n".join(collection))
    print("\n\n")

    print("Recorrido inverso:")
    print("\n".join(collection.get_reverse_iterator()), end="\n\n")