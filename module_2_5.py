# Функции в Python
# Функция создания матрицы
def get_matrix(n, m, the_value):
    matrix=[0]*n
    for i in range(0, n):
        matrix[i]=[0]*m
        for j in range(0, m):
            matrix[i][j] = the_value
    return matrix

# Вызов функции
result1 = get_matrix(2, 2, 10) # вызов функции для матрицы1
result2 = get_matrix(3, 5, 42) # вызов функции для матрицы2
result3 = get_matrix(4, 2, 13) # вызов функции для матрицы3
print('Матрица1:', result1)
print('Матрица2:', result2)
print('Матрица3:', result3)