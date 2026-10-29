#implement hebb's learning
import numpy as np

input = np.array([[1, 1],[1, -1],[-1, 1],[-1, -1]])
output = np.array([1, -1, -1, 1])

weights = np.array([0, 0])

for i in range(len(input)):
    weights += input[i] * output[i]
    print("Updated Weights after Pattern", i + 1, ":", weights)

print("\nFinal Weights:", weights)