MoveAtlas
=========

**The open atlas of movement data, human and animal**: one API over the
movement-disorders corpus. |n_catalogued| catalogued datasets
(|n_human| human, |n_animal| animal); |n_records| harmonized records
from |n_subjects| subjects and |n_hours| hours of signal across six
canonical families (pose, IMU, EMG, force plates, silhouette, EEG),
with patient-level evaluation splits. Of those records, |n_served_records|
from |n_served_datasets| datasets are served from MoveAtlas's own
|n_published_records| Zenodo records and download in one call; the
|n_recipe_records| from |n_recipe_datasets| datasets whose licences
forbid redistribution are reproducible from their original host with the
documented recipe, and |n_unstaged_records| from |n_unstaged_datasets|
redistributable datasets await their record. Every count on this page is
computed from the registry at build time.
MoveAtlas exists because the **hyperkinetic disorders - dystonia,
tremor, chorea, myoclonus, tics, athetosis, ballismus, stereotypies -**
are where open data is scarcest: the atlas documents every gap it could
not fill (the coverage matrix's empty cells are findings, not
omissions), and contributes its own: **CODY**, the public
dystonia-centred release of adult and pediatric hyperkinetic pose data
(`10.5281/zenodo.22232609 <https://doi.org/10.5281/zenodo.22232609>`_).
The catalogue reaches further than the six harmonized families: invasive
LFP and ECoG recordings, structural MRI cohorts, brain histology and
transcriptomics, genetics panels and clinical scales are catalogued with
their own cards and access routes, and a translational animal lane
(mouse, rat and macaque models of the same disorders) is kept strictly
separate from the human clinical axes.

.. raw:: html

   <div class="ma-chips">
   <span class="ma-chip">v0.1.0.dev0</span>
   <span class="ma-chip">BSD-3-Clause</span>
   <span class="ma-chip">PyPI name reserved</span>
   <span class="ma-chip">local pre-launch build</span>
   <a class="ma-chip" href="whats_new.html"><b>What's new</b></a>
   </div>

.. grid:: 2
   :gutter: 2

   .. grid-item::

      .. button-ref:: dataset_summary
         :color: primary
         :expand:

         Browse the atlas

   .. grid-item::

      .. button-ref:: submit_dataset
         :color: secondary
         :outline:
         :expand:

         Contribute a dataset

.. raw:: html
   :file: _generated/hero_stats.html

.. image:: _static/catalogue_glance.png
   :alt: The full catalogue at a glance, 12 modality lanes and the harmonized hours per family
   :width: 100%
   :class: only-light

.. image:: _static/catalogue_glance_dark.png
   :alt: The full catalogue at a glance, 12 modality lanes and the harmonized hours per family
   :width: 100%
   :class: only-dark

Six harmonized families
-----------------------

Every thumbnail below is a real record from the corpus; every count is
measured from the canonical manifests at build time.

.. raw:: html
   :file: _generated/family_cards.html

.. image:: _static/sample_pose.png
   :alt: Real canonical gait skeletons, able-bodied and stroke, from the Van Criekinge dataset
   :width: 100%
   :class: only-light

.. image:: _static/sample_pose_dark.png
   :alt: Real canonical gait skeletons, able-bodied and stroke, from the Van Criekinge dataset
   :width: 100%
   :class: only-dark

Find your path
--------------

.. grid:: 2 2 4 4
   :gutter: 2

   .. grid-item-card:: Browse
      :link: dataset_summary
      :link-type: doc

      The master table of all |n_catalogued| datasets, human and animal
      lanes side by side: filter, sort, export; access and harmonization
      badges on every row.

   .. grid-item-card:: Learn
      :link: modalities
      :link-type: doc

      The modalities tour: what each family looks like on real records,
      and the six lanes beyond the signal. The :doc:`taxonomy` page
      defines every cell code and its HPO terms.

   .. grid-item-card:: Analyze
      :link: auto_examples/index
      :link-type: doc

      executed examples over real corpus data; every page downloads
      as ``.py`` and ``.ipynb``. Full :doc:`API reference <api>`.

   .. grid-item-card:: Contribute
      :link: submit_dataset
      :link-type: doc

      Signal a dataset, host it openly, write the adapter, pass the two
      gates: license triage and privacy.

Quickstart
----------

.. code-block:: python

   import moveatlas

   moveatlas.list_datasets()                    # the catalogue + access cases
   ds = moveatlas.dataset("gait120")            # a hosted multimodal dataset
   records, meta = ds.get_data(modality="emg")  # downloaded from its record, verified

   moveatlas.fetch("fog_star")                  # a recipe: fetched at the origin,
   moveatlas.ingest("fog_star")                 # harmonized on your machine

Two ways in, one catalogue: browse the data first (:doc:`statistics`,
:doc:`dataset_summary`, :doc:`modalities`, :doc:`taxonomy`, the
:doc:`dataset pages <datasets/index>`), or start from the library
(:doc:`getting_started` in three lines, then the :doc:`user_guide` for
one complete walk per access case, the record format and the
subject-level evaluations).

The problem
-----------

Movement-disorders data is scattered across dozens of repositories in
incompatible formats, behind licenses ranging from CC0 to retracted
tombstones; published pipelines are validated on single small cohorts
with splits that leak patients between train and test. Nobody can say
what generalizes. Our access-barriers casebook documents, with evidence,
how often "open" data is not practically open.

The solution
------------

One package, one canonical contract per modality, fixed patient-level
evaluations, and honest access machinery: hosted datasets download in one
call from MoveAtlas's own verified records; recipe datasets fetch from their
original home through our ingestion code; barriers raise their documented
route instead of pretending. Benchmarks combine evidence across datasets
by meta-analysis.

Data provenance
---------------

Every dataset keeps its identity, license text and citation trail; the
catalogue draws from the open repositories of the field.

.. raw:: html
   :file: _generated/provenance.html

Core team
---------

MoveAtlas is founded and owned by Xavier Vasques. Contributions are
credited in the release notes and, from the public launch, in the
versioned software citation.

Contributors
------------

The contributor mosaic appears here at the public launch; until then,
see the release notes for per-change credit.

Acknowledgements
----------------

MoveAtlas's design gratefully follows `MOABB
<https://moabb.neurotechx.com>`_ (NeuroTechX), the reproducibility
framework for BCI, as its explicit model.

Citation
--------

The MoveAtlas resource paper is in preparation. Until then, cite the
individual dataset papers listed on each data card; see :doc:`cite`.

Disclaimer and contact
----------------------

MoveAtlas is an open-science project that will evolve with the needs of
its community. Nothing on this site redistributes data whose licence
forbids it; access cases are enforced in the package itself. Contact:
the repository's issue tracker (public launch) or the owner directly
until then.

.. toctree::
   :hidden:

   statistics
   dataset_summary
   modalities
   taxonomy
   datasets/index
   getting_started
   user_guide
   troubleshooting
   auto_examples/index
   submit_dataset
   api
   cite
   whats_new
