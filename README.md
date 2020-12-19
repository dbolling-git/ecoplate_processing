# ecoplate_processing
This script will take the output from an Ecoplate (Biolog) read in an Absorbance 96 Plate
Reader and will process it after a quick trip to excel. It can process multiple files that are
in the input folder. The input files can have a varying number of plates. The output is a table 
that includes carbon use, metabolic pathway in‘long format’. It is particularly recommended 
for downstream statistical applications.

For context, Ecoplate (Biolog) is a microbial function analysis tool that provides data on
physiological profiling, focusing on triplicate assays on the use of 31 carbon sources.
This method was initially developed by Garland and Mills (1991) and further addressed
by Guckert et al (1996) and Garland (1997). This code was specifically developed to
automate the processing of this data for use by the Cuellar-Gempeler lab at Humboldt
State University.

References cited:

Garland. 1997. Analysis and interpretation of community-level physiological profiles in
microbial ecology. FEMS Microbiology Ecology 24: 289-300.

Garland and Mills. 1991. Classification and characterization of heterotrophic microbial
communities on the basis of patterns of community-level sole-carbon-source utilization.
Applied and environmental microbiology 57(8): 2351-2359.

Guckert, Carr, Johnson, Hamm, Davidson and Kumagai. 1996. Community analysis by
Biolog: curve integration for statistical analysis of activated sludge microbial habitats.
Journal of microbiological methods 27: 183-197.

## Requirements
You will need to have pandas, openpyxl, and xlrd libraries installed in your machine.
You can install these by either pip install openpyxl or conda install openpyxl in the
terminal depending on which you are using. I have included a requirements.txt that you 
can install with pip install -r requirements.txt.

## Steps Overview

ecoplate.py is the script that will organize the data in a format that is easier to read. It is
also well suited for downstream applications.

I have included example files in each folder marked with an ex_ prefix. Ex_ecoplate112719.xls is the
output file from the Absorbance 96 Plate reader. You will need to extract the table data from that 
file and create a simple table with just the data to use as an input file. ex_plates15.csv is an
example of this input file format.

Before you begin each run: Be sure to delete the example files, if you do not want them mingling with
your data set. 

**Step One**
Be sure to nest the Input, Input_Processed, and Output folders inside of the folder EcoPlate. The Input, 
Input_Processed, and Output folders must be a subfolder of EcoPlate and must be on the same level together.
The ecoplate.py file must be in the Ecoplate folder and NOT in the Input, Input_processed, or Output folders.

**Step Two**
Open the output file from the Absorbance 96 Plate Reader it will be Ecoplate(date).xls in excel. Copy the block 
of data for the first plate including the numbered columns 1-12 and the 8 rows of data and paste it into a new excel 
file in the A1 block. Subsequent plates need to be copied in the next avaiable empty A cell. Ex_plates15.csv is
an example of preparing 15 plates for transformation, though you can do a varied numbered of plates. Save the file
as a .csv into the Input folder.

**Step Three**
Open the terminal, locate the ecoplate.py file in the /ecoplate folder. Type python ecoplate.py and the program
will work automatically. The program will look for a few common input errors like saving incomplete data sets or
accidently duplicating plates during input. All the files will output as thier input name prefixed by output_. The
files that process will move to the Input Processed folder. Files with errors will remain in the Input folder.

