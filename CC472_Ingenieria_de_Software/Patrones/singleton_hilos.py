from threading import Lock, Thread


class SingletonMeta(type):
    """
    Esta es una implementación segura para subprocesos de Singleton.
    """

    _instances = {}

    _lock: Lock = Lock()
    """
    Ahora tenemos un objeto de bloqueo que se utilizará para sincronizar 
    subprocesos durante primer acceso al Singleton.
    """

    def __call__(cls, *args, **kwargs):
        """
        Los posibles cambios en el valor del argumento `__init__` no afectan
        la instancia devuelta.
        """
        
        """ Ahora, imagine que el programa acaba de lanzarse. Dado que todavía no hay una instancia de Singleton, 
        varios subprocesos pueden pasar simultáneamente el condicional anterior y llegar a este punto casi 
        al mismo tiempo. El primero de ellos adquirirá bloqueo y continuará, mientras que el resto esperará aquí. """

        with cls._lock:    
            """ El primer hilo en adquirir el bloqueo, alcanza este condicional, entra y crea la instancia de Singleton. 
            Una vez que sale del bloque de bloqueo, un hilo que podría haber estado esperando la liberación del 
            bloqueo puede ingresar a esta sección. Pero dado que el campo Singleton ya está inicializado, el hilo
            no creará un nuevo objeto. """

            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    value: str = None
    """
    Usaremos esta propiedad para probar que nuestro Singleton realmente funciona.
    """

    def __init__(self, value: str) -> None:
        self.value = value

    def some_business_logic(self):
        """
        Finalmente, cualquier singleton debe definir alguna lógica de negocios, 
        que puede ser ejecutado en su instancia.
        """


def test_singleton(value: str) -> None:
    singleton = Singleton(value)
    print(singleton.value)


if __name__ == "__main__":
    # el código de cliente

    print("\nSi ve el mismo valor, entonces se reutilizó singleton (¡bien!) \n"
          "Si ves valores diferentes,"
          "se crearon 2 singletons (¡mal!) \n \n"
          "RESULTADO:\n")

    process1 = Thread(target=test_singleton, args=("instance1",))
    process2 = Thread(target=test_singleton, args=("instance2",))
    process1.start()
    process2.start()