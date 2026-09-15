# -*- coding: utf-8 -*-
"""
Silhouettes: the privacy-preserving face of clinical video
==========================================================

64-point body contours from the KOA-PD-NM gait dataset. A contour keeps
the movement and drops the identity, which is exactly why silhouettes
are the publishable form of patient video in MoveAtlas (see the privacy
gate). Detection masks say honestly when the walker was not found.
"""

import matplotlib.pyplot as plt
import numpy as np

from moveatlas.datasets.base import load_record
from moveatlas.store import LocalStore

store = LocalStore()
recs = load_record(store.path(
    "datasets/pose/koa_pd_nm/processed/canonical_silhouette.pkl"))
rec = recs[0]
print(rec["subject_ns"], rec["cohort"], rec["severity"],
      rec["contour"].shape, f"{rec['fps']} fps",
      f"detected {rec['detect_mask'].mean():.0%}")

# %%
# Eight mid-sequence contours, walking left to right.

good = np.where(rec["detect_mask"])[0]
mid = good[len(good) // 4: 3 * len(good) // 4]
frames = mid[np.linspace(0, len(mid) - 1, 8).astype(int)]
fig, ax = plt.subplots(figsize=(9, 2.6))
for i, fr in enumerate(frames):
    c = rec["contour"][fr].copy()
    ax.fill(c[:, 0] + i * 1.4, c[:, 1], alpha=0.9, lw=0)
ax.set_aspect("equal")
ax.axis("off")
ax.set_title(f"{rec['cohort']} ({rec['severity']}) - one gait sequence")
fig.tight_layout()
