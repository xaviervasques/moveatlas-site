Submit a new dataset
====================

MoveAtlas grows the way MOABB grew: the unit of contribution is one small
adapter file, and a contributed dataset instantly gains a data card, a
place in every applicable table, and (from P2) benchmark coverage.

The flow
--------

1. **Signal the dataset** on the pinned wishlist issue of the repository
   (one line: name, link, licence if known). We are open to any
   suggestion.
2. **Host the data openly.** If you own the data, deposit it on Zenodo,
   Hugging Face or Kaggle first, under an explicit licence (CC0 or
   CC BY 4.0 preferred). An openly hosted dataset enters the hosted tier
   and becomes one-click; anything else enters as a recipe or a pointer.
3. **Write the adapter**: subclass ``moveatlas.datasets.base.BaseDataset``,
   declare the metadata (subjects, modalities, licence, citation, DOI,
   taxonomy cells) and implement ``_load`` mapping your format to the
   canonical contract of its family (``configs/canonical_*.yaml``).
   The four pilot adapters in ``moveatlas/datasets/`` are the templates.
4. **Open the pull request** with the adapter, the data card, and a
   passing smoke test.

Two MoveAtlas-specific gates, before any merge
----------------------------------------------

- **Licence triage**: the licence evidence (verbatim source, URL, date
  checked) lands on the data card. "Probably fine" is not a licence.
- **The privacy gate**: no patient-identifiable imagery, ever, in
  anything hosted or rendered. Derived series (keypoints, masks without
  visible patients, tabular features) are the publishable forms.

What we never do
----------------

We never mirror data whose licence forbids redistribution, never bypass
an access control, and never host a retracted deposit. Datasets in those
situations are documented as pointers or barriers, with their access
route on the card.
