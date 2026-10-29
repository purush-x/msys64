#simple linear neural network model
import numpy as np
input = np.array([[0,0], [0,1], [1,0], [1,1]])
target = np.array([0, 0, 0, 1])

weights = np.array([1, 1])
bias = -1.5

def step_function(x):
    if x < 0:
        return 0
    else:
        return 1

print("Predicted output")

for i in range(len(input)):
    net = np.dot(input[i], weights) + bias
    print(input[i],"->", step_function(net))