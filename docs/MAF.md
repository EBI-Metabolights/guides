# Metabolite Annotation File (MAF)
## MAF
When you create an assay a corresponding metabolite annotation file will add to your study. Metabolite information should include all **metabolites / unknowns / features** identified within the study. You should complete the table with as much information as possible. Sample names should be automatically included in the columns to the right of the table (please contact us if not or download & edit in e.g., Excel), in each column sample values per metabolite should be included.

The Metabolite Annotation File (m\_MTBLSxxx.tsv) should be referenced in the metabolite assignment file column of each assay. If results are cumulative of multiple assays, enter the same file for each.


### Validation Rules

* MAF can not be empty.

* All MAF should be referenced in the assay.

* MAF file should readable.

* "database\_identifier" should be the first column.

* Columns 'database\_identifier', 'chemical\_formula', 'smiles', 'inchi' and 'metabolite\_identification' found in the correct column position.

* MS/NMR assay name can be found in the MAF.

* Sample name can be found in the MAF.

* No empty rows in the MAF.

For comprehensive details on the validation rules that apply to Metabolite Annotation Files, please visit our [GitHub validation-rules docs](https://github.com/EBI-Metabolights/mtbls-validation/blob/main/docs/validation-rules/metabolite-validation-rules.md) 

## LC-MS and GC-MS MAF

| Column Name | Description | Example |
| --- | --- | --- |
| database_identifier | Stable external accession for the compound/feature.  <code>Recommended, if available</code> | (e.g., CHEBI:27389) |
| chemical_formula | Molecular formula of the identified compound.  <code>Optional</code> | (plain text, e.g., C4H9NO2) |
| smiles | SMILES string for the compound.  <code>Optional</code> | canonical if available; plain text (e.g., CC(CN)C(O)=O) |
| inchi | Full InChI string for the compound (starting with InChI=; not the InChIKey).  <code>Optional</code> | e.g., InChI=1S/C4H9NO2/c1-3(2-5)4(6)7/h3H,2,5H2,1H3,(H,6,7) |
| metabolite_identification | Human-readable metabolite name or, if unknown, your metabolites/unknowns/features as reported.  **<code>Required</code>** | e.g., 3-Aminoisobutyric acid, or Feature 001, Feature 002, Unknown1, etc. |
| mass_to_charge | Precursor/Parent/Feature m/z (numeric). Typically the molecular ion. For MS/MS or MSn provide precursor ion m/z.  **<code>Required</code>** | e.g '104' for 3-Aminoisobutyric acid in [M-H]+ mode |
| fragmentation| Fragment/Daughter/Product m/z (numeric). For MS/MS or MSn provide product ion(s).  <code>Recommended, if available</code>  (**<code>Required</code>** for MRM, Precursor Ion Scan) | e.g. for '3-Aminoisobutyric acid': 86, 87, 69, 58. |
| modifications | Chemical modifications/adducts/derivatisation noted for the feature.  <code>Recommended, if available</code> | e.g., [M+Na]+, [M+K]+, TMS-deriv., etc. |
| charge | Observed charge state for the compound/feature.  <code>Recommended, if available</code> | e.g., [M-H]+, [M-H]-, OR Positive, Negative, OR +1, -1. |
| retention_time | Chromatographic RT used for the assignment (numeric; unit as used by your pipeline).  **<code>Required</code>** | e.g., 3.15 |
| taxid | NCBI Taxonomy ID for the biological source associated with this identification (if applicable).  <code>Optional</code> | e.g., NCBI:txid9606 |
| species | Species name corresponding to taxid, aligned with your Sample sheet’s organism term.  <code>Optional</code> | e.g., Homo sapiens, Mus musculus, etc. |
| database | Name of the spectral/compound database or library used for the match (text). Field often used to report Compound ID present in secondary database.  <code>Optional</code> | e.g., PubChem Compound identifier (CID:XXXX) |
| database_version | Direct URL/URI to the external record or evidence for the identification (resolvable link).  <code>Optional</code> | e.g., https://pubchem.ncbi.nlm.nih.gov/ |
| reliability | Qualitative confidence level/category for the identification or Metabolomics Standards Initiative (MSI) level (see https://doi.org/10.1021/es5002105).  <code>Recommended, if available</code> | e.g., 'MSI:2', 'MSI:1' etc. |
| uri | Direct URL/URI to the external record or evidence for the identification (resolvable link).  <code>Optional</code> | --- |
| search_engine | Name (and optional version) of the software/tool used for the identification or match.  <code>Optional</code> | e.g., library search, MZmine, XCMS, etc.  |
| search_engine_score | Primary score reported by the search tool (numeric); specify score type in your methods/protocol.  <code>Optional</code> | --- |
| smallmolecule_abundance_sub | Aggregated abundance for the metabolite (e.g., subject/condition-level summary). If reporting per-sample values, put those in the auto-added sample columns on the right and leave this blank.  <code>Optional</code> | --- |
| smallmolecule_abundance_stdev_sub | Standard deviation corresponding to smallmolecule_abundance_sub (numeric).  <code>Optional</code> | --- |
|smallmolecule_abundance_std_error_sub | Standard error corresponding to smallmolecule_abundance_sub (numeric).  <code>Optional</code> | --- |
| SampleName1 | Quantification value (e.g. concentration, AUC, etc.).  <code>Recommended, if available</code> | --- |
| SampleName2 | Quantification value (e.g. concentration, AUC, etc.).  <code>Recommended, if available</code> | --- |


## NMR MAF

| Column Name | Description | Example |
| --- | --- | --- |
| database_identifier | Stable external accession for the compound/feature.  <code>Recommended, if available</code> | (e.g., CHEBI:27389) |
| chemical_formula | Molecular formula of the identified compound.  <code>Optional</code> | (plain text, e.g., C4H9NO2) |
| smiles | SMILES string for the compound.  <code>Optional</code> | canonical if available; plain text (e.g., CC(CN)C(O)=O) |
| inchi | Full InChI string for the compound (starting with InChI=; not the InChIKey).  <code>Optional</code> | e.g., InChI=1S/C4H9NO2/c1-3(2-5)4(6)7/h3H,2,5H2,1H3,(H,6,7) |
| metabolite_identification | Human-readable metabolite name or, if unknown, your metabolites/unknowns/features as reported.  **<code>Required</code>** | e.g., 3-Aminoisobutyric acid, or Feature 001, Feature 002, Unknown1, etc. |
| chemical_shift | Electronic environment of nuclei relative to a reference standard like tetramethylsilene (TMS). Reported in parts per million (ppm; numerical value).  <code>Recommended, if available</code> | e.g., 4.16 |
| multiplicity|  Indicates the splitting or coupling of an NMR signal, reflecting the number of adjacent hydrogens.  <code>Recommended, if available</code> | e.g., 1-H, 2-H, 3-H, etc. Other reporting options include 'Singlet' or 's'; 'Doublet' or 'd'; 'Triplet' or 't'; 'Quartet' or 'q'; 'Multiplet' or 'm'; 'Doublet of doublets' or 'dd'; etc. 
| taxid | NCBI Taxonomy ID for the biological source associated with this identification (if applicable).  <code>Optional</code> | e.g., NCBI:txid9606 |
| species | Species name corresponding to taxid, aligned with your Sample sheet’s organism term.  <code>Optional</code> | e.g., Homo sapiens, Mus musculus, etc. |
| database | Name of the spectral/compound database or library used for the match (text). Field often used to report Compound ID present in secondary database.  <code>Optional</code> | e.g., PubChem Compound identifier (CID:XXXX) |
| database_version | Direct URL/URI to the external record or evidence for the identification (resolvable link).  <code>Optional</code> | e.g., https://pubchem.ncbi.nlm.nih.gov/ |
| reliability | Qualitative confidence level/category for the identification or Metabolomics Standards Initiative (MSI) level  (see https://doi.org/10.1021/es5002105).  <code>Recommended, if available</code> | e.g., 'MSI:2', 'MSI:1' etc. |
| uri | Direct URL/URI to the external record or evidence for the identification (resolvable link).  <code>Optional</code> | --- |
| search_engine | Name (and optional version) of the software/tool used for the identification or match.  <code>Optional</code> | e.g., library search, MZmine, XCMS, etc.  |
| search_engine_score | Primary score reported by the search tool (numeric); specify score type in your methods/protocol.  <code>Optional</code> | --- |
| smallmolecule_abundance_sub | Aggregated abundance for the metabolite (e.g., subject/condition-level summary). If reporting per-sample values, put those in the auto-added sample columns on the right and leave this blank.  <code>Optional</code> | --- |
| smallmolecule_abundance_stdev_sub | Standard deviation corresponding to smallmolecule_abundance_sub (numeric).  <code>Optional</code> | --- |
|smallmolecule_abundance_std_error_sub | Standard error corresponding to smallmolecule_abundance_sub (numeric).  <code>Optional</code> | --- |
| SampleName1 | Quantification value (e.g. concentration, AUC, etc.).  <code>Recommended, if available</code> | --- |
| SampleName2 | Quantification value (e.g. concentration, AUC, etc.).  <code>Recommended, if available</code> | --- |


