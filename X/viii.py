#kohonen self organising map
import numpy as np
import matplotlib.pyplot as plt

# Input Data
data = np.array([[1, 1],[1, 2],[2, 1],[8, 8],[8, 9],[9, 8]])

# SOM Size
rows = 2
cols = 2

# Initialize Weights Randomly
np.random.seed(1)
weights = np.random.rand(rows, cols, 2)

# Learning Rate
learning_rate = 0.5

# Training
for epoch in range(100):
    for x in data:
        # Find Best Matching Unit (BMU)
        distances = np.linalg.norm(weights - x, axis=2)
        bmu = np.unravel_index(
            np.argmin(distances), distances.shape
        )

        # Update BMU Weights
        weights[bmu] = weights[bmu] + learning_rate * (x - weights[bmu])

    # Reduce Learning Rate
    learning_rate *= 0.99

print("Final SOM Weights:")
print(weights)

print("\nCluster Assignment:")
for x in data:
    distances = np.linalg.norm(weights - x, axis=2)
    bmu = np.unravel_index(
        np.argmin(distances), distances.shape
    )
    print(x, "-> Neuron", bmu)