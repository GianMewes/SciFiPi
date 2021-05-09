import pandas as pd

from preFilters.DuplicateFilter import DuplicateFilter
from preFilters.ImputationFilter import ImputationFilter

class PreFilterBuilder:
	dataFrame: pd.DataFrame

	def __init__(self, data=None):
		if isinstance(data, pd.DataFrame):
			self.dataFrame = data
		elif data is None:
			self.dataFrame = pd.DataFrame
		else:
			print("FilterBuilder: No Valid Input!")

	def filterDuplicates(self):
		filter = DuplicateFilter()
		self.dataFrame = filter.applyFilter(self.dataFrame)
		return self

	def filterImputation(self):
		filter = ImputationFilter()
		self.dataFrame = filter.applyFilter(self.dataFrame)
		return self

	def getDataFrame(self):
		return self.dataFrame