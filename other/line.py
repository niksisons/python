import numpy as np

# Заданные матрицы
A = np.array([
    [-8.3, 0.2, 9.0],
    [-1.4, 0.8, -8.5],
    [9.1, -6.5, -8.4],
    [2.6, 5.9, -6.4],
    [1.8, 8.3, -7.8]
])

B = np.array([
    [9.5],
    [-0.6], 
    [9.2], 
    [-9.5], 
    [0.2]])

# Метод наименьших квадратов
X0 = np.linalg.inv(A.T @ A) @ A.T @ B

# Проверка решения
approx_B = A @ X0

# Вектор невязок
V = approx_B - B

# Норма вектора невязок
norm_V = np.linalg.norm(V)

print("Решение X0:")
print(X0)

print("\nПроверка решения:")
print("A * X0:")
print(approx_B)

print("\nВектор невязок V:")
print(V)

print("\nНорма вектора невязок:")
print(norm_V)
