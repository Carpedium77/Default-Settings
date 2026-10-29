
import matplotlib.pyplot as plt
from matplotlib.patches import RegularPolygon
import numpy as np

N = int(input("Enter Cluster Size (N): "))
R = float(input("Enter Cell Radius (R): "))

D = R * np.sqrt(3 * N)
labels = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]

def hex_to_xy(q, r):
    x = np.sqrt(3) * R * (q + r / 2)
    y = 1.5 * R * r
    return x, y

fig, ax = plt.subplots(figsize=(8, 8))
radius = 2
A_cells = []

for q in range(-radius, radius + 1):
    for r in range(-radius, radius + 1):
        x, y = hex_to_xy(q, r)
        label = labels[(q + 3 * r) % N]

        if label == "A":
            A_cells.append((x, y))

        hexagon = RegularPolygon(
            (x, y),
            numVertices=6,
            radius=R,
            orientation=0,
            edgecolor="black",
            facecolor="lightblue"
        )

        ax.add_patch(hexagon)
        ax.text(x, y, label, ha="center",
                va="center", fontsize=10)

cx, cy = A_cells[0]

for x, y in A_cells[1:]:
    dist = np.sqrt((x - cx) ** 2 + (y - cy) ** 2)

    if abs(dist - D) < 0.3 * R:
        ax.plot([cx, x], [cy, y], "r--", linewidth=2)
        ax.text((cx + x) / 2, (cy + y) / 2,
                f"D={dist:.2f}", color="red")
        break

plt.title(f"Frequency Reuse\nCluster Size N = {N}, Radius = {R}")
ax.set_aspect("equal")
ax.axis("off")
plt.show()
