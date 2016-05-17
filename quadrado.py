from collections import Counter
import unittest

lru={0:[0]}
def soma_quadrados(n):
    if n==0:
        return [0]
    quadrados=[]
    maxi=1
    while(maxi*maxi<=n):
        quadrados.append(maxi*maxi)
        maxi=maxi+1
    while len(quadrados)>0:
        valor=n   
        quadrado=quadrados.copy()
        p=quadrado.pop()
        resposta=[]
        while(valor>0):
            if valor in lru.keys() and valor is not n:
                resposta=resposta+lru[valor]
                valor=0
            else:
                if len(quadrado)>0:
                    if ((valor-p)<0):
                       p=quadrado.pop()
                    else:
                        valor=valor-p
                        resposta.append(p)
                        if(valor<quadrado[-1]):
                            p=quadrado.pop()
                else:
                    valor=valor-p
                    resposta.append(p)
        if n not in lru.keys():
            lru[n]=resposta.copy()
        elif len(resposta)<len(lru[n]):
            lru[n]=resposta.copy()
        quadrados.pop()
    return lru[n]

class SomaQuadradosPerfeitosTestes(unittest.TestCase):
    def teste_0(self):
        self.assert_possui_mesmo_elementos([0], soma_quadrados(0))

    def teste_01(self):
        self.assert_possui_mesmo_elementos([1], soma_quadrados(1))

    def teste_02(self):
        self.assert_possui_mesmo_elementos([1, 1], soma_quadrados(2))

    def teste_03(self):
        self.assert_possui_mesmo_elementos([1, 1, 1], soma_quadrados(3))

    def teste_04(self):
        self.assert_possui_mesmo_elementos([4], soma_quadrados(4))

    def teste_05(self):
        self.assert_possui_mesmo_elementos([4, 1], soma_quadrados(5))

    def teste_11(self):
        self.assert_possui_mesmo_elementos([9, 1, 1], soma_quadrados(11))

    def teste_12(self):
        self.assert_possui_mesmo_elementos([4, 4, 4], soma_quadrados(12))

    def assert_possui_mesmo_elementos(self, esperado, resultado):
        self.assertEqual(Counter(esperado), Counter(resultado))
if __name__ == '__main__':
    unittest.main()