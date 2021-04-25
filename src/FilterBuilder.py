import pandas as pd

from filters.Filter import Filter
from filters.MissingValueFilter import MissingValueFilter
from filters.MatrixFilter import MatrixFilter
from filters.FormatData import FormatDataFrame
from filters.FixTimezone import FixTimezone
from filters.FixTimeshifts import FixTimeshifts
from filters.UnitFilter import UnitFilter
from filters.ImputationFilter import ImputationFilter
from filters.Duplicates import Duplicates
from filters.Noise import Noise

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

	def fixTimezone(self):
		filter = FixTimezone()
		self.dataFrame = filter.applyFilter(self.dataFrame)
		return self

	def fixTimeshifts(self):
		filter = FixTimezone()
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

	def removeDuplicates(self):
		filter = Duplicates()
		self.dataFrame = filter.applyFilter(self.dataFrame)
		return self.dataFrame

	def removeNoise(self, columnlist):
		filter = Noise()
		self.dataFrame = filter.applyFilter(self.dataFrame, columnlist)
		return self.dataFrame