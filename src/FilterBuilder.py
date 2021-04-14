import pandas as pd

from filters.Filter import Filter
from filters.MissingValueFilter import MissingValueFilter
from filters.MatrixFilter import MatrixFilter
from filters.FormatData import FormatDataFrame
from filters.FixTimeZone import FixTimezone

class FilterBuilder:
	dataFrame: pd.DataFrame # TODO: Von Gian: Was macht diese Zeile hier?

	def __init__(self, data=None):
		if isinstance(data, str):
			self.dataFrame = pd.read_csv(data)
		elif isinstance(data, pd.DataFrame):
			self.dataFrame = data
		elif data is None:
			self.dataFrame = pd.DataFrame
		else:
			print("FilterBuilder: No Valid Input!")

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