
n = int(input("Number of inputs: "))
X = []
T = []
for i in range(n):
    row = list(map(float, input("Input " + str(i + 1) + " (x1 x2 class): ").split()))
    X.append(row[:-1])
    T.append(int(row[-1]))

m = int(input("Number of neurons: "))
W = []
C = []
for i in range(m):
    row = list(map(float, input("Neuron " + str(i) + " (w1 w2 class): ").split()))
    W.append(row[:-1])
    C.append(int(row[-1]))

alpha = float(input("Learning rate: "))
decay = float(input("Learning rate multiplier after each epoch (0.5 halves it, 1 keeps it): "))
epochs = int(input("Epochs: "))


def distance(x, w):
    d = 0
    for i in range(len(x)):
        d += (x[i] - w[i]) ** 2
    return d


for epoch in range(1, epochs + 1):
    for x, t in zip(X, T):
        dist = []
        for w in W:
            dist.append(distance(x, w))
        winner = dist.index(min(dist))
        for i in range(len(x)):
            if C[winner] == t:
                W[winner][i] = W[winner][i] + alpha * (x[i] - W[winner][i])
            else:
                W[winner][i] = W[winner][i] - alpha * (x[i] - W[winner][i])
    alpha = alpha * decay
    print("Epoch", epoch, "W =", [[round(v, 2) for v in w] for w in W])

print("Final W =", [[round(v, 2) for v in w] for w in W])
for x in X:
    dist = [distance(x, w) for w in W]
    print(x, "-> class", C[dist.index(min(dist))])