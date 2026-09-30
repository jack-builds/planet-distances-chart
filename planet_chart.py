#!/usr/bin/env python3
"""Bar chart of the 8 planets and their average distances from the Sun."""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
dist_mkm = [57.9, 108.2, 149.6, 227.9, 778.6, 1433.5, 2872.5, 4495.1]  # million km

fig, ax = plt.subplots(figsize=(11, 6))
colors = ["#b8a99a", "#e8c07a", "#4f9dd9", "#d9663f", "#d9a45b", "#e0c98f", "#8fd4d9", "#5f7fd9"]
bars = ax.bar(planets, dist_mkm, color=colors, edgecolor="black", linewidth=0.6)

for bar, d in zip(bars, dist_mkm):
    ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 60,
            f"{d:,.1f}", ha="center", va="bottom", fontsize=10, fontweight="bold")

ax.set_title("Distance of the 8 Planets from the Sun", fontsize=14, fontweight="bold", pad=14)
ax.set_ylabel("Average distance (million km)", fontsize=11)
ax.set_ylim(0, 5050)
ax.grid(axis="y", linestyle="--", alpha=0.4)
ax.set_axisbelow(True)

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "planets.png")
fig.tight_layout()
fig.savefig(out, dpi=150)
print("Saved:", out)
