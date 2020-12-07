import pandas as pd
import numpy as np
from sys import argv


script, first = argv

db = pd.read_excel(first)

de = db.rename(columns={'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,
					'K':11,'L':12}, index ={0:'A', 1:'B', 2:'C', 3:'D', 4:'E', 5:'F', 
					6:'G', 7:'H'})
					
row_names = """
Water	control

Pyruvic_acid_methyl_esther	ester

Tween40	polymer

Tween80	polymer

alpha_cyclodextrin	polymer

Glycogen	polymer

D_cellobiose	carbohydrate

alfa_D_Lactose	carbohydrate

Beta_methyl_D_glucoside	carbohydrate

D_xylose	carbohydrate

I_Erytritol	carbohydrate

D_Mannitol	carbohydrate

N_acetyl_D_glucosamine	carbohydrate

D_glucosaminic_acid	carboxylic_acid

Glucose_1_phosphate	phosphorylated

D_L_alpha_glycerol_phospate	phosphorylated

D_galactonic_acid_gama_lactone	carboxylic_acid

D_galactouronic_acid	carboxylic_acid

two_hydroxy_benzoic_Acid	carboxylic_acid

four_hydroxy_benzoic_Acid	carboxylic_acid

Gamma_hydroxybutyric_Acid	carboxylic_acid

Itaconic_Acid	carboxylic_acid

alpha_keto_butyric_acid	carboxylic_acid

D_malic_Acid	carboxylic_acid

L_Arginine	aminoacid

L_Asparagine	aminoacid

L_phenylalanine	aminoacid

L_serine	aminoacid

L_threonine	aminoacid

Glycyl_L_glutamic_Acid	aminoacid

Phenylethyl_amine	amine

Putrescine	amine
"""
#these are the elements for my "Index" and "Metabolism" Columns

rows = row_names.split() #now I split the words into seperate items

count = 0
list = []
while count < len(rows):
    list.append(rows[count])
    count += 2
list_2 = []
count = 1
while count <len(rows):
    list_2.append(rows[count])
    count += 2
# list contains the names and list_2 contains the metabolism
sample_list_one = []
sample_list_one.append(de.loc['A',1])
sample_list_one.append(de.loc['B',1])
sample_list_one.append(de.loc['C',1])
sample_list_one.append(de.loc['D',1])
sample_list_one.append(de.loc['E',1])
sample_list_one.append(de.loc['F',1])
sample_list_one.append(de.loc['G',1])
sample_list_one.append(de.loc['H',1])
sample_list_one.append(de.loc['A',2])
sample_list_one.append(de.loc['B',2])
sample_list_one.append(de.loc['C',2])
sample_list_one.append(de.loc['D',2])
sample_list_one.append(de.loc['E',2])
sample_list_one.append(de.loc['F',2])
sample_list_one.append(de.loc['G',2])
sample_list_one.append(de.loc['H',2])
sample_list_one.append(de.loc['A',3])
sample_list_one.append(de.loc['B',3])
sample_list_one.append(de.loc['C',3])
sample_list_one.append(de.loc['D',3])
sample_list_one.append(de.loc['E',3])
sample_list_one.append(de.loc['F',3])
sample_list_one.append(de.loc['G',3])
sample_list_one.append(de.loc['H',3])
sample_list_one.append(de.loc['A',4])
sample_list_one.append(de.loc['B',4])
sample_list_one.append(de.loc['C',4])
sample_list_one.append(de.loc['D',4])
sample_list_one.append(de.loc['E',4])
sample_list_one.append(de.loc['F',4])
sample_list_one.append(de.loc['G',4])
sample_list_one.append(de.loc['H',4])

sample_list_two = []
x = 5
sample_list_two.append(de.loc['A',x])
sample_list_two.append(de.loc['B',x])
sample_list_two.append(de.loc['C',x])
sample_list_two.append(de.loc['D',x])
sample_list_two.append(de.loc['E',x])
sample_list_two.append(de.loc['F',x])
sample_list_two.append(de.loc['G',x])
sample_list_two.append(de.loc['H',x])
x = 6
sample_list_two.append(de.loc['A',x])
sample_list_two.append(de.loc['B',x])
sample_list_two.append(de.loc['C',x])
sample_list_two.append(de.loc['D',x])
sample_list_two.append(de.loc['E',x])
sample_list_two.append(de.loc['F',x])
sample_list_two.append(de.loc['G',x])
sample_list_two.append(de.loc['H',x])
x = 7
sample_list_two.append(de.loc['A',x])
sample_list_two.append(de.loc['B',x])
sample_list_two.append(de.loc['C',x])
sample_list_two.append(de.loc['D',x])
sample_list_two.append(de.loc['E',x])
sample_list_two.append(de.loc['F',x])
sample_list_two.append(de.loc['G',x])
sample_list_two.append(de.loc['H',x])
x = 8
sample_list_two.append(de.loc['A',x])
sample_list_two.append(de.loc['B',x])
sample_list_two.append(de.loc['C',x])
sample_list_two.append(de.loc['D',x])
sample_list_two.append(de.loc['E',x])
sample_list_two.append(de.loc['F',x])
sample_list_two.append(de.loc['G',x])
sample_list_two.append(de.loc['H',x])
sample_list_three = []
x = 9
sample_list_three.append(de.loc['A',x])
sample_list_three.append(de.loc['B',x])
sample_list_three.append(de.loc['C',x])
sample_list_three.append(de.loc['D',x])
sample_list_three.append(de.loc['E',x])
sample_list_three.append(de.loc['F',x])
sample_list_three.append(de.loc['G',x])
sample_list_three.append(de.loc['H',x])
x = 10
sample_list_three.append(de.loc['A',x])
sample_list_three.append(de.loc['B',x])
sample_list_three.append(de.loc['C',x])
sample_list_three.append(de.loc['D',x])
sample_list_three.append(de.loc['E',x])
sample_list_three.append(de.loc['F',x])
sample_list_three.append(de.loc['G',x])
sample_list_three.append(de.loc['H',x])
x = 11
sample_list_three.append(de.loc['A',x])
sample_list_three.append(de.loc['B',x])
sample_list_three.append(de.loc['C',x])
sample_list_three.append(de.loc['D',x])
sample_list_three.append(de.loc['E',x])
sample_list_three.append(de.loc['F',x])
sample_list_three.append(de.loc['G',x])
sample_list_three.append(de.loc['H',x])
x = 12
sample_list_three.append(de.loc['A',x])
sample_list_three.append(de.loc['B',x])
sample_list_three.append(de.loc['C',x])
sample_list_three.append(de.loc['D',x])
sample_list_three.append(de.loc['E',x])
sample_list_three.append(de.loc['F',x])
sample_list_three.append(de.loc['G',x])
sample_list_three.append(de.loc['H',x])
#getting the data from the file and placing them into seperate samples
all_data= {'Metabolism':list_2,'Sample One':sample_list_one,'Sample two':sample_list_two,
		'Sample three':sample_list_three}
#creating a dictionary for all my data sets

final = pd.DataFrame(all_data,list) #placing the elements into a dataframe

final #the dataframe

def get_filename():
    print("What would you like to name your new file? Can not include a '.'")
    file_name= input("> ")
    file_check = [char for char in file_name]
    while '.' in file_check:
        print("Error file must not contain a '.'")   
        file_name= input("> ")
        file_check = [char for char in file_name]
    else:
        return file_name

file = get_filename()
combined_name = file + ".xlsx"
print(combined_name)
final.to_excel(combined_name)
print("Succesful conversion",combined_name,"has been saved to directory!")
    
