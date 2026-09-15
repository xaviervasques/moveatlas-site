# -*- coding: utf-8 -*-
"""
The diseased striatum in single neurons: Q175 Huntington model vs control
=========================================================================

The atlas's animal lane holds 7,567 striatal neuron reconstructions
bulk-fetched from NeuroMorpho.Org (CC BY 4.0). One archive (Luebke)
contains a method-matched comparison: medium spiny neurons from
control mice and from the Q175 Huntington's-disease knock-in model,
reconstructed by the same lab. Chorea's cellular substrate, drawn from
real morphology files - with the honest caveat that the symptom link
is via the ANIMAL MODEL, not measured movement.
"""
import json
import os

import matplotlib.pyplot as plt
import numpy as np

from moveatlas.store import LocalStore

BLUE, ORANGE, INK2 = "#2a78d6", "#eb6834", "#52514e"

base = LocalStore().path("datasets/bio/neuromorpho_bg/raw")
neurons = json.load(open(os.path.join(base, "metadata_striatum.json"),
                         encoding="utf-8"))


def cond_of(n):
    c = n.get("experiment_condition")
    return ";".join(c) if isinstance(c, list) else str(c)


luebke = [n for n in neurons if n.get("archive") == "Luebke"]
groups = {"Control": [], "Q175 HD model": []}
for n in luebke:
    c = cond_of(n)
    if c == "Control":
        groups["Control"].append(n)
    elif c.startswith("Q175"):
        groups["Q175 HD model"].append(n)
print({k: len(v) for k, v in groups.items()},
      "medium spiny neurons (same archive, same method)")


def load_swc(n):
    p = os.path.join(base, "swc", n["archive"].lower(),
                     n["neuron_name"] + ".CNG.swc")
    if not os.path.exists(p):
        return None
    rows = []
    for line in open(p, encoding="utf-8", errors="replace"):
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        f = line.split()
        rows.append((int(f[0]), int(f[1]), float(f[2]), float(f[3]),
                     float(f[4]), float(f[5]), int(f[6])))
    return rows


def dendritic_length(rows):
    """Sum of parent-child segment lengths over dendrite points
    (SWC types 3 basal / 4 apical), micrometres."""
    pos = {r[0]: np.array(r[2:5]) for r in rows}
    total = 0.0
    for r in rows:
        if r[1] in (3, 4) and r[6] in pos:
            total += float(np.linalg.norm(pos[r[0]] - pos[r[6]]))
    return total


# %%
# Three real arbors per group (xy projection, micrometres). Same scale
# everywhere; dots mark the soma.

fig, axes = plt.subplots(2, 3, figsize=(8.5, 5.6))
for row, (label, color) in enumerate([("Control", BLUE),
                                      ("Q175 HD model", ORANGE)]):
    drawn = 0
    for n in groups[label]:
        rows = load_swc(n)
        if not rows or drawn >= 3:
            continue
        ax = axes[row, drawn]
        pos = {r[0]: (r[2], r[3]) for r in rows}
        soma = next((r for r in rows if r[1] == 1), rows[0])
        for r in rows:
            if r[6] in pos and r[1] in (3, 4):
                x0, y0 = pos[r[6]]
                x1, y1 = pos[r[0]]
                ax.plot([x0 - soma[2], x1 - soma[2]],
                        [y0 - soma[3], y1 - soma[3]],
                        lw=0.5, color=color)
        ax.scatter([0], [0], s=24, color=INK2, zorder=3)
        ax.set_aspect("equal")
        ax.set_xlim(-220, 220)
        ax.set_ylim(-220, 220)
        ax.axis("off")
        if drawn == 0:
            ax.text(-210, 195, label, fontsize=9.5, color=color,
                    fontweight="bold")
        drawn += 1
fig.suptitle("Real medium-spiny-neuron reconstructions, striatum "
             "(NeuroMorpho, Luebke archive)", fontsize=10, x=0.02,
             ha="left")
fig.tight_layout(rect=(0, 0, 1, 0.95))

# %%
# Total dendritic length per neuron, control vs Q175: a purely
# descriptive measurement over every reconstruction of both groups
# (no hypothesis test here; this page describes the data).

lengths = {}
for label in groups:
    vals = []
    for n in groups[label]:
        rows = load_swc(n)
        if rows:
            vals.append(dendritic_length(rows) / 1000.0)  # mm
    lengths[label] = np.array(vals)
    print(f"{label}: {len(vals)} reconstructions, median total "
          f"dendritic length {np.median(vals):.2f} mm")

fig, ax = plt.subplots(figsize=(6.0, 3.2))
rng = np.random.default_rng(0)
for i, (label, color) in enumerate([("Control", BLUE),
                                    ("Q175 HD model", ORANGE)]):
    v = lengths[label]
    x = i + rng.uniform(-0.13, 0.13, len(v))
    ax.scatter(x, v, s=16, color=color, alpha=0.7, zorder=3)
    ax.hlines(np.median(v), i - 0.22, i + 0.22, color=INK2, lw=2,
              zorder=4)
ax.set_xticks([0, 1])
ax.set_xticklabels(["Control", "Q175 HD model"])
ax.set_ylabel("total dendritic length (mm)")
ax.spines[["top", "right"]].set_visible(False)
ax.set_title("Per-neuron dendritic length, medians marked", loc="left",
             fontsize=10)
fig.tight_layout()
