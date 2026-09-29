"""Bar chart of the 8 planets and their distances from the Sun."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
dist_au = [0.39, 0.72, 1.00, 1.52, 5.20, 9.58, 19.2, 30.1]          # astronomical units
dist_km = [57.9, 108.2, 149.6, 227.9, 778.6, 1433.5, 2872.5, 4495.1]  # millions of km

fig, ax = plt.subplots(figsize=(11, 6))
bars = ax.bar(planets, dist_au,
              color=["#b0b0b0", "#e8c47a", "#4a90d9", "#d96a4a",
                     "#d9a84a", "#e0c98f", "#7ac8c8", "#4a6ad9"])
for b, au, km in zip(bars, dist_au, dist_km):
    ax.text(b.get_x() + b.get_width() / 2, b.get_height() + 0.4,
            f"{au} AU\n({km}M km)", ha="center", fontsize=9)
ax.set_title("Distance of the 8 Planets from the Sun", fontsize=15)
ax.set_ylabel("Distance (AU)")
ax.set_ylim(0, 35)
ax.grid(axis="y", alpha=0.3)
plt.tight_layout()
plt.savefig("planets.png", dpi=150)
print("saved planets.png")
