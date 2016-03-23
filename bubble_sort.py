import unittest

#O(n²) para tempo de execução e O(1) para memória, no pior caso

def bubble_sort(seq):
    n = len(seq) - 1
    flag = 0
    for i in range(n):
        for j in range(n):
            if seq[j]>seq[j+1]:
                seq[j+1], seq[j] = seq[j], seq[j+1]
        if flag == 0:
            break;
        flag = 0;
    return seq

class OrdenacaoTestes(unittest.TestCase):
    def teste_lista_vazia(self):
        self.assertListEqual([], bubble_sort([]))

    def teste_lista_unitaria(self):
        self.assertListEqual([1], bubble_sort([1]))

    def teste_lista_binaria(self):
        self.assertListEqual([1, 2], bubble_sort([2, 1]))

    def teste_lista_binaria(self):
        self.assertListEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], bubble_sort([9, 7, 1, 8, 5, 3, 6, 4, 2, 0]))


if __name__ == '__main__':
    unittest.main()
