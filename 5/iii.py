#perceptron learning algo for bianry classification AND OR
import numpy as np

input = np.array([[0, 0],[0, 1],[1, 0],[1, 1]])

and_output = [0, 0, 0, 1]
or_output = [0, 1, 1, 1]

def step_function(x):
    if x < 0:
        return 0
    else:
        return 1

print("AND Gate")

weights = np.array([1, 1])
bias = -1.5

for i in range(len(input)):
    net = np.dot(input[i], weights) + bias
    print(input[i], "->", step_function(net))

print("\nOR Gate")

bias = -0.5

for i in range(len(input)):
    net = np.dot(input[i], weights) + bias
    print(input[i], "->", step_function(net))