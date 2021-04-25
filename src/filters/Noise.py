import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsRegressor

from filters.Filter import Filter

class Noise(Filter):
    def applyFilter(self, dataFrame:pd.DataFrame, columnlist):
        # notes:
        # techniques that could be used: Filters, Fast-Fourier-Tranformation, PCA, Signal-to-Noise-Ratio, 
        # differentiate betweeen: normal data, noise (weak outliers) and anomalies (strong outliers)
        # one should be able to only filter specific columns

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
            clf.fit(dataFrame.index.values[:, np.newaxis], dataFrame.iloc[:,column])
            column_new = clf.predict(dataFrame.index.values[:, np.newaxis])
            # old column is replaced by new column
            dataFrame[column] = column_new

        return dataFrame
    