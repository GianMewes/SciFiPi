import pandas as pd
import numpy as np
from sklearn.svm import OneClassSVM

from filters.Filter import Filter

class ImputationFilter(Filter):
	def applyFilter(self, dataFrame:pd.DataFrame):
		cols = dataFrame.columns

		dataframe = dataFrame.fillna(np.nan)
		
		corMatrix = dataFrame.corr()
		for col in cols:
			try: 
				values = dataFrame[col]
				values = pd.to_numeric(values)
				values = values.fillna(np.nan)

				# check if any nans exist in this column:
				if values.hasnans:

					values = pd.to_numeric(values)

					#perform linear interpolation for missing values
					nan_indices = np.where(values.isnull())[0]


					values = values.interpolate()

				dataFrame[col] = values
			except: ValueError

		return dataFrame