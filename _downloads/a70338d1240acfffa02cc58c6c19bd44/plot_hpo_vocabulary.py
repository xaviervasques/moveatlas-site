# -*- coding: utf-8 -*-
"""
The label vocabulary: HPO movement terms mapped to the taxonomy
===============================================================

MoveAtlas anchors its labels to the Human Phenotype Ontology: every
movement-abnormality term under HP:0100022, with its depth, parents and
the taxonomy cells it maps to. This is the vocabulary of rule R2 (weak
supervision) and it is data anyone can browse.
"""
import re

import matplotlib.pyplot as plt
import pandas as pd

from moveatlas.store import LocalStore

hpo = pd.read_csv(LocalStore().path("docs/hpo_movement_terms.csv"))
print(f"{len(hpo)} movement terms under HP:0100022")
print(hpo.head(8)[["hpo_id", "name",
                   "depth_under_HP0100022"]].to_string(index=False))

# %%
# Depth structure of the movement subtree.

fig, ax = plt.subplots(figsize=(6.5, 2.8))
hpo["depth_under_HP0100022"].value_counts().sort_index().plot.bar(
    ax=ax, width=0.6)
ax.set_xlabel("depth under 'Abnormality of movement'")
ax.set_ylabel("terms")
ax.set_title("The HPO movement subtree by depth", loc="left", fontsize=9)
plt.setp(ax.get_xticklabels(), rotation=0)
fig.tight_layout()

# %%
# Terms already anchored to taxonomy cells (the 13 anchors verified at
# ingestion), and how many descendants each cell inherits.

cellcol = [c for c in hpo.columns if c.endswith("_cells")][0]
anchored = hpo[hpo[cellcol].notna() & (hpo[cellcol] != "")]
counts = {}
for cells in anchored[cellcol]:
    for c in re.findall(r"[A-E]\d+", str(cells)):
        counts[c] = counts.get(c, 0) + 1
ser = pd.Series(counts).sort_values(ascending=False)
fig, ax = plt.subplots(figsize=(6.5, 2.8))
ser.plot.bar(ax=ax, width=0.6)
ax.set_ylabel("HPO terms mapped")
ax.set_title("Taxonomy cells by mapped HPO terms", loc="left",
             fontsize=9)
plt.setp(ax.get_xticklabels(), rotation=0)
fig.tight_layout()
print(anchored[["hpo_id", "name", cellcol]].head(10).to_string(
    index=False))
