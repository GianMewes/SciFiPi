import pandas as pd

from filters.Filter import Filter
from filters.DecimalShiftFilter import DecimalShiftFilter
from filters.NoiseFilter import NoiseFilter
from filters.LagFilter import LagFilter

class FilterBuilder:
	dataFrame: pd.DataFrame

	def __init__(self, data=None):
		if isinstance(data, str):
			self.dataFrame = pd.read_csv(data)
		elif isinstance(data, pd.DataFrame):
			self.dataFrame = data
		elif data is None:
			self.dataFrame = pd.DataFrame
		else:
			print("FilterBuilder: No Valid Input!")

	def getDataFrame(self):
		return self.dataFrame

	def filterDecimalShift(self):
		filter = DecimalShiftFilter()
		self.dataFrame = filter.applyFilter(self.dataFrame)
		return self

	def filterNoise(self, columnlist):
		filter = NoiseFilter()
		self.dataFrame = filter.applyFilter(self.dataFrame, columnlist)
		return self.dataFrame
	
	def filterLag(self, columnPairs):
		filter = LagFilter()
		self.dataFrame = filter.applyFilter(self.dataFrame, columnPairs)
		return self.dataFrame
