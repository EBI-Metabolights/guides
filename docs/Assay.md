# Assay
## Assay Overview
The assay information will describe the assay process for each control and sample in the assay and connect the sample name to both its corresponding raw data file and metabolite identification table. MULTIPLE assays can be added per study.

The assay is divided into sections each starting with a Protocol Ref column, eg. Chromatography, which describes the specifics of that part of the assay using controlled vocabulary, so every study using the same system is easily findable.

### Validation Rules:


* At least one assay file in the study.
* All the referenced assay files can be found.
* No empty column names in the assay spreadsheet.
* Template columns in the relevant assay sheet can not be removed.
* Required columns can not be empty.
* Sample names that are all referenced in assays.
* Raw or Derived files existed in MS study.
* Derived, fid or acqu files existed in NMR study.
* Are there more sample rows than assay rows.
* Assay files are referenced of the correct type.

## NMR Assay


| Column Name | Description | Example |
| --- | --- | --- |
| Sample Name | A unique identifier from a particular source (a batch of samples can have a unique Sample name as identified in the Sample table). It’s usually associated with an output spectral data filename. | pas101220\_104 |
| Protocol REF - Extraction | This is the column marking the start of data pertaining to **Extraction**. The example term MUST be present in all rows of this column. | Extraction |
| Parameter Value - Extraction Method | This how a sample was extracted from its source material. | Methanol |
| Extract Name | Leave blank if you don’t have one. |  |
| Protocol REF - NMR sample | This is the column marking the start of data pertaining to **NMR sample**. This should be present in every sample row. | NMR sample |
| Parameter Value - NMR tube type | Size and type of tube. | standard 5 mm glass NMR tube (Wilmad, LabGlass, USA) |
| Parameter Value - Solvent | Solvent used in the NMR sample. | D2O |
| Parameter Value - Sample pH | Sample pH value. | 7 |
| Parameter Value - Temperature | Sample Temperature value. | 298 |
| Unit | With relevant temperature unit. | Celsius |
| Labelled Extract Name | Leave blank if you don’t have one. |  |
| Label | If you used a chemical or biochemical marker in the sample such as a radioactive isotope of fluorescent dye which is bound to a material in order to make it detectable in an analytical instrument then enter it here. | hydrogen molecular entity |
| Protocol REF - NMR spectroscopy | This is the column marking the start of data pertaining to **NMR spectroscopy**. This should be present in every sample row. | NMR spectroscopy |
| Parameter Value - Instrument | Add the full name of the instrument you used for the NMR study in this assay, including the model number and its operating frequency | Varian Unity Inova 500 MHz spectrometer |
| Parameter Value - NMR Probe | Add a full description including the name and type of probe used.This information can be found in the ‘Acquisition Parameter Data File’, ‘acqus.txt’ found within the Bruker raw data file structure, in the field marked ‘ $PROBHD= ’. | 5 mm CPTCI 1H-13C/15N/D Z-GRD |
| Parameter Value - Number of transients | The number of scans acquired. This information can be found in the ‘Acquisition Parameter Data File’, ‘acqus.txt’ found within the Bruker raw data file structure, in the field marked ‘$NS=’. | 128 |
| Parameter Value - Pulse sequence name | The pulse sequence program used with a short description.This information can be found in the ‘Acquisition Parameter Data File’, ‘acqus.txt’ found within the Bruker raw data file structure, in the field marked ‘ $PULPROG= ’ and in the file ‘pulseprogram.txt’. | 1D 1H with presaturation (presat) |
| Parameter Value - Magnetic field strength | In Tesla (T) | 11.7 |
| Unit | Units can be added in exactly the same way as Temperature unit column. | Tesla |
| Acquisition Parameter Data File | These should contain the acquisition parameter data. In the Bruker raw data file structure, the file is called ‘acqus.txt ’. | acqus1.txt |
| Protocol REF - NMR assay | This is the column marking the start of data pertaining to **NMR assay**. This should be present in every sample row. | NMR assay |
| NMR Assay Name | This can be, but doesn’t have to be, the same as the ‘Sample Name’ | 17\_QC1 |
| Free Induction Decay Data File | This is where you should enter, either the folder or the zipped NMR raw files for each sample in this study. | 17\_QC1.zip |
| Protocol REF Data transformation | This is the column marking the start of data pertaining to **Data transformation**. This should be present in every sample row. | Data transformation |
| Normalization name | These should contain the normalization data files. | Total sum |
| Derived Spectral Data File | If your data has been transformed into one of the open-source raw data formats e.g. JCAMP , nmrML , then add them here.Please add full path of the file in the cell | 17\_QC1.nmrML  **OR if in folder structure** FILES/DERIVED\_FILES/NMR/17\_QC1.nmrML |
| Protocol REF Metabolite identification | This is the column marking the start of data pertaining to **Metabolite identification**. This should be present in every sample row. | Metabolite identification |
| Data Transformation Name | These should contain the data transformation files |  |
| Metabolite Assignment File (MAF) | A TSV file containing information about the metabolites investigated in the study. Information regarding database accession IDs , where in the spectra the metabolite is found and data pertaining to its abundance within the study samples should be in this file. | m\_mtbls1\_NMR\_spectroscopy\_v2\_maf.tsv |



 Can't find what you are looking for? Check out our [FAQ's](FAQs.md#upload-download) for most commonly asked questions and solutions.

## LC_MS Assay



| Column Name | Description | Example |
| --- | --- | --- |
| Sample Name | A unique identifier from a particular source (a batch of samples can have a unique Sample name as identified in the Sample table). It’s usually associated with an output spectral data filename. | ADG10003u\_007 |
| Protocol REF - Extraction | This is the column marking the start of data pertaining to **Extraction**. The example term MUST be present in all rows of this column. | Extraction |
| Parameter Value - Post Extraction | This column describes how the sample was extracted into a solvent prior to being injected into the analytical instrument of choice. | 400 µL water |
| Parameter Value - Derivatization | If the sample has been subjected to chemical modification prior to injection. | sylilation |
| Extract Name | Leave blank if you don’t have one. |  |
| Protocol REF - Chromatography | This is the column marking the start of data pertaining to **Chromatography**. The example term MUST be present in all rows of this column. | Chromatography |
| Parameter Value - Chromatography Instrument | Add the full name of the instrument you used for the Chromatographic part of this assay, including the manufacturer and model number as reported in manufacturer’s brochures, user manuals, or on their website. | Shimadzu Nexera UHPLC system |
| Parameter Value - Column model | Manufacturer, model number and dimensions. | HSS T3 C18 (1.8 μm, 1.0 x 100 mm; Waters) |
| Parameter Value - Column type | Type or phase of column used. | reverse phase |
| Labelled Extract Name | Leave blank if you don’t have one. |  |
| Label | If you used a chemical or biochemical marker in the sample such as a radioactive isotope of fluorescent dye which is bound to a material in order to make it detectable in an analytical instrument then enter it here. |  |
| Protocol REF - Mass spectrometry | This is the column marking the start of data pertaining to **Mass spectrometry**. The example term MUST be present in all rows of this column. | Mass spectrometry |
| Parameter Value - Scan polarity | Values should identical within each assay. If you have ‘positive’ or ‘negative’ values in the same assay then split them into separate ‘positive’ and ‘negative’ assays. | positive |
| Parameter Value - Scan m/z range | The range used in the assay. | 100-1000 |
| Parameter Value - Instrument | Add the full name of the mass spectrometer/detector you used for this LC/MS assay, including the instrument manufacturer and model number as reported in manufacturer’s brochures, user manuals, or on their website. | Bruker micrOTOF-Q II |
| Parameter Value - Ion source | Where applicable to the instrument. | ESI |
| Parameter Value - Mass analyzer | The analyser/detector of the mass fragments generated during the assay. | Triple quadrupole |
| MS Assay Name | This can be, but doesn’t have to be, the same as the ‘Sample Name’ | treated 0 min rabbit 1 |
| Raw Spectral Data File | This is where you should enter the Raw (unprocessed) MS data files (.RAW).Please add full path of the file in the cell. | FILES/Sepd340.raw **OR if in folder structure** FILES/RAW\_FILES/LC\_MS/Sepd340.raw |
| Protocol REF - Data transformation | This is the column marking the start of data pertaining to **Data transformation**. The example term MUST be present in all rows of this column. | Data transformation |
| Normalization name | these should contain the normalization data files preferably as an Excel spreadsheet file. If you don’t have these then leave the cells/column blank. | MSpos-Ex1-Col0-48h-Ag\_normalized\_data.xlsx |
| Derived Spectral Data File | If your data has been transformed into one of the open-source raw data formats e.g. mzML , CDF, or any other converted file, then add them here.Please add full path of the file in the cell. | FILES/Sepd340.mzML **OR if in folder structure** FILES/DERIVED\_FILES/LC\_MS/Sepd340.mzML |
| Protocol REF - Metabolite identification | This is the column marking the start of data pertaining to **Metabolite identification**. The example term MUST be present in all rows of this column. | Metabolite identification |
| Data Transformation Name | These should contain the data transformation files. |  |
| Metabolite Assignment File (MAF) | A TSV file containing information about the metabolites investigated in the study. Information regarding database accession IDs , where in the spectra the metabolite is found and data pertaining to its abundance within the study samples should be in this file. | m\_mtbls1\_mass\_spectrometry\_v2\_maf.tsv |


## GC_MS Assay


| Column Name | Description | Example |
| --- | --- | --- |
| Sample Name | A unique identifier from a particular source (a batch of samples can have a unique Sample name as identified in the Sample table). It’s usually associated with an output spectral data filename. | Example\_1 |
| Protocol REF - Extraction | This is the column marking the start of data pertaining to **Extraction**. The example term MUST be present in all rows of this column. | Extraction |
| Parameter Value - Post Extraction | This how the sample was extracted into a solvent prior to being injected into the analytical instrument of choice. | 2 ml ethyl acetate |
| Parameter Value - Derivatization | If the sample has been subjected to chemical modification prior to injection. | sylilation |
| Extract Name | This can be, but doesn’t have to be, the same as the ‘Sample Name’ | Example\_1 |
| Protocol REF - Chromatography | This is the column marking the start of data pertaining to **Chromatography**. The example term MUST be present in all rows of this column. | Chromatography |
| Parameter Value - Chromatography Instrument | Add the full name of the instrument used for the Chromatographic part of this assay, including the manufacturer and model number as reported in manufacturer’s brochures, user manuals or website. | Shimadzu GCMS-QP2010 Ultra |
| Parameter Value - Autosampler model | Add the full name of the autosampler used for the Chromatographic part of this assay, including the manufacturer and model number as reported in manufacturer’s brochures, user manuals or website. |  |
| Parameter Value - Column model | Manufacturer, model number and dimensions in the format shown in the examples: | Zebron ZB-AAA GC(10 m x 0.25 mm; Phenomenex) |
| Parameter Value - Column type | Polarity of column used. This information can be found on the manufacturer’s website. | low polarity **OR** medium polarity **OR** high polarity |
| Parameter Value - Guard column | Manufacturer, model number and dimensions in the format shown in the examples: |  |
| Labeled Extract Name | Leave blank if you don’t have one. |  |
| Label | If you used a chemical or biochemical marker in the sample such as a radioactive isotope of fluorescent dye which is bound to a material in order to make it detectable in an analytical instrument then enter it here. |  |
| Protocol REF - Mass spectrometry | This is the column marking the start of data pertaining to **Mass spectrometry**. The example term MUST be present in all rows of this column. | Mass spectrometry |
| Parameter Value - Scan polarity | This should be ‘positive’ for a GC/MS assay. | positive |
| Parameter Value - Scan m/z range | The range used in the assay. | 50-400 |
| Parameter Value - Instrument | Add the full name of the mass spectrometer/detector used for this GC/MS assay, including the instrument manufacturer and model number as reported in manufacturer’s brochures, user manuals or website. | Thermo Electron Trace DSQ |
| Parameter Value - Ion source | Where applicable to the instrument. | electron ionization |
| Parameter Value - Mass analyzer | The analyser/detector of the mass fragments generated during the assay. | quadrupole |
| MS Assay Name | This can be, but doesn’t have to be, the same as the ‘Sample Name’ | Example\_1 |
| Raw Spectral Data File | This is where you should enter the Raw (unprocessed) MS data files (.RAW). Please add full path of the file in the cell. | FILES/myfilename1.raw **OR if in folder structure** FILES/RAW\_FILES/myfilename1.raw |
| Protocol REF - Data transformation | This is the column marking the start of data pertaining to **Data transformation**. The example term MUST be present in all rows of this column. | Data transformation |
| Normalization name | These should contain the normalization data files preferably as an Excel spreadsheet file. If you don’t have these then leave the cells/column blank. | normalized-data.xlsx |
| Derived Spectral Data File | If your data has been transformed into one of the open-source raw data formats, e.g. mzML, or any other converted file, then add them here. Please add full path of the file in the cell. | FILES/myfilename1.mzML **OR if in folder structure** FILES/DERIVED\_FILES/myfilename1.mzML |
| Protocol REF - Metabolite identification | This is the column marking the start of data pertaining to **Metabolite identification**. The example term MUST be present in all rows of this column. | Metabolite identification |
| Data Transformation Name | These should contain the data transformation files. |  |
| Metabolite Assignment File (MAF) | A TSV file containing information about the metabolites investigated in the study. Information regarding database accession IDs, where in the spectra the metabolite is found and data pertaining to its abundance within the study samples should be in this file. | m\_MTBLS1\_GC-MS\_positive\_\_metabolite\_profiling\_v2\_maf.tsv |
