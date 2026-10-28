#perceptron learning algo
import numpy as np

# Input Data
X = np.array([[0, 0],
              [0, 1],
              [1, 0],
              [1, 1]])

# AND Gate Output
and_output = [0, 0, 0, 1]

# OR Gate Output
or_output = [0, 1, 1, 1]

# Step Activation Function
def step(x):
    if x >= 0:
        return 1
    else:
        return 0

print("AND Gate")

weights = np.array([1, 1])
bias = -1.5

for i in range(len(X)):
    net = np.dot(X[i], weights) + bias
    print(X[i], "->", step(net))

print("\nOR Gate")

bias = -0.5

for i in range(len(X)):
    net = np.dot(X[i], weights) + bias
    print(X[i], "->", step(net))