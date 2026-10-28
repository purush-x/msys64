#simple linear neural network
import numpy as np

X = np.array([[0, 0],
              [0, 1],
              [1, 0],
              [1, 1]])

y = np.array([0, 0, 0, 1])

weights = np.array([1, 1])
bias = -1.5

def step_function(x):
    if x >= 0:
        return 1
    else:
        return 0

print("Predicted Output")

for i in range(len(X)):
    net = np.dot(X[i], weights) + bias
    output = step_function(net)
    print(X[i], "->", output)