import pandas as pd
import numpy as np
from sklearn.svm import OneClassSVM

from filters.Filter import Filter

class UnitFilter(Filter):
	def applyFilter(self, dataFrame:pd.DataFrame):
		print("UnitValueFilter. DataFrame: " + str(dataFrame))

		pressure_values = np.array(dataFrame.loc[:,'PT102/OUT.CV'])

		pressure_values = pressure_values.reshape(-1, 1)

		clf = OneClassSVM(gamma='auto').fit(pressure_values)
		
		pressure_outlier = clf.predict(pressure_values)

		d = np.where(pressure_outlier>0)
		print(d[0])

		print(pressure_outlier)
		# dataFrame = dataFrame.drop(['TIMESTAMP'], axis=1)
		# Do something with the dataFrame
		return dataFrame