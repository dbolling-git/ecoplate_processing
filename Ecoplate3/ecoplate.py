import pandas as pd
import numpy as np 
import os

# Author: Daryl Bolling
# Date: 2020-12-18
# Email: dbolling4@protonmail.com

def check_file(csv):
    fail_path = csv
    fail_path = fail_path.split('/')
    fail_path = fail_path[-1]
    checks = 'pass'       #parasable check flag
    df = pd.read_csv(csv)     #checks to see if there sets came in with an missing items
    length_count = len(df)+1  # a simple check
    if length_count % 9 == 0:
        #print(f'DataFrame {csv} length pass') #checking the program is reading
        pass
    else:
        print(f"Items missing from dataframe in ", fail_path)
        checks = 'fail'
   
    length_df = len(df) + 1
    length_df = int(length_df)
    
    if length_df > 8:
        plates = length_df/9     
        plates = int(plates)
        plates_factor = np.arange(8, length_df, 9).tolist()
        plates_factor.pop()
          
        for item in plates_factor:
    
            if df.loc[item,'1'[0]] == 1.0: #checks for indexers 
               
                pass
               
            else:
                print(f'Row(s) missing in ', fail_path)
                checks = 'fail'
                break#checks for missing rows
                 #this is what will break the check
    
    else:
        pass
  
    #print(f'Rows in {csv} pass.') save for diagnostic
    if length_df > 8:  
        plates = length_df/9     
        plates = int(plates)
        plates_factor = np.arange(8, length_df, 9).tolist()
        plates_factor.pop()
        break_duplicate = 'no'  #checks to see if there was a duplicate
        set_of = []                        #check for redundant entries
        for item in plates_factor:
            factor1 = df.loc[item+1,'1'[0]]
            factor2 = df.loc[item+2,'1'[0]]   
            tuples = (factor1,factor2)
            set_of.append(tuples)
        set_of_set = set(set_of)    #ordering the set of tuple sets to elimnate duplicates
        if len(set_of) != len(set_of_set):
           
            print(f"You likely have a duplicate dataset, please check ", fail_path)
            checks = 'fail'
            
        else:
            #print('No duplicate sets detected.') #for dianostics
            
            pass
    
        
    else:
        pass
    
    return checks        

