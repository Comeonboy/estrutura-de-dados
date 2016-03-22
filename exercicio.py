
from aula5.fila import Fila
from aula4.pilha import Pilha

#A memória e o tempo de execução são O(n) porque aumentam conforme o tamanho da variável <expressão>

class ErroLexico(Exception):
    pass


class ErroSintatico(Exception):
    pass

def analise_lexica(expressao): #PRONTO PORÉM FEIO
    """
    Executa análise lexica transformando a expressao em fila de objetos:
    Transforma inteiros em ints
    Flutuantes em floats
    e verificar se demais caracteres são validos: +-*/(){}[]
    :param expressao: string com expressao a ser analisada
    :return: fila com tokens
    """

    car = ''
    fila = Fila()
    if len(expressao):
        for c in expressao:
            if c in ('1234567890'):
                car = car+c
            elif c in ("+-*/(){}[]."):
                if len(car)!=0:
                    fila.enfileirar(car)
                    car = ''
                fila.enfileirar(c)
            else:
                raise ErroLexico('erro')
        if len(car)>0:
            fila.enfileirar(car)


    return fila


def analise_sintatica(fila): #PRONTO PORÉM GRANDE
    """
    Função que realiza analise sintática de tokens produzidos por analise léxica.
    Executa validações sintáticas e se não houver erro retorn fila_sintatica para avaliacao
    :param fila: fila proveniente de análise lexica
    :return: fila_sintatica com elementos tokens de numeros
    """
    fila2 = Fila()
    car=''
    if (len(fila) == 0):
        raise ErroSintatico('erro')
    while (len(fila)!=0):
        c = fila.desenfileirar()
        if c in ('+-*/(){}[]'):
            if len(car)!=0:
                if '.' in car:
                    fila2.enfileirar(float(car))
                    car = ''
                else:
                    fila2.enfileirar(int(car))
                    car = ''
            fila2.enfileirar(c)
        else:
            car = car + c
    if len(car)>0:
        if '.' in car:
            car = float(car)
        else:
            car = int(car)
        fila2.enfileirar(car)

    return fila2


def avaliar(expressao):
    """
    Função que avalia expressão aritmetica retornando se valor se não houver nenhum erro
    :param expressao: string com expressão aritmética
    :return: valor númerico com resultado
    """
    fila = analise_sintatica(analise_lexica(expressao))
    pilha = Pilha()
    v1,v2,v3=None,None,None
    r=0
    for c in fila:
        pilha.empilhar(c)
        if len(pilha)>=3:
            v3 = pilha.desempilhar()
            v2 = pilha.desempilhar()
            v1 = pilha.desempilhar()
            if str(v3) not in '({[)}]' and str(v1) not in '(){}[]' and str(v2) in '+-/*':
                if str(v2) == '+':
                    r = v1 + v3
                elif str(v2) == '-':
                    r = v1 - v3
                elif str(v2) == '/':
                    r = v1/v3
                elif str(v2) == "*":
                    r = v1*v3
                pilha.empilhar(r)
            else:
                pilha.empilhar(v1)
                pilha.empilhar(v2)
                pilha.empilhar(v3)
        if str(c) in ')}]':
            pilha.desempilhar()
            r=pilha.desempilhar()
            pilha.desempilhar()
            pilha.empilhar(r)
            if len(pilha)>=3:
                v3 = pilha.desempilhar()
                v2 = pilha.desempilhar()
                v1 = pilha.desempilhar()
                if str(v3) not in '({[)}]' and str(v1) not in '(){}[]' and str(v2) in '+-/*':
                    if str(v2) == '+':
                        r = v1 + v3
                    elif str(v2) == '-':
                        r = v1 - v3
                    elif str(v2) == '/':
                        r = v1/v3
                    elif str(v2) == "*":
                        r = v1*v3
                    pilha.empilhar(r)
                else:
                    pilha.empilhar(v1)
                    pilha.empilhar(v2)
                    pilha.empilhar(v3)
    return pilha.topo()









import unittest


