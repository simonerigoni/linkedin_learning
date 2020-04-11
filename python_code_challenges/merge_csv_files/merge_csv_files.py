# Merge CSV files that can also have different columns
# python merge_csv_files.py

import pandas as pd

def merge_csv(list_input_filepath, output_filepath):
    '''
    Merge two or more CSV file

    Arguments:
        input_filepath: variable number of CSV file to merge
        output_filepath (str): output CSV file

    Returns
        None
    '''
    all_df = []

    for filepath in list_input_filepath:
        #with open(filepath, 'r') as input_file:
        #    line = input_file.readline()
        df = pd.read_csv(filepath)  
        all_df.append(df)
            
    concat_df = pd.concat(all_df, axis = 0, ignore_index = True)

    #print(concat_df)

    concat_df.to_csv(output_filepath, index = False)


if __name__ == '__main__':
    merge_csv(['class_1.csv', 'class_2.csv'], 'all_students.csv')