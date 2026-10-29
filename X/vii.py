#implement hebbian learning algo using and & or gates
import numpy as np
# AND gate input
X = np.array([
 [1, 1],
 [1, -1],
 [-1, 1],
 [-1, -1]
])
# Target output
Y = np.array([1, -1, -1, -1])
# Initialize weights
weights = np.array([0, 0])
# Hebbian Learning
for i in range(len(X)):
 weights = weights + X[i] * Y[i]
print("Final Weights:", weights)
# Testing
print("\nTesting AND Gate:")
for i in range(len(X)):
 net = np.dot(X[i], weights)
 if net >= 0:
 output = 1
 else:
 output = -1
 print(X[i], "->", output)



 import numpy as np
# OR gate input
X = np.array([
 [1, 1],
 [1, -1],
 [-1, 1],
 [-1, -1]
])
# Target output
Y = np.array([1, 1, 1, -1])
# Initialize weights
weights = np.array([0, 0])
# Hebbian Learning
for i in range(len(X)):
 weights = weights + X[i] * Y[i]
print("Final Weights:", weights)
# Testing
print("\nTesting OR Gate:")
for i in range(len(X)):
 net = np.dot(X[i], weights)
 if net >= 0:
 output = 1
 else:
 output = -1
 print(X[i], "->", output)