import numpy as np

arr = np.random.randint(low=0, high=10, size=(5))

print("Фильтрация масок на numpy")
print(f"\nНаш созданный массив: {arr}")
print(f"\nВыберем числа, которые больше пяти: \n{arr > 5}")
print(f"\nВыберем числа которые больше 5 и меньше одного: \n{(arr > 5) & (arr < 2)}")

print(f"\nФильтрая масок на pytrhon")
lst = [3, 8, 1, 12, 7, 4, 9]

# Через list comprehension:
print([x for x in lst if x > 5])

# Сложное условие:
print([x for x in lst if x > 5 and x < 10])

# Чётные:
print([x for x in lst if x % 2 == 0])