# -*- coding: utf-8 -*-
"""
Descriptive science, ready to run: step frequency across the lifespan
=====================================================================

Two NONAN GaitPrint cohorts share one protocol (16-IMU overground
walking at 200 Hz): 35 young adults and 41 older adults. This example
computes each walker's dominant step frequency from the lower-back
vertical acceleration and compares the cohorts, the kind of one-figure
descriptive result a study starts from.
"""
import matplotlib.pyplot as plt
import numpy as np

import moveatlas

N_PER_COHORT = 8      # keep the docs build light; raise freely


def step_frequency(rec):
    """Dominant frequency of the lower-back vertical acceleration in the
    locomotor band (1.2-3.5 Hz), from the magnitude spectrum."""
    sig = rec["signal"][:, 2, 0]          # lower_back, accel axis 0
    sig = sig - sig.mean()
    n = len(sig)
    spec = np.abs(np.fft.rfft(sig * np.hanning(n)))
    freqs = np.fft.rfftfreq(n, 1.0 / rec["fps"])
    band = (freqs >= 1.2) & (freqs <= 3.5)
    return freqs[band][np.argmax(spec[band])]


results = {}
for code, label in (("nonan_gaitprint_young", "young adults"),
                    ("nonan_gaitprint", "older adults")):
    ds = moveatlas.dataset(code)
    # cheap subject discovery: the store's per-subject shard names,
    # so we never load data just to enumerate subjects
    from moveatlas.store import LocalStore
    import os
    shards = LocalStore().glob_dir(ds._reldir)
    picks = [f"{code}:{os.path.basename(p)[:-4]}"
             for p in shards[:N_PER_COHORT]]
    records, meta = ds.get_data(subjects=picks)
    freqs = []
    for subj in picks:
        recs = [r for r in records if r["subject_ns"] == subj][:3]
        freqs.append(np.mean([step_frequency(r) for r in recs]))
    results[label] = np.array(freqs)
    print(f"{label}: {len(freqs)} subjects, "
          f"median {np.median(freqs):.2f} Hz")

# %%
# One figure, one message. (With 8 subjects per side this is a demo of
# the tooling, not a finding; raise N_PER_COHORT to the full cohorts for
# the real comparison.)

fig, ax = plt.subplots(figsize=(6, 3.2))
for i, (label, v) in enumerate(results.items()):
    x = np.full(len(v), i) + np.linspace(-0.1, 0.1, len(v))
    ax.plot(x, v, "o", ms=6, alpha=0.7)
    ax.hlines(np.median(v), i - 0.2, i + 0.2, color="black", lw=2)
ax.set_xticks(range(len(results)))
ax.set_xticklabels(list(results))
ax.set_ylabel("dominant step frequency (Hz)")
ax.set_title("Overground walking, lower-back accelerometry "
             "(bar = median)")
fig.tight_layout()
