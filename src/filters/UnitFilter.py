import pandas as pd
import numpy as np
from sklearn.svm import OneClassSVM

from filters.Filter import Filter

class UnitFilter(Filter):
	def applyFilter(self, dataFrame:pd.DataFrame):
		print("UnitValueFilter. DataFrame: " + str(dataFrame))

		pressure_values = dataFrame.loc[:,'PT102/OUT.CV']

		pressure_values = pd.to_numeric(pressure_values)

		new_pressure_values = []
		for k in range(len(pressure_values)):
			if pressure_values[k] < 0.3:
				new_pressure_values.append(pressure_values[k] * 10)
			else:
				new_pressure_values.append(pressure_values[k])
		dataFrame['PT102/OUT.CV'] = new_pressure_values

		# d = np.where(pressure_outlier>0)
		# print(d[0])

		# print(pressure_outlier)
		# dataFrame = dataFrame.drop(['TIMESTAMP'], axis=1)
		# Do something with the dataFrame
		return dataFrame