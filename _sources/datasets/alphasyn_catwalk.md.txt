# Alpha-synuclein transgenic mouse CatWalk gait (Data in Brief)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "Alpha-synuclein transgenic mouse CatWalk gait (Data in Brief)",
 "description": "Alpha-synuclein transgenic mouse CatWalk gait (Data in Brief). MoveAtlas animal family. 33 subjects. licence CC BY.",
 "identifier": "https://pmc.ncbi.nlm.nih.gov/articles/PMC5988224/",
 "license": "https://creativecommons.org/licenses/by/4.0/",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "animal"
 ],
 "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC5988224/",
 "isAccessibleForFree": true,
 "measurementTechnique": "animal",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 }
}
</script>
```

<span class="ma-fam ma-animal">animal</span>&nbsp; <span class="ma-badge ma-catalogued">catalogued</span>&nbsp; <span class="ma-badge ma-hosted">hosted</span>&nbsp; <code>alphasyn_catwalk</code>

| | |
|---|---|
| **Taxonomy cells** | animal: synucleinopathy gait analog (parkinsonian lane) |
| **Subjects** | 33 |
| **Status** | catalogued (2026-09-02) |
| **License** | CC BY (open-access article statement, verified on PMC) |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("alphasyn_catwalk")
records, meta = ds.get_data()
```

## License and access

- **License**: CC BY (open-access article statement, verified on PMC)
- **Redistribution**: yes
- **Access route**: article supplementary files (10.1016/j.dib.2017.12.067)
- **Source**: <https://pmc.ncbi.nlm.nih.gov/articles/PMC5988224/>

## Data card

The dataset's card, factual lines; the full card with its verification dates, download journal and processing notes is in the repository.

- **dataset**: alphasyn_catwalk
- **family**: animal
- **MoveAtlas cells**: animal: synucleinopathy gait analog (parkinsonian lane)
- **population**: mouse C57BL/6N: 12 WT, 13 a-syn KO, 8 human-a-syn-on-KO double transgenic, 7 months
- **n_subjects**: 33
- **signal**: CatWalk paw positions/print sizes/intensities at 100 Hz, 90 run files
- **license**: CC BY (open-access article statement, verified on PMC); redistribution: yes
- **access**: article supplementary files (10.1016/j.dib.2017.12.067)
- **link**: https://pmc.ncbi.nlm.nih.gov/articles/PMC5988224/
