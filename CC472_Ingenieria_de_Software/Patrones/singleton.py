from datetime import datetime


class SingletonMeta(type):
    """
    La clase Singleton se puede implementar de diferentes formas en Python. 
    Algunos métodos posibles incluyen: clase base, decorador, metaclase. 
    Usaremos la metaclase porque es la más adecuada para este propósito.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Los posibles cambios en el valor del argumento `__init__` no afectan
        la instancia devuelta.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    value: str = None
    nSessions: int = None
    dates: list = None
    """
    Usaremos esta propiedad para probar que nuestro Singleton realmente funciona.
    """

    def __init__(self, value: str ) -> None:
        self.value = value
        self.dates = [datetime.now().strftime("%d/%m/%Y %H:%M:%S")]
        self.nSessions = 1

    def setNumberSessions(self):
        self.nSessions += 1

    def setDateSessions(self):
        today = datetime.now()
        d = today.strftime("%d/%m/%Y %H:%M:%S")
        self.dates.append(d)

if __name__ == "__main__":
    # El codigo para el cliente

    s1 = Singleton(value='s1')
    s2 = Singleton(value='s2')

    if id(s1) == id(s2):
        print("\nSingleton funciona, ambas variables contienen la misma instancia.")
        del s1, s2

        s1 = Singleton(value='s1')
        print("\nImprimiendo fechas de creacion de 's1': \n {}".format(s1.dates), end="\n")
        print("\nImprimiendo numero de sesiones de 's1': {}".format(s1.nSessions), end="\n\n")
        print("---------------------------------------------------------------------------------")


        s2 = Singleton(value='s2')
        s2.setDateSessions()
        s2.setNumberSessions()
        print("\nImprimiendo fechas de creacion de 's2': \n {}".format(s2.dates), end="\n")
        print("\nImprimiendo numero de sesiones de 's2': {}".format(s2.nSessions), end="\n\n")
        print("---------------------------------------------------------------------------------")

        
        s3 = Singleton(value='s3')
        s3.setDateSessions()
        s3.setNumberSessions()
        print("\nImprimiendo fechas de creacion de 's3': \n {}".format(s3.dates), end="\n")
        print("\nImprimiendo numero de sesiones de 's3': {}".format(s3.nSessions), end="\n\n")
        print("---------------------------------------------------------------------------------")


        print("Imprimiendo nombres de todas las instancias ...\n {} {} {}".format(s1.value, s2.value, s3.value))
        print("\nImprimiendo ID's de todas las instancias ...\n {} {} {}".format(id(s1), id(s2), id(s3)))


    else:
        print("Singleton ha fallado, las variables contienen diferentes instancias.")