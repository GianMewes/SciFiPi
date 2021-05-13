import pandas as pd
import numpy as np
from sklearn import tree

from ..filters.Filter import Filter

class ImputationFilter(Filter):
	def applyFilter(self, dataFrame:pd.DataFrame):
		cols = dataFrame.columns 

		if len(cols) < 4:
			# print('DataFrame has less than 4 columns. Imputing missing values via interpolation.')
			for col in cols:
				values = dataFrame[col]

				# check if any nans exist in this column:
				if values.hasnans:
					# print('Found missing values in column '+ col)
					values.fillna(method = 'backfill', inplace = True)
					print('[Imputation-Filter] Added missing values in column '+ col + ' via backfilling.')

				dataFrame[col] = values

		else:
			# print('DataFrame has many columns. Imputing missing values via decision tree regression.')

			for col in cols: 
				values = dataFrame[col]

				# check if any nans exist in this column:
				if values.hasnans:
					# print('Found missing values in column '+ col)
					data = dataFrame

					# force conversion to numeric, else nan
					train_set = data.apply(lambda x: pd.to_numeric(x, errors='coerce')).dropna()
					train_val = train_set[col].values
					train_set = train_set.loc[:, data.columns != col]
					data = data.loc[:, data.columns != col]

					#find all indices in values that are nan and remove them from training data
					nan_indices = np.where(values.isnull())[0]

					# train decision tree regressor
					dTree = tree.DecisionTreeRegressor()

					dTree.fit(train_set, train_val)

					# infer missing values
					for i in nan_indices:
						try:
							values[i] = dTree.predict(data.iloc[i].values.reshape(1,-1))[0]
						except:
							pass 
					print('[Imputation-Filter]: Added missing values in column '+ col + ' via decision tree regression.')


				dataFrame[col] = values

				# check if any nans exist in this column:
				if values.hasnans:
					# print('Found unhandled missing values in column '+ col)
					values.fillna(method = 'backfill', inplace = True)
					print('[Imputation-Filter]: Added missing values in column '+ col + ' via backfilling.')
					dataFrame[col] = values


		return dataFrame