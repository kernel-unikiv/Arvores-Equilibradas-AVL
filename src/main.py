# main.py
# Exemplo de utilização da Árvore AVL

from avl_tree import ArvoreAVL

if __name__ == "__main__":
    arvore = ArvoreAVL()
    raiz = None

    valores = [50, 20, 10, 40, 30, 90]

    for valor in valores:
        raiz = arvore.inserir(raiz, valor)

    print("Valores da árvore AVL em ordem:")
    arvore.em_ordem(raiz)
