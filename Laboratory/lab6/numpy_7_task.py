import numpy as np
import time


print("Типы данных, память и скорость")

# 1. Переполнение int8
a = np.array([100, 100], dtype=np.int8)
print(f"int8 сумма с переполнением: {np.sum(a, dtype=np.int8)}")
print(f"int32 сумма без переполнения: {np.sum(a, dtype=np.int32)}")

# 2. Память: один массив — разные типы
size = 1_000_000
for dtype in [np.int8, np.int16, np.int32, np.int64, np.float32, np.float64]:
    arr = np.ones(size, dtype=dtype)
    print(f"{str(dtype):<12}: {arr.nbytes:>10,} байт")

# 3. Скорость NumPy vs Python
big = np.random.randint(0, 1000, 10_000_000)
lst = big.tolist()

t = time.time(); np.sum(big); np_t = time.time() - t
t = time.time(); sum(lst);   py_t = time.time() - t

print(f"\nNumPy:  {np_t:.6f} сек")
print(f"Python: {py_t:.6f} сек")
print(f"NumPy быстрее в {py_t/np_t:.1f} раз")