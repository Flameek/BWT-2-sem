import numpy as np

a = np.array([1, 2, 3])
b = np.array([[1.3, 3.1, 5.6], [2.7, 4.9, 6.2]])

# ===== Агрегатные функции numpy =====
print(f"""Для массива "a":
===
Сумма: {np.sum(a)} 
Среднее арифметическое: {np.mean(a)} 
Min: {np.min(a)} 
Max: {np.max(a)} 
Стандартное отклонение: {np.std(a):.4f}
===""")

print()

print(f"""Для массива "b":
===
Сумма: {np.sum(b)} 
Среднее арифметическое: {np.mean(b)} 
Min: {np.min(b)} 
Max: {np.max(b)} 
Стандартное отклонение: {np.std(b):.4f}
===""")

print()

# ===== Поэлементные операции между массивами =====
# Для поэлементных операций нужны массивы одинаковой формы
c = np.array([10, 20, 30])                     # одномерный, как a
d = np.array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])  # двумерный, как b

print("Поэлементные операции между массивами:")
print(f"a + c: {a + c}")
print(f"a - c: {a - c}")
print(f"a * c: {a * c}")
print(f"a / c: {a / c}")
print()
print(f"b + d:\n{b + d}")
print(f"b * d:\n{b * d}")
print()

# ===== Операции между массивом и скаляром =====
print("Операции между массивом и скаляром:")
print(f"a + 10: {a + 10}")
print(f"a * 2: {a * 2}")
print(f"a ** 2: {a ** 2}")
print(f"b + 5:\n{b + 5}")
print(f"b * 3:\n{b * 3}")
print()

# ===== Аналогичные операции на чистом python =====
a_list = [1, 2, 3]
c_list = [10, 20, 30]

print("=== ЧИСТЫЙ PYTHON ===")
print(f"Список a: {a_list}")
print()

# Агрегатные функции
print(f"Сумма: {sum(a_list)}")
print(f"Среднее: {sum(a_list) / len(a_list)}")
print(f"Min: {min(a_list)}")
print(f"Max: {max(a_list)}")

# Стандартное отклонение вручную
mean = sum(a_list) / len(a_list)
variance = sum((x - mean) ** 2 for x in a_list) / len(a_list)
std = variance ** 0.5
print(f"Стандартное отклонение: {std:.4f}")
print()

# Поэлементные операции
print(f"a + c: {[x + y for x, y in zip(a_list, c_list)]}")
print(f"a - c: {[x - y for x, y in zip(a_list, c_list)]}")
print(f"a * c: {[x * y for x, y in zip(a_list, c_list)]}")
print(f"a / c: {[x / y for x, y in zip(a_list, c_list)]}")
print()

# Операции со скаляром
print(f"a + 10: {[x + 10 for x in a_list]}")
print(f"a * 2: {[x * 2 for x in a_list]}")
print(f"a ** 2: {[x ** 2 for x in a_list]}")
print()

# Двумерный список — операции
b_list = [[1.3, 3.1, 5.6], [2.7, 4.9, 6.2]]
flat = [x for row in b_list for x in row]

print(f"Сумма b_list: {sum(flat)}")
print(f"Min b_list: {min(flat)}")
print(f"Max b_list: {max(flat)}")
print(f"b_list[i][j] + 5:")
for row in b_list:
    print([x + 5 for x in row])
