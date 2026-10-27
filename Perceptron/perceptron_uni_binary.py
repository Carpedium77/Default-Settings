
import numpy as np

n = int(input("Number of inputs: "))
m = int(input("Number of samples: "))
X = []
Y = []

for i in range(m):
    X.append(list(map(int, input("Enter input: ").split())))
    Y.append(int(input("Enter target (0/1): ")))

w = np.zeros(n)
lr = 0.1
bias = 0

def activation(net):
    return 1 if net >= 0 else 0

for epoch in range(100):
    total_error = 0

    for i in range(m):
        net = np.dot(X[i], w) + bias
        y = activation(net)
        error = Y[i] - y

        w = w + lr * error * X[i]
        bias = bias + lr * error
        total_error += abs(error)

    print("Epoch:", epoch + 1, "Error:", total_error)
    if total_error == 0:
        break

print("\nFinal Predictions:")
for i in range(m):
    net = np.dot(X[i], w) + bias
    y = activation(net)
    print("Input", X[i], "Target", Y[i], "Output", y)
