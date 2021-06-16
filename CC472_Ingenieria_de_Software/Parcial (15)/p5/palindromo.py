class StringUtil:
    
    def __init__(self, myString=None):
        self.myString = myString

    def isPalindromo(myString):
         
        # Eliminamos los espacios
        myString = myString.replace(" ", "")

        # ponemos todo a minúscula
        myString = myString.lower()

        if myString == ''.join(reversed(myString)):
            return True
        else:
            return False