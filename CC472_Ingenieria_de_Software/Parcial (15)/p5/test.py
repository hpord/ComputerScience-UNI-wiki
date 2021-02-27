import unittest
from palindromo import StringUtil


class TestMyModule(unittest.TestCase):
    
    def test_palindromo(self):
        self.assertEqual(StringUtil.isPalindromo(myString="dabale arroz a la zorra el abad"), True)

        # ahora comprobamos que también funciona para caso de mayúsculas
        self.assertEqual(StringUtil.isPalindromo(myString="DabaLe arroZ a lA zorra el ABad"), True)

        # ponemos un caso donde no sea palindromo
        self.assertEqual(StringUtil.isPalindromo(myString="esto no es palindromo"), False)
        
if __name__ == "__main__":
    unittest.main()