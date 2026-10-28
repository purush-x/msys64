#XOR using MLP-using backpropagation learning algo
from sklearn.neural_network import MLPClassifier
import numpy as np

# XOR Input
X = np.array([[0, 0],
              [0, 1],
              [1, 0],
              [1, 1]])

y = np.array([0, 1, 1, 0])

# Create MLP Model
model = MLPClassifier(
    hidden_layer_sizes=(2,),
    activation='logistic',
    solver='lbfgs',
    max_iter=1000,
    random_state=1
)

# Train Model
model.fit(X, y)

# Prediction
prediction = model.predict(X)

print("Input Output")
for i in range(len(X)):
    print(X[i], "-->", prediction[i])