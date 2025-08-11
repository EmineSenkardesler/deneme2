#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt


def ensure_output_directory(output_directory: Path) -> Path:
    output_directory.mkdir(parents=True, exist_ok=True)
    return output_directory


def save_random_timeseries(rng: np.random.Generator, output_directory: Path) -> Path:
    num_points: int = 120
    x_index = np.arange(num_points)
    baseline = np.cumsum(rng.normal(0.0, 1.0, size=num_points))
    comparison = np.cumsum(rng.normal(0.0, 1.0, size=num_points)) + 5.0

    plt.figure(figsize=(7, 4), dpi=150)
    plt.plot(x_index, baseline, label="Series A", color="#1f77b4", linewidth=1.6)
    plt.plot(x_index, comparison, label="Series B", color="#ff7f0e", linewidth=1.6)
    plt.title("Random Cumulative Time Series")
    plt.xlabel("Step")
    plt.ylabel("Value")
    plt.legend()
    plt.grid(alpha=0.25)
    plt.tight_layout()

    output_path = output_directory / "timeseries.png"
    plt.savefig(output_path)
    plt.close()
    return output_path


def save_random_barchart(rng: np.random.Generator, output_directory: Path) -> Path:
    categories = ["A", "B", "C", "D", "E", "F"]
    values = rng.uniform(3.0, 15.0, size=len(categories))

    plt.figure(figsize=(6, 4), dpi=150)
    bars = plt.bar(categories, values, color="#2ca02c", alpha=0.85)
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, height, f"{height:.1f}", ha="center", va="bottom", fontsize=8)
    plt.title("Random Category Values")
    plt.xlabel("Category")
    plt.ylabel("Value")
    plt.tight_layout()

    output_path = output_directory / "barchart.png"
    plt.savefig(output_path)
    plt.close()
    return output_path


def main() -> None:
    output_directory = ensure_output_directory(Path(__file__).resolve().parent / "plots")
    rng = np.random.default_rng()
    ts_path = save_random_timeseries(rng, output_directory)
    bar_path = save_random_barchart(rng, output_directory)
    print("Saved:")
    print(f"- {ts_path}")
    print(f"- {bar_path}")


if __name__ == "__main__":
    main()


