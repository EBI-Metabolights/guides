# Sample
## Sample
The sample information should provide all relevant facts about each sample and any controls/standards included in the study. There is ONE sample sheet per study.

Sample metadata should include a unique sample name, organism, organism part (for controls use eg. experimental blank and solvent) and sample type (ie. control, QC, experimental sample). Further sample descriptors should be included where available by selecting +Factor to add new columns (eg. Gender, Age, Treatment).

A group of samples can be added to the sample table using **+Samples** and pasting a list or selecting to import Raw data file names if appropriate. There is also the option to add as many new rows as required with **+Rows** and edit cells individually.


### Validation Rules:


* Sample columns present in the sample file.
* "Sample collection" column completely filled in.
* No empty rows in sample file.
* Organism name should be at least 5 characters long.
* Organism cannot be 'human' or 'man', please choose the 'Homo sapiens' taxonomy term.
* Organism cannot be one of the invalid terms.

**Invalid organism term:** cat, dog, mouse, horse, flower, man, fish, leave, root, mice, steam, bacteria, value, food, matrix, mus, rat, blood, urine, plasma, hair, fur, skin, saliva, fly, unknown.



## Factors
The standard information captured in a sample sheet includes the organism and part of the organism studied. Each study will then vary in what sample information can be provided as eg. clinic samples may have gender, age and treatment information available and plant samples might have genetic variants and geological locations. This further information which helps to describe samples and to stratify the groups of interest for analysis and statistics is added to sample tables as factors.

### Add factor in the sample sheet
From the sample section select **+Add factor**. Type the factor term and use the drop-down to select the most relevant ontology term. If there is no ontology term available, type your free text and press enter to accept (then OK to add to the factor). In the second step you can add a unit if the factor information you are adding includes numerical values, if not simply select add factor in this step.

A new column will then be added to the sample sheet so you can add the relevant information for each sample.


### Delete factor column in sample sheet
To delete the factor, download the sample file and select to open with eg. Excel, then simply remove the factor related columns and re-upload the modified file. There will be 3-4 columns for each factor; Factor Value[factor\_name], Unit (if added), Term source REF, Term accession number.

***It is important not to remove the original columns or alter column headers when editing as the format is a fixed requirement.***

### View factor information

A list of all factors added to the study together with the ontology information can be found on the first tab of your study.
