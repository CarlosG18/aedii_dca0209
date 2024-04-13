import pytest
from binarysearchtree import *

def size_tree(node):
    """
        função responsavel por calcular a quantidade de nos filhos dado um nó pai.

        argumentos:
            - node: nó pai que se deseja saber calcular quantos nós filhos possui

        retorno:
            - size: quantidade de nós filhos que o nó (node) possui
    """
    if node is None:
       return 0

    left_count  = size_tree(node.left_child) if node.left_child else 0
    right_count  = size_tree(node.right_child) if node.right_child else 0

    return 1 + left_count + right_count

def search_element(vector, node, index_aux):
    """
        função que obtem um vetor com o nó desejado

        argumentos:
            - vector: vetor que armazenará o valor correto
            - node: nó pai que começará a adição
            - index_aux: variavel de auxilio para encontrar o valor correto

        retorno:
            - index_aux: variavel de auxilio para encontrar o valor correto
            - vector: vetor com o valor correto
    """
    if node.right_child is not None:
        index_aux, vector = search_element(vector, node.right_child,index_aux)

    index_aux -= 1
    if index_aux == 0:
        vector.append(node.value)
    
    if node.left_child is not None:
        index_aux, vector = search_element(vector, node.left_child, index_aux)

    return index_aux, vector

def findKthLargestValue(tree, k):
    """
    Finds the kth largest integer in a Binary Search Tree (BST).

    The function traverses the BST in an in-order manner to collect the node values in a sorted list.
    It then returns the kth largest value from this list. The BST is assumed to contain only integer values.
    In case of duplicate integers, they are treated as distinct values.
    The kth largest integer is determined in the context of these distinct values.

    Parameters:
    tree (BST): the Binary Search Tree (BST).
    k (int): A positive integer representing the kth position.

    Returns:
    int: The kth largest integer present in the BST.
    """
    vector = []
    index_aux = k
    
    if tree.root.right_child is not None:
        qtd_right_tree = size_tree(tree.root.right_child)
    else: 
        qtd_right_tree = 0
    
    if k > qtd_right_tree:
        index_aux -= qtd_right_tree
        if index_aux == 1:
            return tree.root.value
        else:
            index_aux -= 1
            _, vector = search_element(vector, tree.root.left_child, index_aux)
    else:
        _, vector = search_element(vector, tree.root.right_child, index_aux)

    return vector[0]

@pytest.fixture(scope="session")
def data():

    array = [[15,5,20,17,22,2,5,1,3],
             [5,4,6,3,7],
             [5],
             [20,15,25,10,19,21,30,22],
             [1,2,3,4,5],
             [10,8,6,4,2],
             [10,8,6,9,4,7,2,5,3],
             [99727,99,727],
             [15,5,20,17,22,24,23,25,2,5,1,3],
             [15,5,20,17,22,2,5,1,3],
             [15,5,20,17,22,2,5,1,3]
             ]
    return array

def test_1(data):
    bst = BST()
    for value in data[0]:
      bst.add(value)
    assert findKthLargestValue(bst, 3) == 17

def test_2(data):
    bst = BST()
    for value in data[1]:
      bst.add(value)
    assert findKthLargestValue(bst, 1) == 7

def test_3(data):
    bst = BST()
    for value in data[2]:
      bst.add(value)
    assert findKthLargestValue(bst, 1) == 5

def test_4(data):
    bst = BST()
    for value in data[3]:
      bst.add(value)
    assert findKthLargestValue(bst, 3) == 22

def test_5(data):
    bst = BST()
    for value in data[4]:
      bst.add(value)
    assert findKthLargestValue(bst, 5) == 1

def test_6(data):
    bst = BST()
    for value in data[5]:
      bst.add(value)
    assert findKthLargestValue(bst, 2) == 8

def test_7(data):
    bst = BST()
    for value in data[6]:
      bst.add(value)
    assert findKthLargestValue(bst, 5) == 6

def test_8(data):
    bst = BST()
    for value in data[7]:
      bst.add(value)
    assert findKthLargestValue(bst, 1) == 99727

def test_9(data):
    bst = BST()
    for value in data[8]:
      bst.add(value)
    assert findKthLargestValue(bst, 7) == 15

def test_10(data):
    bst = BST()
    for value in data[9]:
      bst.add(value)
    assert findKthLargestValue(bst, 5) == 5

def test_11(data):
    bst = BST()
    for value in data[10]:
      bst.add(value)
    assert findKthLargestValue(bst, 6) == 5
