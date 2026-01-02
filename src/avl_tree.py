# avl_tree.py
# Implementação simples de uma Árvore AVL
# Variáveis e métodos em português

class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None
        self.altura = 1


class ArvoreAVL:
    # Retorna a altura de um nó
    def obter_altura(self, no):
        if no is None:
            return 0
        return no.altura

    # Retorna o fator de balanceamento
    def obter_balanceamento(self, no):
        if no is None:
            return 0
        return self.obter_altura(no.esquerda) - self.obter_altura(no.direita)

    # Rotação simples à direita (caso LL)
    def rotacao_direita(self, y):
        x = y.esquerda
        t2 = x.direita

        # Realiza rotação
        x.direita = y
        y.esquerda = t2

        # Atualiza alturas
        y.altura = 1 + max(self.obter_altura(y.esquerda),
                           self.obter_altura(y.direita))
        x.altura = 1 + max(self.obter_altura(x.esquerda),
                           self.obter_altura(x.direita))

        return x

    # Rotação simples à esquerda (caso RR)
    def rotacao_esquerda(self, x):
        y = x.direita
        t2 = y.esquerda

        # Realiza rotação
        y.esquerda = x
        x.direita = t2

        # Atualiza alturas
        x.altura = 1 + max(self.obter_altura(x.esquerda),
                           self.obter_altura(x.direita))
        y.altura = 1 + max(self.obter_altura(y.esquerda),
                           self.obter_altura(y.direita))

        return y

    # Inserção de um valor na árvore AVL
    def inserir(self, no, valor):
        # Inserção normal de BST
        if no is None:
            return No(valor)

        if valor < no.valor:
            no.esquerda = self.inserir(no.esquerda, valor)
        elif valor > no.valor:
            no.direita = self.inserir(no.direita, valor)
        else:
            return no  # valores repetidos não são permitidos

        # Atualiza altura do nó atual
        no.altura = 1 + max(self.obter_altura(no.esquerda),
                            self.obter_altura(no.direita))

        # Verifica balanceamento
        balanceamento = self.obter_balanceamento(no)

        # Caso LL
        if balanceamento > 1 and valor < no.esquerda.valor:
            return self.rotacao_direita(no)

        # Caso RR
        if balanceamento < -1 and valor > no.direita.valor:
            return self.rotacao_esquerda(no)

        # Caso LR
        if balanceamento > 1 and valor > no.esquerda.valor:
            no.esquerda = self.rotacao_esquerda(no.esquerda)
            return self.rotacao_direita(no)

        # Caso RL
        if balanceamento < -1 and valor < no.direita.valor:
            no.direita = self.rotacao_direita(no.direita)
            return self.rotacao_esquerda(no)

        return no

    # Impressão em ordem (para teste)
    def em_ordem(self, no):
        if no is not None:
            self.em_ordem(no.esquerda)
            print(no.valor, end=" ")
            self.em_ordem(no.direita)
