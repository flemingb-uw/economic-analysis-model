"""Build a JPEG snapshot of the results (KPIs + forecast chart) using matplotlib."""

from __future__ import annotations

from io import BytesIO
from typing import Sequence

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402


def build_results_jpeg(
    kpis: Sequence[tuple[str, str]],
    heuristics: Sequence[tuple[str, str]],
    years: Sequence[int],
    sales: Sequence[float],
    profit: Sequence[float],
    title: str = "Economic Analysis - Results",
    y_label: str = "Amount",
) -> bytes:
    """Return JPEG bytes: a KPI header block above the sales / gross-profit chart."""
    fig = plt.figure(figsize=(11, 8), dpi=150, facecolor="white")
    fig.text(0.05, 0.95, title, fontsize=18, fontweight="bold", va="top")

    def _block(items: Sequence[tuple[str, str]], top: float, per_row: int) -> None:
        for i, (label, value) in enumerate(items):
            row, col = divmod(i, per_row)
            x = 0.05 + col * (0.9 / per_row)
            y = top - row * 0.09
            fig.text(x, y, label, fontsize=9, color="#555555", va="top")
            fig.text(x, y - 0.025, value, fontsize=13, fontweight="bold", va="top")

    _block(kpis, 0.89, 3)
    _block(heuristics, 0.71, 3)

    ax = fig.add_axes([0.08, 0.08, 0.88, 0.48])
    ax.plot(list(years), list(sales), marker="o", label="Combined sales")
    ax.plot(list(years), list(profit), marker="o", label="Combined gross profit")
    ax.set_xlabel("Year")
    ax.set_ylabel(y_label)
    ax.grid(alpha=0.3)
    ax.legend(loc="upper left")

    buf = BytesIO()
    fig.savefig(buf, format="jpeg", facecolor="white")
    plt.close(fig)
    return buf.getvalue()
