# ecoplate_processing
This script will take the output from an Absorbance 96 Plate Reader and process it after a quick trip to excel. 

## Steps Overview

I have included two files that you can use as example files. Ecoplate03062019.xls is the output file from the 
Absorbance 96 Plate Reader. ecoplate1.xlsx is an example of the format of file the program needs to be able to
work. ecolab.py is the script that will organize the data in a format that a human can read. 

You will need to have pandas, openpyxl, and xlrd libraries installed. You can install these by either
pip install openpyxl or conda install openpyxl in the terminal depending on which you are using. 

**Step One**
Open the output file from the Absorbance 96 Plate Reader it will be Ecoplate(date).xls in excel. Copy the block
of data starting on C19 and ending on N26. 

**Step Two**
Open a new excel file and paste the data onto the A2 cell. The data should extend to L9. You will fill A1-L1 with
the letters of the alphabet capitilized. You can refer to my example ecoplate1.xlxs for reference.

**Step Three**
Place the new excel file into the same directory as the the ecolab.py file. Point to that directoy in the terminal
and type python ecolab.py (your new excel file with .xlsx). The program will ask you what you would like to name 
your new file and that file will be saved in the same directory.
