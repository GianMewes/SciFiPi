import pandas
import pandas as pd
import numpy as nd
import os
import glob
import py7zr

from src.read_dirty import list_dirty_files, read_file, extract_metadata
from src.save_clean import save_data, save_metadata

DIRTY_PATH = 'dirty_data'
CLEAN_PATH = 'clean_data'


if __name__ == '__main__':
    paths = list_dirty_files(DIRTY_PATH)

    for path in paths:
        data = read_file(path)

        data, metadata = extract_metadata(data)

        print('Head of the file at ' + path + ': \n ' + str(data.head))
        print('Metadata of the file at ' + path + ': \n ' + str(metadata))

        save_metadata(metadata, CLEAN_PATH, path)
        save_data(data, CLEAN_PATH, filepath = path)
