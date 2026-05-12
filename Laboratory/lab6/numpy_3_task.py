import numpy as np

b = np.array([[1.3, 3.1, 5.6],
              [2.7, 4.9, 6.2]])

print(f"""Для массива "b":
===
Сумма: {np.sum(b)} 
Cумма по столбцам: {np.sum(b, axis=0)} 
Сумма по строкам: {np.sum(b, axis=1)} 
Среднее по строкам: {np.mean(b, axis=0)}
Среднее по столбцам: {np.mean(b, axis=1)}
Максимум по стобцам: {np.max(b, axis=0)}
Максимум по строкам: {np.max(b, axis=1)}
===""")

b_copy = [[1.3, 3.1, 5.6], [2.7, 4.9, 6.2]]
print("На Python")
general = 0
for count in b_copy:
    for elem in count:
        general += elem
print(f"Сумма всей матрицы: {general}")

str_sum = []
for count in b_copy:
    str_sum.append(float(sum(count)))
print(f"Сумма по строкам: {str_sum}")

stlssss_sum = []
for j in range(len(b_copy[0])):
    stl_sum = 0
    for i in range(len(b_copy)):
        stl_sum += b_copy[i][j]
    stlssss_sum.append(stl_sum)
print(f"Сумма всей матрицы по столбцам: {stlssss_sum}")

avg_sum_str = []
for count in b_copy:
    avg_sum_str.append(float(sum(count) / len(count)))
print(f"Среднее по строкам: {avg_sum_str}")

avg_sum_stl = []
cols = len(b_copy[0])
counts = len(b_copy)
for j in range(cols):
    s = 0
    for i in range(cols):
        s = 0
        for i in range(counts):
            s += b_copy[i][j]
        avg_sum_stl.append(s / counts)
print(f"Среднее по стобцам: {avg_sum_stl}")

row_max = [max(count) for count in b_copy]
row_min = [min(count) for count in b_copy]
print(f"""Максимум по строкам: {row_max}
Минимум по строкам: {row_min}
""")

col_max = []
col_min = []
for j in range(cols):
    column = [b_copy[i][j] for i in range(counts)]
    col_max.append(max(column))
    col_min.append(min(column))
print(f"Максимум по столбцам: {col_max}")
print(f"Минимум по столбцам: {col_min}")
