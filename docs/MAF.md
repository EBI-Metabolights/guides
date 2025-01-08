# MAF
## MAF
When you create an assay a corresponding metabolite annotation file will add to your study. Metabolite information should include all **metabolites / unknowns / features** identified within the study. You should complete the table with as much information as possible (note you can leave smiles / InChI empty as these can be auto completed from metabolite names or database identifiers during curation). Sample names should be automatically included in the columns to the right of the table (please contact us if not or download & edit in eg. excel), in each column sample values per metabolite should be included.

The metabolite table file (m\_MTBLSxxx.tsv) should be referenced in the metabolite assignment file column of each assay. If results are cumulative of multiple assays, enter the same file for each.


### Validation Rules:


* MAF can not be empty.

* All MAF should be referenced in the assay.

* MAF file should readable.

* "database\_identifier" should be the first column.

* Columns 'database\_identifier', 'chemical\_formula', 'smiles', 'inchi' and 'metabolite\_identification' found in the correct column position.

* MS/NMR assay name can be found in the MAF.

* Sample name can be found in the MAF.

* No empty rows in the MAF.