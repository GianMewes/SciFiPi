import pandas as pd

from filters.Filter import Filter
from filters.MissingValueFilter import MissingValueFilter

class FilterBuilder:
	dataFrame: pd.DataFrame

	def __init__(self, dirtyDataFrame):
		self.dataFrame = dirtyDataFrame

	def filterMissingValues(self):
		filter = MissingValueFilter()
		self.dataFrame = filter.applyFilter(self.dataFrame)
		return self

	# def filterUnits():
	# 	UnitFilter.filterUnits()
	# 	return self

	def getDataFrame(self):
		return self.dataFrame





# class MyFilter

# 	static myCustomFilter(obj:FilterBuilder = self)



# Anwender von FilterBuilder / Andere Datei, anderes Projekt
# filterBuilder = new FilterBuilder("myFolder/dirtyData.csv")
# filterBuilder.filterUnits().filterMissingValues().getDataFrame()