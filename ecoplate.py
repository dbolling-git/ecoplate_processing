import pandas as pd
import argparse
import numpy as np
from verify import verify_df


def split_set(dataframe) -> dict:
    """
    Takes in dataframe of ecoplate data and creates a dictionary of
    individual 3 plate samples, must be constructed by template
    file.
    :param dataframe: dataframe made from template csv
    :return: returns a dictionary mapped to individual 3 plate samples
    """
    samples_dict = {}
    start_marker = 0
    end_marker = 8
    while end_marker <= len(dataframe):
        df = dataframe.iloc[start_marker:end_marker]
        samples_dict[start_marker] = df
        start_marker += 8
        end_marker += 8
    return samples_dict


def get_sample_data(dataframe, plate_no, map_dataframe):
    """
    Returns a dataframe of individual 3 plate samples, and maps them to
    their name and class.
    :param dataframe: the 12 column by 8 row 3 sample dataset for a sample
    :param plate_no: used to identify the specific number of plate taken
    from data
    :param map_dataframe: dataframe made from csv file that contains the
    names and classes of samples in table
    :return: a dataframe containing 3 ecoplate samples
    """
    sample_one = dataframe[['A', 'B', 'C', 'D']]
    sample_two = dataframe[['E', 'F', 'G', 'H']]
    sample_three = dataframe[['I', 'J', 'K', 'L']]
    all_samples = [sample_one, sample_two, sample_three]

    for j, sample in enumerate(all_samples):
        for rows in range(len(sample_one)):

            if rows == 0:
                df = sample.iloc[rows].transpose()

            else:
                temp = sample.iloc[rows].transpose()
                df = pd.concat([df, temp], ignore_index=True, sort=False)

        if j == 0:
            result = df
        else:
            result = pd.concat([result, df], ignore_index=True, sort=False)
    result = pd.DataFrame(result, columns=['Data'])
    result['Plate_Number'] = plate_no
    result = pd.concat([map_dataframe, result], axis=1)

    return result


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--eco_file", help="path to ecoplate file", type=str,
                        required=True)

    return parser.parse_args()


def create_normalized_data(dataframe):
    st_dict = {}
    start_index = 0
    end_index = 32
    while end_index <= len(dataframe):
        st_dict[start_index] = list(round(dataframe.iloc[start_index:end_index][
                                              'Data'] - dataframe['Data'][
            start_index], 4))
        start_index += 32
        end_index += 32
    for key in st_dict:
        if key == 0:
            st_data = st_dict[key]
        else:
            temp = st_dict[key]
            st_data = st_data + temp
    dataframe.insert(5, 'St_Data', st_data, allow_duplicates= True)
    return dataframe


if __name__ == '__main__':
    args = parse_args()
    plate_no = 1
    ecoplate_data = pd.read_csv(args.eco_file)
    if verify_df(ecoplate_data):
        map_names = pd.read_csv('Names_met_map.csv')
        results = split_set(ecoplate_data)
        for key in results.keys():
            if key == 0:
                final_result = get_sample_data(results[key], plate_no, map_names)
                replicants = list(np.ones(32)) + list(np.ones(32) * 2) + \
                             list(np.ones(32) * 3)
                final_result.insert(4, 'Replicate Number', replicants)
                final_result['Replicate Number'] = final_result['Replicate ' \
                                                                'Number'].astype(int)
                plate_no += 1
            else:
                temp = get_sample_data(results[key], plate_no, map_names)
                temp.insert(4, 'Replicate Number', replicants)
                temp['Replicate Number'] = temp['Replicate Number'].astype(int)
                final_result = pd.concat([final_result, temp], ignore_index=True,
                                         sort=False)
                plate_no += 1
        final_result = create_normalized_data(final_result)
        final_result.to_csv('final.csv', index= False)
        print('final.csv created!\n')
    else:
        print('Check copied values for errors.\n')


