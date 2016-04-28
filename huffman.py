def calcular_frequencias(s):
    quantidade = {}
    for a in s:
        if a in quantidade.keys():
            quantidade[a] += 1
        else:
            quantidade[a] = 1
    return quantidade


def gerar_arvore_de_huffman(s):
    dicionario = calcular_frequencias(s)
    for a,b in dicionario.items():
        char = a
        menor = b
        break
    for a,b in dicionario.items():
        if b <= menor:
            menor = b
            char = a
    dicionario.__delitem__(char)
    arvore = Arvore(char,menor)
    while len(dicionario.keys())>0:
        for a,b in dicionario.items():
            char = a
            menor = b
            break
        for a,b in dicionario.items():
            if b <= menor:
                char = a
                menor = b
        arvore = arvore.fundir(Arvore(char,menor))
        dicionario.__delitem__(char)
    return arvore
    pass


def codificar(cod_dict, s):
    codigo = ""
    for i in s:
        codigo = codigo + cod_dict.get(i)
    return codigo



class Noh:
    def __init__(self, peso, esquerdo = None, direito = None):
        self.peso = peso
        self.esquerdo = esquerdo
        self.direito = direito
        self.nome = "Noh"

        
    def __hash__(self):
        return hash(self.peso)

    def __eq__(self, other):
        if other is None or not isinstance(other, Noh):
            return False
        return self.peso == other.peso and self.esquerdo == other.esquerdo and self.direito == other.direito


class Folha():
    def __init__(self, char, peso):
        self.char = char
        self.peso = peso
        self.noh = Noh(peso)
        self.nome = "Folha"
        
    def __hash__(self):
        return hash(self.__dict__)

    def __eq__(self, other):
        if other is None or not isinstance(other, Folha):
            return False
        return self.__dict__ == other.__dict__


class Arvore(object):
    def __init__(self, charRaiz = None, pesoRaiz = None):
        self.dicionario = {}
        if charRaiz is None or pesoRaiz is None:
            self.raiz = None
        else:
            self.raiz = Folha(charRaiz, pesoRaiz)
            
    def fundir(self, arvore):
        arvoreNova = Arvore()
        arvoreNova.raiz = Noh(self.raiz.peso+arvore.raiz.peso)
        if self.raiz.peso > arvore.raiz.peso:
            arvoreNova.raiz.esquerdo = self.raiz
            arvoreNova.raiz.direito = arvore.raiz
        else:
            arvoreNova.raiz.direito=self.raiz
            arvoreNova.raiz.esquerdo=arvore.raiz
        return arvoreNova

    def cod_dict(self):
        gerar_dicionario(self.raiz, self.dicionario)
        return self.dicionario

    def decodificar(self,caminho):
        resultado = ""
        item = ""
        self.cod_dict()
        for i in caminho:
            item = item+i
            for a,b in self.dicionario.items():
                if b == item:
                    resultado = resultado + a
                    item = ""
        return resultado
        
        
    def __hash__(self):
        return hash(self.raiz)

    def __eq__(self, other):
        if other is None:
            return False
        return self.raiz == other.raiz

def gerar_dicionario(item, dicionario, caminho = ''):
    if item.nome is "Folha":
        dicionario[item.char] = str(caminho)
    else:
        gerar_dicionario(item.direito, dicionario, caminho + '1')
        gerar_dicionario(item.esquerdo, dicionario, caminho + '0')

import unittest
from unittest import TestCase


class CalcularFrequenciaCarecteresTestes(TestCase):
    def teste_string_vazia(self):
        self.assertDictEqual({}, calcular_frequencias(''))

    def teste_string_nao_vazia(self):
        self.assertDictEqual({'a': 3, 'b': 2, 'c': 1}, calcular_frequencias('aaabbc'))


class NohTestes(TestCase):
    def teste_folha_init(self):
        folha = Folha('a', 3)
        self.assertEqual('a', folha.char)
        self.assertEqual(3, folha.peso)

    def teste_folha_eq(self):
        self.assertEqual(Folha('a', 3), Folha('a', 3))
        self.assertNotEqual(Folha('a', 3), Folha('b', 3))
        self.assertNotEqual(Folha('a', 3), Folha('a', 2))
        self.assertNotEqual(Folha('a', 3), Folha('b', 2))

    def testes_eq_sem_filhos(self):
        self.assertEqual(Noh(2), Noh(2))
        self.assertNotEqual(Noh(2), Noh(3))

    def testes_eq_com_filhos(self):
        noh_com_filho = Noh(2)
        noh_com_filho.esquerdo = Noh(3)
        self.assertNotEqual(Noh(2), noh_com_filho)

    def teste_noh_init(self):
        noh = Noh(3)
        self.assertEqual(3, noh.peso)
        self.assertIsNone(noh.esquerdo)
        self.assertIsNone(noh.direito)


def _gerar_arvore_aaaa_bb_c():
    raiz = Noh(7)
    raiz.esquerdo = Folha('a', 4)
    noh = Noh(3)
    raiz.direito = noh
    noh.esquerdo = Folha('b', 2)
    noh.direito = Folha('c', 1)
    arvore_esperada = Arvore()
    arvore_esperada.raiz = raiz
    return arvore_esperada


class ArvoreTestes(TestCase):
    def teste_init_com_defaults(self):
        arvore = Arvore()
        self.assertIsNone(arvore.raiz)

    def teste_init_sem_defaults(self):
        arvore = Arvore('a', 3)
        self.assertEqual(Folha('a', 3), arvore.raiz)

    def teste_fundir_arvores_iniciais(self):
        raiz = Noh(3)
        raiz.esquerdo = Folha('b', 2)
        raiz.direito = Folha('c', 1)
        arvore_esperada = Arvore()
        arvore_esperada.raiz = raiz

        arvore = Arvore('b', 2)
        arvore2 = Arvore('c', 1)
        arvore_fundida = arvore.fundir(arvore2)
        self.assertEqual(arvore_esperada, arvore_fundida)

    def teste_fundir_arvores_nao_iniciais(self):
        arvore_esperada = _gerar_arvore_aaaa_bb_c()

        arvore = Arvore('b', 2)
        arvore2 = Arvore('c', 1)
        arvore3 = Arvore('a', 4)
        arvore_fundida = arvore.fundir(arvore2)
        arvore_fundida = arvore3.fundir(arvore_fundida)

        self.assertEqual(arvore_esperada, arvore_fundida)

    def teste_gerar_dicionario_de_codificacao(self):
        arvore = _gerar_arvore_aaaa_bb_c()
        self.assertDictEqual({'a': '0', 'b': '10', 'c': '11'}, arvore.cod_dict())

    def teste_decodificar(self):
        arvore = _gerar_arvore_aaaa_bb_c()
        self.assertEqual('aaaabbc', arvore.decodificar('0000101011'))


class TestesDeIntegracao(TestCase):
    def teste_gerar_arvore_de_huffman(self):
        arvore = _gerar_arvore_aaaa_bb_c()
        self.assertEqual(arvore, gerar_arvore_de_huffman('aaaabbc'))

    def teste_codificar(self):
        arvore = gerar_arvore_de_huffman('aaaabbc')
        self.assertEqual('0000101011', codificar(arvore.cod_dict(), 'aaaabbc'))
        self.assertEqual('aaaabbc', arvore.decodificar('0000101011'))

if __name__=='__main__':
    unittest.main()
