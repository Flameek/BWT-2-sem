import numpy as np

a = np.random.randint(low=0, high=10, size=5)
b = np.random.randint(low=0, high=10, size=(3,5))
print(f"{a}  \n\n{b}")


print("\nBROADCASTING")
print(f"\nМассив a + скаляр: {a + 10}")
print(f"\nМассив b + скаляр: \n{b + 10}")
print(f"\nМассив a + b: \n{a + b}")