def eco_transform(file, output):
    df = pd.read_csv(file) #first import the csv file
    len_df = len(df)  #length of our dataframe
    comparison_list = np.arange(0, len_df, 1).tolist() #make a list from zero to the length of index
    df['index'] = comparison_list #make a new column of these values
    delete_list = np.arange(8, len_df, 9).tolist() # this will be the list of the rows to be deleted from df
    delete_list #our list for comaparison
    for item in comparison_list:   #look in our index
        if item in delete_list:    #if the value matches the delete list, 
            df.drop(item,axis=0,inplace=True) #drop it- elimates the extra column rows
    df.drop(['index'], axis=1,inplace=True) # getting rid of the old index
    length_df =len(df)
    length_df
    len_of_index = np.arange(0, length_df).tolist() #creating a new index without missing numbers
    df['new_index'] = len_of_index #new index with the data list
    df.set_index('new_index',inplace=True) #setting our current index to that column

    list = ['Water', 'Pyruvic_acid_methyl_esther', 'Tween40', 'Tween80', 'alpha_cyclodextrin', 
            'Glycogen', 'D_cellobiose', 'alfa_D_Lactose', 'Beta_methyl_D_glucoside',
            'D_xylose',  'I_Erytritol', 'D_Mannitol', 'N_acetyl_D_glucosamine', 
            'D_glucosaminic_acid', 'Glucose_1_phosphate','D_L_alpha_glycerol_phospate', 
            'D_galactonic_acid_gama_lactone', 'D_galactouronic_acid', 
            'two_hydroxy_benzoic_Acid', 'four_hydroxy_benzoic_Acid', 
            'Gamma_hydroxybutyric_Acid', 'Itaconic_Acid','alpha_keto_butyric_acid', 
            'D_malic_Acid', 'L_Arginine', 'L_Asparagine', 'L_phenylalanine', 'L_serine', 
            'L_threonine', 'Glycyl_L_glutamic_Acid', 'Phenylethyl_amine', 'Putrescine']
    namelist_plate = list + list + list #this is the length of the names for one plate
    list_2 = ['control', 'ester', 'polymer', 'polymer', 'polymer', 'polymer', 
    		  'carbohydrate', 'carbohydrate', 'carbohydrate', 'carbohydrate', 
    		  'carbohydrate', 'carbohydrate', 'carbohydrate', 'carboxylic_acid', 
              'phosphorylated', 'phosphorylated', 'carboxylic_acid', 'carboxylic_acid', 
              'carboxylic_acid', 'carboxylic_acid', 'carboxylic_acid', 
              'carboxylic_acid', 'carboxylic_acid', 'carboxylic_acid', 
              'aminoacid', 'aminoacid', 'aminoacid', 'aminoacid', 'aminoacid', 
              'aminoacid', 'amine', 'amine']
    metablist_plate = list_2 + list_2 + list_2 #this is the length of metabolism for one plate
    tot_plates = len(df)/8  #get the total number or plates for the dataframe
    total_plates = int(tot_plates)  #turn that from a float into an int so we can work with it
    transform_factor = np.arange(0, total_plates).tolist() # an important variable
    plate_no = np.arange(0, total_plates).tolist() # for our plate number list
    plates_list = transform_factor # we'll use this for generating our name for the names
    transform = []                   # this will be need to make our calculations later
    for item in transform_factor:
        transform.append(item * 8)
        final_names_list = namelist_plate    #ok we iniate the final names list
    plates_list.pop()       # pop off one value for the list we already mad
    if len(plates_list) > 0: #in case we only have one dataframe won't break program

        for item in plates_list:             #add the names for the each plate 3 times over per plate for 
            final_names_list = final_names_list + namelist_plate #the 3 samples

    else:
        pass

    final_metab_list = metablist_plate 
    if len(plates_list) > 0:

        for item in plates_list:
            final_metab_list = final_metab_list + metablist_plate #this is for the metabotabolits list 
    else:
        pass
    #Algorithm for generating the plate:
    data_list = []
    for item_2 in transform:

        c = ['1','2','3','4','5','6','7','8','9','10','11','12'] #columns
        x = 0 + item_2#row number 
        y = 0 # column number
        z = 0 
        sample_count = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,
        				25,26,27,28,29,30,31]
        for item in sample_count:                  #first data set 32 samples 
            if y < 4:

                data_list.append(df.loc[x,c[y]])
                y += 1


            elif y == 4:
                x += 1
                y = 0
                data_list.append(df.loc[x,c[y]])
                y += 1

        x = 0 + item_2
        y = 4
        for item in sample_count:
            if y < 8:
                data_list.append(df.loc[x,c[y]])
                y += 1
            elif y == 8:
                x += 1
                y = 4
                data_list.append(df.loc[x,c[y]])
                y+=1
        x = 0 + item_2
        y = 8
        for item in sample_count:    
            if y < 12:
                data_list.append(df.loc[x,c[y]])
                y += 1
            elif y == 12:
                x += 1
                y = 8
                data_list.append(df.loc[x,c[y]])
                y += 1
    logic_plate_no = []
    for item in plate_no:
        logic_plate_no.append(item + 1)# gives us a list of all our plates 
    plate_string = [str(i) for i in logic_plate_no ] #convert the numbers into strings!!
    len_plate_list = total_plates * 96  # get the total number of rows you need for plate list 
    plate_no_list = np.arange(0, len_plate_list).tolist() # an iterable list to make the column for plate no
    plate_list_data = [] # list of data for our plate count
    tick = 0 # so we are going to count to 96 and then add one to our plate value
    plate_count = 1
    act_plate_no = 0
    for item in plate_no_list:
        if tick < 96:
            plate_list_data.append(plate_count)
            tick += 1
        if tick == 96:
            tick = 0
            plate_count += 1
    ones = np.ones(32).tolist()
    data_sample = []

    for item in ones:
        data_sample.append(item)
    for item in ones:
        data_sample.append(item+1)
    for item in ones:
        data_sample.append(item+2)



    final_data_list = data_sample 
    if len(plates_list) > 0:

        for item in plates_list:
            final_data_list = final_data_list + data_sample #this is for the metabotabolits list 
    else:
        pass
    final_data_list= [int(i) for i in final_data_list]   
    all_data = {'Metabolism':final_metab_list,'Value':data_list,  
    			'SampleID':final_data_list,'Plate':plate_list_data}
    final = pd.DataFrame(all_data,final_names_list)
    final.to_csv(output)
    
path = os.getcwd()           # get current directory set it equal to path
new_path = path + '/input/' # add the /input/ to that directory
list_dir = os.listdir(new_path)

for item in list_dir: #go through the items in my list_directory and do a command
    item_split = item.split('.')
    if (item_split[1]) != 'csv': #pass through this item 
        pass
    else:   #otherwise
        funcpath = os.getcwd() # get the directory set it equal to funcpath
        in_path = funcpath + '/input/' # input_path is our input folders path
        out_path = funcpath + '/output/output_' #out path is our output folders path with prefix
        output_path = out_path +item #what we what to name our file
        input_path = in_path + item # our address for our input file in the input folder and file name        
        checked = check_file(input_path)
        if checked == 'pass':
            eco_transform(input_path,output_path)
            move_path = funcpath + "/input_processed/" + item #this is where we want the file to got
            print(item + " complete!")
            os.rename(input_path,move_path)
        else:                                  #this is where the files goes if it fails
            failed_file = item + ' failed'     #the check
            print(failed_file)
            print('\n')