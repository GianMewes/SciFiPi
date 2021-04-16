import pandas as pd
import numpy as np
from sklearn.svm import OneClassSVM

from filters.Filter import Filter

class UnitFilter(Filter):
	def applyFilter(self, dataFrame:pd.DataFrame):
		# print("UnitValueFilter. DataFrame: " + str(dataFrame))

		pressure_values = dataFrame.loc[:,'PT102/OUT.CV']

		pressure_values = pd.to_numeric(pressure_values)

		# calculate change factor between two timestamps
		change_factor = []
		change_factor.append(0)
		for k in range(1, len(pressure_values)):
			change_factor.append(pressure_values[k]/pressure_values[k-1])

		multiplier = [round(x, 2) if x < 1 else round(x, 1) for x in change_factor]
		multiplier_low = [i for i,x in enumerate(multiplier) if x==0.1]
		multiplier_high = [i for i,x in enumerate(multiplier) if x==10]

		for i in range(min(len(multiplier_high), len(multiplier_high))):
			if multiplier_low[i] < multiplier_high[i]:
				for n in range(multiplier_low[i], multiplier_high[i]):
					pressure_values[n] = pressure_values[n] * 10
			elif multiplier_low[i] > multiplier_high[i]:
				for n in range(multiplier_high[i], multiplier_low[i]):
					pressure_values[n] = pressure_values[n] / 10

		dataFrame['PT102/OUT.CV'] = pressure_values

		return dataFrame