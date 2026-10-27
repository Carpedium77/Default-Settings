
import numpy as np

n = int(input("Number of inputs: "))
m = int(input("Number of samples: "))
X = []
Y = []

for i in range(m):
    X.append(list(map(float, input("Enter input: ").split())))
    Y.append(float(input("Enter target (0 to 1): ")))

w = np.zeros(n)
lr = 0.1
bias = 0

def activation(net):
    net = np.clip(net, -500, 500)
    return 1 / (1 + np.exp(-net))

for epoch in range(1000):
    total_error = 0

    for i in range(m):
        net = np.dot(X[i], w) + bias
        y = activation(net)
        error = Y[i] - y

        delta = error * y * (1 - y)
        w = w + lr * delta * X[i]
        bias = bias + lr * delta
        total_error += abs(error)

    if (epoch + 1) % 100 == 0:
        print("Epoch:", epoch + 1, "Error:", total_error)

print("\nFinal Predictions:")
for i in range(m):
    net = np.dot(X[i], w) + bias
    y = activation(net)
    print("Input", X[i], "Target", Y[i],
          "Output", round(y, 4))
