# exemplo de arvore basica 

class NoArvore:
    def __init__(self, valor):
        self.valor = valor
        self.filho_esquerda = None
        self.filho_direita = None
class ArvoreBinaria:
    def __init__(self, raiz):
        self.raiz = NoArvore(raiz)

    def inserir(self, valor):
        self._inserir_recursivamente(self.raiz, valor)
        def _inserir_recursivamente(self, no, valor):
            if valor < no.valor:
                if no.filho_esquerda is None:
                    no .filho_esquerda = NoArvore(valor)
                else:
                    self._inserir_recursivamente(no.filho_esquerda, valor)
            else:
                if no.filho_direita is None:
                    no.filho_direita = NoArvore(valor)