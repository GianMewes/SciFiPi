import pandas as pd
import numpy as np

from filters.Filter import Filter

class MatrixFilter(Filter): 
    def applyFilter(self, dataFrame:pd.DataFrame):
        # print("\n\nMatrixFilter:\n\n\n" + str(dataFrame))

        #pressure_values = dataFrame.loc[:,'PT102/OUT.CV']

        return dataFrame