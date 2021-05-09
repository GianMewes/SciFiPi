import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsRegressor

from filters.Filter import Filter

class Noise(Filter):
    def applyFilter(self, dataFrame:pd.DataFrame, columnlist):
        # check if columnlist is empty (all columns selected) or if certain columns are selected
        # if empty --> ALL dataframe columns are assigned to columnlist
        if len(columnlist) == 0:
            columnlist = dataFrame.columns
        else:
            pass

        print(dataFrame)

        # iterate through columnlist 
        for column in columnlist:
            # use a KNN ML model to reconstruct data and denoising it
            clf = KNeighborsRegressor(n_neighbors=100, weights='uniform')
            values_list = dataFrame.iloc[:,column].to_list()
            print(values_list)
            values_list = list(np.float_(values_list))
            # dataFrame.index.dropna(inplace = True)
            clf.fit(dataFrame.index.values[:, np.newaxis], values_list)
            column_new = clf.predict(dataFrame.index.values[:, np.newaxis])
            # old column is replaced by new column
            dataFrame.iloc[:,column] = column_new

        print(dataFrame)

        return dataFrame
    