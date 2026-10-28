#hebb's learning
import numpy as np

X = np.array([
    [1, 1],
    [1, -1],
    [-1, 1],
    [-1, -1]
])

Y = np.array([1, -1, -1, 1])

weights = np.array([0, 0])

for i in range(len(X)):
    weights = weights + X[i] * Y[i]
    print("Updated Weights after Pattern", i + 1, ":", weights)

print("\nFinal Weights:", weights)