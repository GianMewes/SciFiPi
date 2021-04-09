import os
import pandas as pd
import json

def save_data(data, clean_path, filepath):
    '''Saves a dataframe inside the clean_path dicectory. 
    Preserves the filename.'''

    filename = os.path.basename(filepath)

    path = os.path.join(clean_path, filename)

    data.to_csv(path, index = False)

    print('Data successfully saved.')

def save_metadata(data, clean_path, filepath):
    '''Saves metadata as json inside the clean_path directory. 
    Preserves the filename and appends '_metadata.json' '''

    # create filename for metadata file
    filename = os.path.basename(filepath).split('.')[0] + '_metadata.json'

    # create path to save metadata file
    path = os.path.join(clean_path, filename)

    # write metadata file to path
    json_file = open(path, "w")
    json_file.write(json.dumps(data))
    json_file.close()
    print('Metadata successfully saved.')


