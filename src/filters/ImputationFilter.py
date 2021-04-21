import pandas as pd
import numpy as np
from sklearn import tree

from filters.Filter import Filter

class ImputationFilter(Filter):
	def applyFilter(self, dataFrame:pd.DataFrame):
		cols = dataFrame.columns

		dataframe = dataFrame.fillna(np.nan)

		print('Imputation of missing values...')

		if len(cols) < 4:
			print('DataFrame has less than 4 columns. Imputing missing values via interpolation.')
			for col in cols:
				try:
					values = dataFrame[col]
					values = pd.to_numeric(values)
					values = values.fillna(np.nan)
					# check if any nans exist in this column:
					if values.hasnans:
						print('Found missing values in column '+ col)
						values = values.interpolate()
						print('Added missing values in column '+ col + ' via interpolation.')

					dataFrame[col] = values
				except: ValueError

		else:
			print('DataFrame has many columns. Imputing missing values via decision tree regression.')
			#TODO: remove [1:], once input is proper dataframe
			for col in cols[1:]: 
				values = dataFrame[col]

				#TODO: remove, once input is proper dataframe
				try:
					values.replace('Connectivity Error!', value = np.nan, inplace=True)
				except: ValueError

				try:
					#TODO: remove, once input is proper dataframe
					values = pd.to_numeric(values)
					
					#TODO: remove, once input is proper dataframe
					values = values.fillna(np.nan)

					# check if any nans exist in this column:
					if values.hasnans:
						print('Found missing values in column '+ col)
						data = dataFrame

						#TODO: remove, once input is proper dataframe
						try:
							data = data.drop('TIMESTAMP', axis = 1)
						except: ValueError

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
							values[i] = dTree.predict(data.iloc[i].values.reshape(1,-1))
						print('Added missing values in column '+ col + ' via decision tree regression.')

					dataFrame[col] = values
				
				except: ValueError

		return dataFrame