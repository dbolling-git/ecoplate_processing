# ecoplate_processing
This script will take the output from an Absorbance 96 Plate Reader and process it after a quick trip to excel. 
It can process multiple files that are in the input folder.

## Steps Overview

I have included 15 files that you can use as example files. Ecoplate03062019.xls is the output file from the 
Absorbance 96 Plate Reader. ecoplate1.xlsx is an example of the format of file the program needs to be able to
work. ecolab.py is the script that will organize the data in a format that a human can read. 

You will need to have pandas, openpyxl, and xlrd libraries installed. You can install these by either
pip install openpyxl or conda install openpyxl in the terminal depending on which you are using. 

**Step One**
Be sure to nest the Input, Input_Processed, and Output folders inside of the folder EcoPlate. The Input, 
Input_Processed, and Output folders must be a subfolder of EcoPlate and must be on the same level together.

**Step Two**
Open the output file from the Absorbance 96 Plate Reader it will be Ecoplate(date).xls in excel. Copy the block 
of data including the numbered columns 1-12 and the 8 rows of data and paste it to new excel file in the A1
block. Save the file into the *.EcoPlate/Input folder, it is useful to save the file as the plate number and make
sure it is in .xlsx format. 


**Step Three**
Open the terminal, locate the EcoProto2.py file in the */EcoPlate folder. Type python EcoProto2.py and the program
should work automatically.
