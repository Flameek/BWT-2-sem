import numpy as np

arr = np.random.randint(low=0, high=10, size=(5))
print(f"наш массив: \n{arr}")

sorted_np = np.sort(arr)
max_idx_np = np.argmax(arr)

print(f"\nОтсортированный массив: {sorted_np}")
print(f"\nМаксимальный элемент: {arr[max_idx_np]}")
print(f"\nИндекс максимума: {max_idx_np}")

print("\nPython")
lst6 = arr.tolist()
sorted_py = sorted(lst6)
max_val_py = max(lst6)
max_idx_py = lst6.index(max_val_py)

print(f"Отсортированный список: {sorted_py}")
print(f"Максимальный элемент: {max_val_py}")
print(f"Индекс максимума: {max_idx_py}")