# MoSeq pharmacobehavioral space (~700 dosed mice, Wiltschko 2020)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "MoSeq pharmacobehavioral space (~700 dosed mice, Wiltschko 2020)",
 "description": "MoSeq pharmacobehavioral space (~700 dosed mice, Wiltschko 2020). MoveAtlas animal family. licence CC BY 4.0.",
 "identifier": "https://zenodo.org/records/3951698",
 "license": "https://creativecommons.org/licenses/by/4.0/",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "animal"
 ],
 "url": "https://zenodo.org/records/3951698",
 "isAccessibleForFree": true,
 "measurementTechnique": "animal",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 }
}
</script>
```

<span class="ma-fam ma-animal">animal</span>&nbsp; <span class="ma-badge ma-catalogued">catalogued</span>&nbsp; <span class="ma-badge ma-recipe">recipe</span>&nbsp; <code>moseq_pharmacobehavior</code>

| | |
|---|---|
| **Taxonomy cells** | animal: drug-induced hypokinesia/catalepsy through stimulant stereotypies - both poles of the atlas as pharmacological analogs |
| **Subjects** | ~700 |
| **Status** | acquired (2026-09-01) |
| **License** | CC BY 4.0 (Zenodo, verified 2026-09-01) |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("moseq_pharmacobehavior")
ds.info   # recipe: get_data() explains the route
```

## License and access

- **License**: CC BY 4.0 (Zenodo, verified 2026-09-01)
- **Redistribution**: yes
- **Access route**: Zenodo direct download (record 3951698)
- **Source**: <https://zenodo.org/records/3951698>

## Data card

The dataset's card, factual lines; the full card with its verification dates, download journal and processing notes is in the repository.

- **dataset**: moseq_pharmacobehavior
- **family**: animal
- **MoveAtlas cells**: animal: drug-induced hypokinesia/catalepsy through stimulant stereotypies - both poles of the atlas as pharmacological analogs
- **population**: ~700 mice dosed with neuro/psychoactive compounds (haloperidol, risperidone, stimulants...)
- **n_subjects**: ~700
- **signal**: depth-imaging scalars (position, velocity, height) + MoSeq syllable sequences (~3.1 GB)
- **license**: CC BY 4.0 (Zenodo, verified 2026-09-01); redistribution: yes
- **access**: Zenodo direct download (record 3951698)
- **link**: https://zenodo.org/records/3951698
