import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
distance_au = [0.39, 0.72, 1.00, 1.52, 5.20, 9.58, 19.2, 30.1]
distance_mkm = [57.9, 108.2, 149.6, 227.9, 778.6, 1433.5, 2872.5, 4495.1]

fig, ax = plt.subplots(figsize=(11, 6))
bars = ax.bar(planets, distance_au, color="#4C9BD6", edgecolor="#1B4F72")
for bar, au, mkm in zip(bars, distance_au, distance_mkm):
    ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.4,
            f"{au} AU\n({mkm}M km)", ha="center", va="bottom", fontsize=9)

ax.set_title("Distance of the 8 Planets from the Sun")
ax.set_xlabel("Planet")
ax.set_ylabel("Distance from Sun (AU)")
ax.set_ylim(0, max(distance_au) * 1.25)
ax.grid(axis="y", alpha=0.3)
fig.tight_layout()

out = os.path.expanduser("~/demo/planet_distances.png")
os.makedirs(os.path.dirname(out), exist_ok=True)
fig.savefig(out, dpi=150)
print(out)
