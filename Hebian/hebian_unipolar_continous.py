
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

for i in range(m):
    net = np.dot(X[i], w) + bias
    y = activation(net)

    w = w + lr * y * np.array(X[i])
    bias = bias + lr * y

print("\nFinal Weights:", w)
print("Final Bias:", bias)
print("\nFinal Predictions:")

for i in range(m):
    net = np.dot(X[i], w) + bias
    y = activation(net)
    print("Input", X[i], "Target", Y[i],
          "Output", round(y, 4))