class AnaliseLexicaTestes(unittest.TestCase):
    def test_expressao_vazia(self):
        fila = analise_lexica('')
        self.assertTrue(fila.vazia())

    def test_caracter_estranho(self):
        self.assertRaises(ErroLexico, analise_lexica, 'a')
        self.assertRaises(ErroLexico, analise_lexica, 'ab')

    def test_inteiro_com_um_algarismo(self):
        fila = analise_lexica('1')
        self.assertEqual('1', fila.desenfileirar())
        self.assertTrue(fila.vazia())

    def test_inteiro_com_vários_algarismos(self):
        fila = analise_lexica('1234567890')
        self.assertEqual('1234567890', fila.desenfileirar())
        self.assertTrue(fila.vazia())

    def test_float(self):
        fila = analise_lexica('1234567890.34')
        self.assertEqual('1234567890', fila.desenfileirar())
        self.assertEqual('.', fila.desenfileirar())
        self.assertEqual('34', fila.desenfileirar())
        self.assertTrue(fila.vazia())

    def test_parenteses(self):
        fila = analise_lexica('(1)')
        self.assertEqual('(', fila.desenfileirar())
        self.assertEqual('1', fila.desenfileirar())
        self.assertEqual(')', fila.desenfileirar())
        self.assertTrue(fila.vazia())

    def test_chaves(self):
        fila = analise_lexica('{(1)}')
        self.assertEqual('{', fila.desenfileirar())
        self.assertEqual('(', fila.desenfileirar())
        self.assertEqual('1', fila.desenfileirar())
        self.assertEqual(')', fila.desenfileirar())
        self.assertEqual('}', fila.desenfileirar())
        self.assertTrue(fila.vazia())

    def test_colchetes(self):
        fila = analise_lexica('[{(1.0)}]')
        self.assertEqual('[', fila.desenfileirar())
        self.assertEqual('{', fila.desenfileirar())
        self.assertEqual('(', fila.desenfileirar())
        self.assertEqual('1', fila.desenfileirar())
        self.assertEqual('.', fila.desenfileirar())
        self.assertEqual('0', fila.desenfileirar())
        self.assertEqual(')', fila.desenfileirar())
        self.assertEqual('}', fila.desenfileirar())
        self.assertEqual(']', fila.desenfileirar())
        self.assertTrue(fila.vazia())

    def test_adicao(self):
        fila = analise_lexica('1+2.0')
        self.assertEqual('1', fila.desenfileirar())
        self.assertEqual('+', fila.desenfileirar())
        self.assertEqual('2', fila.desenfileirar())
        self.assertEqual('.', fila.desenfileirar())
        self.assertEqual('0', fila.desenfileirar())
        self.assertTrue(fila.vazia())

    def test_subtracao(self):
        fila = analise_lexica('1-2.0')
        self.assertEqual('1', fila.desenfileirar())
        self.assertEqual('-', fila.desenfileirar())
        self.assertEqual('2', fila.desenfileirar())
        self.assertEqual('.', fila.desenfileirar())
        self.assertEqual('0', fila.desenfileirar())
        self.assertTrue(fila.vazia())

    def test_multiplicacao(self):
        fila = analise_lexica('1*2.0')
        self.assertEqual('1', fila.desenfileirar())
        self.assertEqual('*', fila.desenfileirar())
        self.assertEqual('2', fila.desenfileirar())
        self.assertEqual('.', fila.desenfileirar())
        self.assertEqual('0', fila.desenfileirar())
        self.assertTrue(fila.vazia())

    def test_divisao(self):
        fila = analise_lexica('1/2.0')
        self.assertEqual('1', fila.desenfileirar())
        self.assertEqual('/', fila.desenfileirar())
        self.assertEqual('2', fila.desenfileirar())
        self.assertEqual('.', fila.desenfileirar())
        self.assertEqual('0', fila.desenfileirar())
        self.assertTrue(fila.vazia())

    def test_expresao_com_todos_simbolos(self):
        expressao = '1/{2.0+3*[7-(5-3)]}'
        fila = analise_lexica(expressao)
        self.assertListEqual(list(expressao), [e for e in fila])
        self.assertTrue(fila.vazia())


class AnaliseSintaticaTestes(unittest.TestCase):
    def test_fila_vazia(self):
        fila = Fila()
        self.assertRaises(ErroSintatico, analise_sintatica, fila)

    def test_int(self):
        fila = Fila()
        fila.enfileirar('1234567890')
        fila_sintatica = analise_sintatica(fila)
        self.assertEqual(1234567890, fila_sintatica.desenfileirar())
        self.assertTrue(fila_sintatica.vazia())

    def test_float(self):
        fila = Fila()
        fila.enfileirar('1234567890')
        fila.enfileirar('.')
        fila.enfileirar('4')
        fila_sintatica = analise_sintatica(fila)
        self.assertEqual(1234567890.4, fila_sintatica.desenfileirar())
        self.assertTrue(fila_sintatica.vazia())

    def test_expressao_com_todos_elementos(self):
        fila = analise_lexica('1000/{222.125+3*[7-(5-3)]}')
        fila_sintatica = analise_sintatica(fila)
        self.assertListEqual([1000, '/', '{', 222.125, '+', 3, '*', '[', 7, '-', '(', 5, '-', 3, ')', ']', '}'],
                             [e for e in fila_sintatica])


class AvaliacaoTestes(unittest.TestCase):
    def test_expressao_vazia(self):
        self.assertRaises(ErroSintatico, avaliar, '')

    def test_inteiro(self):
        self.assert_avaliacao('1')

    def test_float(self):
        self.assert_avaliacao('2.1')

    def test_soma(self):
        self.assert_avaliacao('2+1')

    def test_subtracao_e_parenteses(self):
        self.assert_avaliacao('(2-1)')

    def test_expressao_com_todos_elementos(self):
        self.assertEqual(1.0, avaliar('2.0/[4*3+1-{15-(1+3)}]'))

    def assert_avaliacao(self, expressao):
        self.assertEqual(eval(expressao), avaliar(expressao))


if __name__ == '__main__':
    unittest.main()