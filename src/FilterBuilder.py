import pandas as pd

from filters.Filter import Filter
from cleaners.FormatData import FormatDataFrame
from filters.FixTimezone import FixTimezone
from preFilters.FixTimeshifts import FixTimeshifts
from filters.UnitFilter import UnitFilter
from preFilters.ImputationFilter import ImputationFilter
from preFilters.Duplicates import Duplicates
from preFilters.FillTimestampsFilter import FillTimestampsFilter
from filters.Noise import Noise
from filters.Lag import Lag

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
	
	def removeLag(self, columnPairs):
		filter = Lag()
		self.dataFrame = filter.applyFilter(self.dataFrame, columnPairs)
		return self.dataFrame

	def fillTimestamps(self):
		filter = FillTimestampsFilter()
		self.dataFrame = filter.applyFilter(self.dataFrame)
		return self