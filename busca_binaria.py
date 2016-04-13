''''
O tempo de execução é O(logn) porque sempre vai ignorar a metade em que o procurado não está
A memória é O(1) porque existem apenas 3 variáveis criadas
''''

def busca_binaria(seq, procurado):
    meio = 0
    if len(seq) == 0:
        return 0
    else:
        final = len(seq) - 1
        inicio = 0
        while inicio <= final:
            meio = int((inicio+final)/2)
            if (procurado > seq[meio]):
                inicio = meio + 1
            else:
                final = meio - 1
    if procurado > seq[meio]:
        return meio + 1
    else:
        return meio


import unittest


class BuscaBinariaTestes(unittest.TestCase):
    def teste_lista_vazia(self):
        self.assertEqual(0, busca_binaria([], 1))
        self.assertEqual(0, busca_binaria([], 2))
        self.assertEqual(0, busca_binaria([], 3))

    def teste_lista_unitaria(self):
        self.assertEqual(0, busca_binaria([1], 0))
        self.assertEqual(0, busca_binaria([1], 1))
        self.assertEqual(1, busca_binaria([1], 2))
        self.assertEqual(1, busca_binaria([1], 3))
        self.assertEqual(1, busca_binaria([1], 4))

    def teste_lista_nao_unitaria(self):
        lista = list(range(10))
        self.assertEqual(0, busca_binaria(lista, -2))
        self.assertEqual(0, busca_binaria(lista, -1))
        for i in lista:
            self.assertEqual(i, busca_binaria(lista, i))
        self.assertEqual(10, busca_binaria(lista, 10))
        self.assertEqual(10, busca_binaria(lista, 11))
        self.assertEqual(10, busca_binaria(lista, 12))

    def teste_lista_elementos_repetidos(self):
        lista = [1, 1, 1, 2, 2, 2]
        self.assertEqual(0, busca_binaria(lista, 1))
        self.assertEqual(3, busca_binaria(lista, 2))

if __name__=='__main__':
    unittest.main()
