# test_avl.py
# Teste simples da inserção AVL

from src.avl_tree import ArvoreAVL

def test_insercao_simples():
    arvore = ArvoreAVL()
    raiz = None

    valores = [10, 20, 30]
    for valor in valores:
        raiz = arvore.inserir(raiz, valor)

    assert raiz.valor == 20
