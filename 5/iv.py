# XOR function using MLP & Backpropagation Learning Algorithm

from sklearn.neural_network import MLPClassifier
import numpy as np

input = np.array([[0, 0],[0, 1],[1, 0],[1, 1]])

output = np.array([0, 1, 1, 0])

# Create MLP Model
model = MLPClassifier(
    hidden_layer_sizes=(2,),(One hidden layer containing 2 neurons)
    activation='logistic', (sigmoid)
    solver='lbfgs',(Optimization algorithm)
    max_iter=10000,
    random_state=0
)

# Train Model
model.fit(input, output)
# Prediction
prediction = model.predict(input)

print("Input Output")

for i in range(len(input)):
    print(input[i], "-->", prediction[i])