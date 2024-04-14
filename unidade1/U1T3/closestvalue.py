import pytest
from binarysearchtree import *


def findClosestValue(tree, target):
    """
    Finds the value in a binary search tree that is closest to the given target value.

    Parameters:
    tree (BST): The binary search tree object in which to find the closest value.
                It is expected to have a 'root' attribute that points to the root node of the tree.
    target (int): The target value for which the closest value in the binary search tree is sought.

    Returns:
    int: The value in the binary search tree that is closest to the target value.
    """

    # Iniciando a variável como nula
    closest_value = None

    # Função auxiliar para percorrer recursivamente
    def traverse(node):
        nonlocal closest_value

        # Caso base: se o nó atual analisado for nulo, retorne a função imediatamente
        if node is None:
            return

        # Atualiza o valor mais próximo (na variável) caso seja necessário
        if closest_value is None or abs(node.value - target) < abs(closest_value - target):
            closest_value = node.value

        # Continua a busca atravessando a árvore com base nas propriedades da BST
        if target < node.value:
            traverse(node.left_child)
        elif target > node.value:
            traverse(node.right_child)

    # Inicia a busca/travessia a partir do nó raiz da árvore
    traverse(tree.root)

    return closest_value

@pytest.fixture(scope="session")
def data():

    array = [[10, 5, 15, 13, 22, 14, 2, 5, 1],
             [100,5,502,204,55000,1001,4500,203,205,207,
              206,208,2,15,5,22,57,60,1,3,-51,1,1,1,1,1,-403]
             ]
    return array

def test_1(data):
    bst = BST()
    for value in data[0]:
      bst.add(value)
    assert findClosestValue(bst, 12) == 13

def test_2(data):
    bst = BST()
    for value in data[1]:
      bst.add(value)
    assert findClosestValue(bst, 100) == 100

def test_3(data):
    bst = BST()
    for value in data[1]:
      bst.add(value)
    assert findClosestValue(bst, 208) == 208

def test_4(data):
    bst = BST()
    for value in data[1]:
      bst.add(value)
    assert findClosestValue(bst, 4500) == 4500

def test_5(data):
    bst = BST()
    for value in data[1]:
      bst.add(value)
    assert findClosestValue(bst, 4501) == 4500

def test_6(data):
    bst = BST()
    for value in data[1]:
      bst.add(value)
    assert findClosestValue(bst, -70) == -51

def test_7(data):
    bst = BST()
    for value in data[1]:
      bst.add(value)
    assert findClosestValue(bst, 2000) == 1001

def test_8(data):
    bst = BST()
    for value in data[1]:
      bst.add(value)
    assert findClosestValue(bst, 6) == 5

def test_9(data):
    bst = BST()
    for value in data[1]:
      bst.add(value)
    assert findClosestValue(bst, 30000) == 55000

def test_10(data):
    bst = BST()
    for value in data[1]:
      bst.add(value)
    assert findClosestValue(bst, -1) == 1

def test_11(data):
    bst = BST()
    for value in data[1]:
      bst.add(value)
    assert findClosestValue(bst, 29751) == 55000

def test_12(data):
    bst = BST()
    for value in data[1]:
      bst.add(value)
    assert findClosestValue(bst, 29749) == 4500

