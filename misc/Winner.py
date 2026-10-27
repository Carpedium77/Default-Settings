# Experiment 22: Winner Take All Learning Rule
# Idea: the neuron closest to the input is the winner, only the winner learns
# Rule: w = w + alpha * (x - w)     (winner only)

# Inputs: one line per input, e.g. 1 1
n = int(input("Number of inputs: "))
X = []
for i in range(n):
    X.append(list(map(float, input("Input " + str(i + 1) + ": ").split())))

# Neurons: one line of starting weights per neuron (numbered from 0)
m = int(input("Number of neurons: "))
W = []
for i in range(m):
    W.append(list(map(float, input("Weights of neuron " + str(i) + ": ").split())))

alpha = float(input("Learning rate: "))
decay = float(input("Learning rate multiplier after each epoch (0.5 halves it, 1 keeps it): "))
epochs = int(input("Epochs: "))


def distance(x, w):
    d = 0
    for i in range(len(x)):
        d += (x[i] - w[i]) ** 2
    return d


for epoch in range(1, epochs + 1):
    for x in X:
        dist = []
        for w in W:
            dist.append(distance(x, w))
        winner = dist.index(min(dist))
        for i in range(len(x)):
            W[winner][i] = W[winner][i] + alpha * (x[i] - W[winner][i])
    alpha = alpha * decay
    print("Epoch", epoch, "W =", [[round(v, 2) for v in w] for w in W])

print("Final W =", [[round(v, 2) for v in w] for w in W])
for x in X:
    dist = [distance(x, w) for w in W]
    print(x, "-> winner neuron", dist.index(min(dist)))