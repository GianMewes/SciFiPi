import pandas as pd
import numpy as np

from filters.Filter import Filter

class EquiDistanceFilter(Filter):
    def applyFilter(self, dataFrame:pd.DataFrame):
        # find most frequent index distance value
        # create two new columns for the index and the difference between two neighbouring index values
        dataFrame['tvalue'] = dataFrame.index
        dataFrame['index-delta'] = (dataFrame['tvalue']-dataFrame['tvalue'].shift())
        # calculate most frequenst distance value by using the mode of the column
        dataOffset = int(dataFrame['index-delta'].mode().dt.total_seconds())
        # drop the created columns
        dataFrame.drop(columns=['tvalue', 'index-delta'])
        # create the offset (as a string) in seconds for the resample() method
        resample_dataOffset = str(dataOffset) + 'S'
        # use the resample() method to create equidistance
        dataFrame = dataFrame.resample(resample_dataOffset).sum()

        return dataFrame