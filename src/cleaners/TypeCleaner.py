import pandas as pd
from filters.Filter import Filter 

class TypeCleaner(Filter):
	
	
	def applyFilter(self, dataFrame:pd.DataFrame):
		# This one's pretty easy. Convert the dataFrame and set it to NaN if there is an entry that cannot be converted
		print("Casting the dataFrame to numeric...")
		dataFrame.apply(pd.to_numeric, errors='coerce')
		return dataFrame