import os
import pandas as pd

def list_dirty_files(PATH):
    '''Returns list of all .csv-files in PATH.'''

    # list all files in directory
    files = os.listdir(PATH)

    # filter for .csv in file path
    files = [k for k in files if '.csv' in k]
    
    # create relative paths for files
    files = [os.path.join(PATH, k) for k in files]

    return files

def read_file(path):
    '''Takes in path of csv file and returns pandas DataFrame.'''
    
    data = pd.read_csv(path)
    print('Reading file at: '+ path)
    
    return data

def extract_metadata(data):
    '''Extract metadata from first row in dataframe. 
    Returns both the properly labeled data and the metadata.'''

    #TODO: check implementieren, ob metadaten vorhanden sind (für idempotenz)

    #TODO: extract metadata verwendet bisher hardgecodete cells um metadaten zu extrahieren
    metadata_df = data.iloc[:2,:]
    metadata = {}

    for k in range(1, len(metadata_df.columns)):
        metadata.update({metadata_df.iloc[0,k]:metadata_df.iloc[1,k]})
    metadata.update({metadata_df.columns[0]:metadata_df.columns[1]})
    metadata.update({metadata_df.columns[2]:metadata_df.columns[3]})
    metadata.update({metadata_df.columns[6]:metadata_df.columns[7]})
    print(metadata)

    # Assign proper columns values:
    data.columns = data.iloc[0,:]
    new_columns = data.iloc[0,:] 
    new_columns[0] = 'TIMESTAMP' 
    data.columns  = new_columns

    # drop unnecesary metadata columns
    data.drop([0,1], inplace = True)

    # reset index 
    data = data.reset_index(drop=True)

    return data, metadata
