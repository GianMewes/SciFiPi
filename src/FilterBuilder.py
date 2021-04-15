import pandas as pd

from filters.Filter import Filter
from filters.MissingValueFilter import MissingValueFilter
from filters.UnitFilter import UnitFilter
from filters.ImputationFilter import ImputationFilter

class FilterBuilder:
	dataFrame: pd.DataFrame

	def __init__(self, path):
		self.dataFrame = pd.read_csv(path)

		self.dataFrame.columns = self.dataFrame.iloc[0,:]
		new_columns = self.dataFrame.iloc[0,:] 
		new_columns[0] = 'TIMESTAMP' 
		self.dataFrame.columns  = new_columns

		# drop unnecesary metadata columns
		self.dataFrame.drop([0,1], inplace = True)

		# reset index 
		self.dataFrame = self.dataFrame.reset_index(drop=True)

	def filterMissingValues(self):
		filter = MissingValueFilter()
		self.dataFrame = filter.applyFilter(self.dataFrame)
		return self

	def filterUnits(self):
		filter = UnitFilter()
		self.dataFrame = filter.applyFilter(self.dataFrame)
		return self

	def filterImputation(self):
		filter = ImputationFilter()
		self.dataFrame = filter.applyFilter(self.dataFrame)
		return self

	def getDataFrame(self):
		return self.dataFrame





# class MyFilter

# 	static myCustomFilter(obj:FilterBuilder = self)



# Anwender von FilterBuilder / Andere Datei, anderes Projekt
# filterBuilder = new FilterBuilder("myFolder/dirtyData.csv")
# filterBuilder.filterUnits().filterMissingValues().getDataFrame()