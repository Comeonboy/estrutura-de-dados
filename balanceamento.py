import unittest

class Pilha():
    def __init__(self):
        self._lista = []

    def vazia(self):
        return len(self._lista) == 0

    def topo(self):
        if self._lista:
            return self._lista[-1]
        raise PilhaVaziaErro();

    def empilhar(self, valor):
        self._lista.append(valor)

    def desempilhar(self):
        try:
            return self._lista.pop()
        except IndexError:
            raise PilhaVaziaErro()

class PilhaVaziaErro(Exception):
    pass


def esta_balanceada(expressao):
    pilha = Pilha()
    for i in range(len(expressao)):
        if expressao[i] == '(' or expressao[i] == '{' or expressao[i] == '[':
            pilha.empilhar(expressao[i])
        elif expressao[i] == ')':
            try:
                if pilha.topo() != '(':
                    return False
                else:
                    pilha.desempilhar()
            except PilhaVaziaErro:
                return False
        elif expressao[i] == '}':
            try:
                if pilha.topo() != '{':
                    return False
                else:
                    pilha.desempilhar()
            except PilhaVaziaErro:
                return False
        elif expressao[i] == ']':
            try:
                if pilha.topo() != '[':
                    return False
                else:
                    pilha.desempilhar()
            except PilhaVaziaErro:
                return False
    if pilha.vazia():
        return True
    else:
        return False

class BalancearTestes(unittest.TestCase):
    def test_expressao_vazia(self):
        self.assertTrue(esta_balanceada(''))

    def test_parenteses(self):
        self.assertTrue(esta_balanceada('()'))

    def test_chaves(self):
        self.assertTrue(esta_balanceada('{}'))

    def test_colchetes(self):
        self.assertTrue(esta_balanceada('[]'))

    def test_todos_caracteres(self):
        self.assertTrue(esta_balanceada('({[]})'))
        self.assertTrue(esta_balanceada('[({})]'))
        self.assertTrue(esta_balanceada('{[()]}'))

    def test_chave_nao_fechada(self):
        self.assertFalse(esta_balanceada('{'))

    def test_colchete_nao_fechado(self):
        self.assertFalse(esta_balanceada('['))

    def test_parentese_nao_fechado(self):
        self.assertFalse(esta_balanceada('('))

    def test_chave_nao_aberta(self):
        self.assertFalse(esta_balanceada('}{'))

    def test_colchete_nao_aberto(self):
        self.assertFalse(esta_balanceada(']['))

    def test_parentese_nao_aberto(self):
        self.assertFalse(esta_balanceada(')('))

    def test_falta_de_caracter_de_fechamento(self):
        self.assertFalse(esta_balanceada('({[]}'))

    def test_falta_de_caracter_de_abertura(self):
        self.assertFalse(esta_balanceada('({]})'))

    def test_expressao_matematica_valida(self):
        self.assertTrue(esta_balanceada('({[1+3]*5}/7)+9'))

    def test_char_errado_fechando(self):
        self.assertFalse(esta_balanceada('[)'))
        
if __name__ == '__main__':
    unittest.main()
