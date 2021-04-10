import pandas as pd

from filters.Filter import Filter

class MissingValueFilter(Filter):
	def applyFilter(self, dataFrame:pd.DataFrame):
		print("MissingValueFilter. DataFrame: " + str(dataFrame))
		# Do something with the dataFrame
		return dataFrame