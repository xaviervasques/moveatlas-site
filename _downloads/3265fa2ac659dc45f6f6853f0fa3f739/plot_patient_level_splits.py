# -*- coding: utf-8 -*-
"""
Patient-level splits: the house rule
====================================

Evaluation splits in MoveAtlas are patient-level, always: a subject never
appears on both sides of a split. This example builds 5 cross-patient
folds over the CODY hyperkinetic cohort (private tier, local records)
and verifies the folds are leak-free.
"""
import numpy as np

import moveatlas
from moveatlas.evaluations import cross_patient_folds

records, meta = moveatlas.dataset("cody_3").get_data()
print(f"{len(records)} records, {meta['subject_ns'].nunique()} subjects")

# %%
# Build the folds and check the invariant.

for i, (train, test) in enumerate(cross_patient_folds(meta, n_splits=5)):
    s_train = set(meta.iloc[train]["subject_ns"])
    s_test = set(meta.iloc[test]["subject_ns"])
    assert not (s_train & s_test), "patient leak!"
    print(f"fold {i}: {len(s_train)} train subjects, "
          f"{len(s_test)} test subjects, leak-free")

# %%
# The same primitive backs the CrossPatient evaluation (P2); CrossDataset
# generalization reuses it with dataset-level grouping.
