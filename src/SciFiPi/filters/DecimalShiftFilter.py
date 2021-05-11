import pandas as pd
import numpy as np
from sklearn.svm import OneClassSVM

from .Filter import Filter

class DecimalShiftFilter(Filter):
	def applyFilter(self, dataFrame:pd.DataFrame):
		# print("UnitValueFilter. DataFrame: " + str(dataFrame))

		for col in dataFrame.columns:
			values = dataFrame.loc[:,col]

			try:
				values = pd.to_numeric(values)

				# calculate change factor between two timestamps
				change_factor = []
				change_factor.append(0)
				for k in range(1, len(values)):
					change_factor.append(values[k]/values[k-1])

				multiplier = [round(x, 2) if x < 1 else round(x, 1) for x in change_factor]
				multiplier_low = [i for i,x in enumerate(multiplier) if x==0.1]
				multiplier_high = [i for i,x in enumerate(multiplier) if x==10]

				for i in range(min(len(multiplier_high), len(multiplier_high))):
					if multiplier_low[i] < multiplier_high[i]:
						for n in range(multiplier_low[i], multiplier_high[i]):
							values[n] = values[n] * 10
						print('[Decimalshift-Filter]: Detected comma error in ' + col + '.')
					elif multiplier_low[i] > multiplier_high[i]:
						for n in range(multiplier_high[i], multiplier_low[i]):
							values[n] = values[n] / 10
						print('[Decimalshift-Filter]: Detected comma error in ' + col + '.')

				dataFrame[col] = values
				
			except Exception:
				pass

		return dataFrame