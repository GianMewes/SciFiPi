import pandas as pd

from FilterBuilder import FilterBuilder

if __name__ == '__main__':
	path = 'dirty_data/dirty_data.csv'

	filterBuilder = FilterBuilder(path)
	cleanDataFrame = filterBuilder.filterUnits().getDataFrame()

	print(str(cleanDataFrame))