from data import *
import math
from random import seed, random
from functions import *

seed(seed_value)
def iterate_matrices(matrix, callback):
    for i in range(count_of_vertexes):
        for j in range(count_of_vertexes):
            matrix[i][j] = callback(i, j)


def B_callback(i, j):
    return random()*2

A = create_matrix_for_undirected_graph(create_matrix_for_directed_graph(count_of_vertexes))
print("матриця ненапрямленого графа")
for row in A:
    print(row)


B = create_zero_matrix(count_of_vertexes)
iterate_matrices(B, B_callback)

C = create_zero_matrix(count_of_vertexes)
def C_callback(i, j):
    return math.ceil(A[i][j] * B[i][j] * 100)
iterate_matrices(C, C_callback)

D = create_zero_matrix(count_of_vertexes)
def D_callback(i, j):
    return 1 if C[i][j] else 0
iterate_matrices(D, D_callback)

H = create_zero_matrix(count_of_vertexes)
def H_callback(i, j):
    return 0 if D[i][j] == D[j][i] else 1
iterate_matrices(H, H_callback)

Tr = create_zero_matrix(count_of_vertexes)
def Tr_callback(i, j):
    return 1 if i < j else 0
iterate_matrices(Tr, Tr_callback)

def create_W():
    W = create_zero_matrix(count_of_vertexes)
    def W_callback(i, j):
        if i > j:
            return W[j][i]
        elif i < j:
            return (D[i][j] + H[i][j] * Tr[i][j]) * C[i][j]
        else:
            return 0
    iterate_matrices(W, W_callback)
    print("\nматриця ваг ненапрямленого графа:")
    for row in W:
        print(row)
    return W