#backropagation MLP 1. backpropagation XOR
import numpy as np

X = np.array([[0, 0],[0, 1],[1, 0],[1, 1]])

y = np.array([[0],[1],[1],[0]])

def sigmoid(x): return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):return x * (1 - x)

np.random.seed(1)

weights_input_hidden = np.random.rand(2, 2)
weights_hidden_output = np.random.rand(2, 1)

learning_rate = 0.5

for epoch in range(10000):

    hidden_input = np.dot(X, weights_input_hidden)
    hidden_output = sigmoid(hidden_input)

    final_input = np.dot(hidden_output, weights_hidden_output)
    predicted_output = sigmoid(final_input)

    error = y - predicted_output

    output_delta = error * sigmoid_derivative(predicted_output)

    hidden_error = np.dot(
        output_delta,
        weights_hidden_output.T
    )

    hidden_delta = hidden_error * sigmoid_derivative(hidden_output)

    weights_hidden_output += learning_rate * np.dot(
        hidden_output.T,
        output_delta
    )

    weights_input_hidden += learning_rate * np.dot(
        X.T,
        hidden_delta
    )
print("Predicted Output:")
print(np.round(predicted_output))



