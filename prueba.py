import  unittest
import  cambia_texto

class ProbarCambiaTexto(unittest.TestCase):

    def text_mayusculas(self):
        palabra = 'buen dia'
        resultado = cambia_texto.todo_mayusculas(palabra)
        self.assertEqual(resultado, 'BUEN DIA')

if __name__ == '__main__':
    unittest.main()