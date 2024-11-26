# Функции в Python
# Функция создания матрицы
# def get_matrix(n, m, the_value):
#     matrix=[]
#     for i in range(0, n):
#         inner_matrix = []
#         for j in range(0, m):
#             inner_matrix.append(the_value)
#         matrix.append(inner_matrix)
#     return matrix
def get_matrix(i, j, val):
    matrix = [[val for i in range(i)] for j in range(j)]
    return matrix

#Вызов функции
result1 = get_matrix(2, 2, 10) # вызов функции для матрицы1
result2 = get_matrix(3, 5, 42) # вызов функции для матрицы2
result3 = get_matrix(4, 2, 13) # вызов функции для матрицы3
print('Матрица1:', result1)
print('Матрица2:', result2)
print('Матрица3:', result3)