#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt


def ensure_output_directory(output_directory: Path) -> Path:
    output_directory.mkdir(parents=True, exist_ok=True)
    return output_directory

#asdadas
def save_random_scatter(rng: np.random.Generator, output_directory: Path) -> Path:
    num_points: int = 300
    x_values = rng.normal(0.0, 1.0, size=num_points)
    y_values = rng.normal(0.0, 1.0, size=num_points)
    colors = rng.uniform(0.0, 1.0, size=num_points)
    sizes = rng.uniform(10.0, 200.0, size=num_points)

    plt.figure(figsize=(6, 5), dpi=150)
    scatter = plt.scatter(
        x_values,
        y_values,
        c=colors,
        s=sizes,
        alpha=0.65,
        cmap="viridis",
        edgecolors="black",
        linewidths=0.2,
    )
    plt.colorbar(scatter, label="color scale")
    plt.title("Random Scatter")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.tight_layout()

    output_path = output_directory / "scatter.png"
    plt.savefig(output_path)
    plt.close()
    return output_path


def save_random_histogram(rng: np.random.Generator, output_directory: Path) -> Path:
    data = rng.normal(0.0, 1.0, size=1000)

    plt.figure(figsize=(6, 4), dpi=150)
    plt.hist(data, bins=30, color="steelblue", alpha=0.85, edgecolor="white")
    plt.title("Random Normal Histogram")
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.tight_layout()

    output_path = output_directory / "histogram.png"
    plt.savefig(output_path)
    plt.close()
    return output_path


def main() -> None:
    output_directory = ensure_output_directory(Path(__file__).resolve().parent / "plots")
    rng = np.random.default_rng()
    scatter_path = save_random_scatter(rng, output_directory)
    histogram_path = save_random_histogram(rng, output_directory)
    print("Saved:")
    print(f"- {scatter_path}")
    print(f"- {histogram_path}")


if __name__ == "__main__":
    main()


