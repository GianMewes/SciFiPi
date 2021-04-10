import pandas as pd

from FilterBuilder import FilterBuilder

if __name__ == '__main__':
	path = "path to a csv"

	filterBuilder = FilterBuilder(path)
	cleanDataFrame = filterBuilder.filterMissingValues().getDataFrame()

	print(str(cleanDataFrame))