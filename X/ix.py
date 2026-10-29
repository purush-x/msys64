#hopified neural network -associative memory

import numpy as np

# Training Patterns
patterns = np.array([[1, 1, -1, -1],[-1, -1, 1, 1]])

# Number of Neurons
n = patterns.shape[1]

# Initialize Weight Matrix
weights = np.zeros((n, n))

# Calculate Weights
for pattern in patterns:
    weights += np.outer(pattern, pattern)

# Remove Self-Connections
np.fill_diagonal(weights, 0)

print("Weight Matrix:")
print(weights)

# Noisy Input Pattern
input_pattern = np.array([1, -1, -1, -1])

# Copy Input Pattern
state = input_pattern.copy()

# Recall the Stored Pattern
for iteration in range(10):
    # Calculate New State
    new_state = np.sign(np.dot(weights, state))

    # Replace 0 with 1
    new_state[new_state == 0] = 1

    print("Iteration", iteration + 1, ":", new_state)

    # Check Stable State
    if np.array_equal(new_state, state):
        break

    state = new_state

print("\nRecalled Pattern:")
print(state)