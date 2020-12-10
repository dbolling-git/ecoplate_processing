import pandas as pd
import numpy as np 
import os

def eco_transform(file, output):
    db = pd.read_excel(file)
    de = db.rename(index = {0:'A', 1:'B', 2:'C', 3:'D', 4:'E', 5:'F', 6:'G', 7:'H'})
    
    list = ['Water', 'Pyruvic_acid_methyl_esther', 'Tween40', 'Tween80', 'alpha_cyclodextrin', 
            'Glycogen', 'D_cellobiose', 'alfa_D_Lactose', 'Beta_methyl_D_glucoside', 'D_xylose', 
            'I_Erytritol', 'D_Mannitol', 'N_acetyl_D_glucosamine', 'D_glucosaminic_acid', 'Glucose_1_phosphate', 
            'D_L_alpha_glycerol_phospate', 'D_galactonic_acid_gama_lactone', 'D_galactouronic_acid', 
            'two_hydroxy_benzoic_Acid', 'four_hydroxy_benzoic_Acid', 'Gamma_hydroxybutyric_Acid', 'Itaconic_Acid',
            'alpha_keto_butyric_acid', 'D_malic_Acid', 'L_Arginine', 'L_Asparagine', 'L_phenylalanine', 'L_serine', 
            'L_threonine', 'Glycyl_L_glutamic_Acid', 'Phenylethyl_amine', 'Putrescine']
    list_2 = ['control', 'ester', 'polymer', 'polymer', 'polymer', 'polymer', 'carbohydrate', 'carbohydrate', 
              'carbohydrate', 'carbohydrate', 'carbohydrate', 'carbohydrate', 'carbohydrate', 'carboxylic_acid', 
              'phosphorylated', 'phosphorylated', 'carboxylic_acid', 'carboxylic_acid', 'carboxylic_acid', 
              'carboxylic_acid', 'carboxylic_acid', 'carboxylic_acid', 'carboxylic_acid', 'carboxylic_acid', 
              'aminoacid', 'aminoacid', 'aminoacid', 'aminoacid', 'aminoacid', 'aminoacid', 'amine', 'amine']
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
    all_data= {'Metabolism':list_2,'Sample1':sample_list_one,'Sample2':sample_list_two,
              'Sample3':sample_list_three}
    final = pd.DataFrame(all_data,list)
    final.index.name = "Csource"
    final.to_excel(output)

path = os.getcwd()           # get current directory set it equal to path
new_path = path + '/input/' # add the /input/ to that directory
list_dir = os.listdir(new_path)

for item in list_dir: #go through the items in my list_directory and do a command
    item_split = item.split('.')
    if (item_split[1]) != 'xlsx': #pass through this item 
        pass
    else:   #otherwise
        funcpath = os.getcwd() # get the directory set it equal to funcpath
        in_path = funcpath + '/input/' # input_path is our input folders path
        out_path = funcpath + '/output/output_' #out path is our output folders path with prefix
        output_path = out_path +item #what we what to name our file
        input_path = in_path + item # our address for our input file in the input folder and file name        
       
        eco_transform(input_path,output_path)
        move_path = funcpath + "/input_processed/" + item #this is where we want the file to got
        print(item + " complete!")
        os.rename(input_path,move_path)