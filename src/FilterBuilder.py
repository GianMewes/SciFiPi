import pandas as pd

from filters.Filter import Filter
from filters.MissingValueFilter import MissingValueFilter
from filters.MatrixFilter import MatrixFilter
from filters.FormatData import FormatDataFrame
from filters.FixTimeZone import FixTimezone

class FilterBuilder:
	# dataFrame: pd.DataFrame

	def __init__(self, dataFrame:pd.DataFrame):
		self.dataFrame = dataFrame

		# self.dataFrame.columns = self.dataFrame.iloc[0,:]
		# new_columns = self.dataFrame.iloc[0,:] 
		# new_columns[0] = 'TIMESTAMP' 
		# self.dataFrame.columns  = new_columns

		# # drop unnecesary metadata columns
		# self.dataFrame.drop([0,1], inplace = True)

		# # reset index 
		# self.dataFrame = self.dataFrame.reset_index(drop=True)

	def filterMissingValues(self):
		filter = MissingValueFilter()
		self.dataFrame = filter.applyFilter(self.dataFrame)
		return self

	def filterMatrix(self):
		filter = MatrixFilter()
		self.dataFrame = filter.applyFilter(self.dataFrame)
		return self

	def formatData(self):
		filter = FormatDataFrame()
		self.dataFrame = filter.applyFilter(self.dataFrame)
		return self

	def fixTimeZone(self):
		filter = FixTimezone()
		self.dataFrame = filter.applyFilter(self.dataFrame)
		return self


	def getDataFrame(self):
		return self.dataFrame





# class MyFilter

# 	static myCustomFilter(obj:FilterBuilder = self)



# Anwender von FilterBuilder / Andere Datei, anderes Projekt
# filterBuilder = new FilterBuilder("myFolder/dirtyData.csv")
# filterBuilder.filterUnits().filterMissingValues().getDataFrame()