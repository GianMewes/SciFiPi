import pandas as pd

from filters.Filter import Filter

class Lag(Filter):
    def applyFilter(self, dataFrame:pd.DataFrame):
		# find lagged variables --> extremely risky, because of related variables
		# use partial autocorrelation of the data
		# df[IDENTIFIED LAG COLUMN] = df[BASE COLUMN].shift(LAG)
        